"""
whatsapp_automator.py
Simple WhatsApp Web automator:
- Reads contacts.csv
- Sends immediate messages or schedules at given HH:MM
Requirements: selenium, webdriver-manager, pandas, schedule
"""

import time
import logging
import urllib.parse
from datetime import datetime
import pandas as pd
import schedule

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------
# Configuration / Globals
# -------------------------
CHROME_PROFILE = None  # Optional: path to Chrome profile to stay logged in. None uses fresh profile.
WAIT_TIMEOUT = 30      # seconds to wait for elements
RETRY_COUNT = 2
RETRY_DELAY = 5        # seconds
LOGFILE = "whatsapp_automator.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOGFILE, encoding='utf-8'), logging.StreamHandler()]
)

# -------------------------
# WebDriver Setup
# -------------------------
def create_driver():
    options = webdriver.ChromeOptions()
    # keep browser visible so user can scan QR; don't use headless
    options.add_argument("--start-maximized")
    if CHROME_PROFILE:
        options.add_argument(f"--user-data-dir={CHROME_PROFILE}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# -------------------------
# Wait until user logged in
# -------------------------
def wait_for_login(driver):
    logging.info("Opening WhatsApp Web... Please scan QR in the opened browser if not already logged in.")
    driver.get("https://web.whatsapp.com/")
    # Wait until main UI is loaded: look for the search box or the main app div
    try:
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab]"))
        )
        logging.info("Logged into WhatsApp Web (or UI is ready).")
    except Exception as e:
        logging.error("Timed out waiting for WhatsApp Web login/ready: %s", e)
        raise

# -------------------------
# Send message function
# -------------------------
def send_message(driver, phone, message, wait_for_open=10):
    """
    phone: in +XXXXXXXXX format
    message: text string
    """
    phone_digits = phone.replace("+", "").replace(" ", "").replace("-", "")
    encoded_msg = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={phone_digits}&text={encoded_msg}"
    logging.info("Preparing to send message to %s", phone)
    for attempt in range(1, RETRY_COUNT + 2):
        try:
            driver.get(url)
            # Wait for chat input box to appear
            input_xpath = "//div[@contenteditable='true' and @data-tab]"
            WebDriverWait(driver, WAIT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
            # Sometimes the message is in the URL prefilled; pressing ENTER sends it.
            input_box = driver.find_element(By.XPATH, input_xpath)
            time.sleep(1)  # small pause to ensure text present
            input_box.send_keys(Keys.ENTER)
            logging.info("Message sent to %s", phone)
            time.sleep(2)  # brief pause after send
            return True
        except Exception as e:
            logging.warning("Attempt %s: failed to send to %s: %s", attempt, phone, e)
            if attempt <= RETRY_COUNT:
                logging.info("Retrying in %s seconds...", RETRY_DELAY)
                time.sleep(RETRY_DELAY)
            else:
                logging.error("All retries failed for %s", phone)
                return False

# -------------------------
# Job wrapper (for scheduler)
# -------------------------
def job_send(driver, phone, message, name=None):
    name = name or phone
    logging.info("Job started for %s", name)
    ok = send_message(driver, phone, message)
    if ok:
        logging.info("Job done: message delivered to %s", name)
    else:
        logging.error("Job failed for %s", name)

# -------------------------
# Read CSV & schedule
# -------------------------
def load_and_schedule(driver, csv_path="contacts.csv"):
    df = pd.read_csv(csv_path, dtype=str).fillna("")
    # expected columns: name, phone, message, time, send_now
    for idx, row in df.iterrows():
        name = row.get("name", "").strip() or f"contact_{idx}"
        phone = row.get("phone", "").strip()
        message = row.get("message", "").strip()
        t = row.get("time", "").strip()
        send_now = row.get("send_now", "").strip().lower() in ("yes", "true", "1", "y")

        if not phone or not message:
            logging.warning("Skipping %s: phone or message missing.", name)
            continue

        if send_now:
            # send immediately
            logging.info("Sending immediately to %s (%s)", name, phone)
            job_send(driver, phone, message, name=name)
        elif t:
            # schedule daily at HH:MM
            try:
                dt = datetime.strptime(t, "%H:%M")
                hhmm = dt.strftime("%H:%M")
                logging.info("Scheduling daily message to %s at %s", name, hhmm)
                # use schedule library
                schedule.every().day.at(hhmm).do(job_send, driver=driver, phone=phone, message=message, name=name)
            except ValueError:
                logging.error("Invalid time format for %s: %s (expected HH:MM)", name, t)
        else:
            logging.info("No schedule or immediate flag for %s — skipping.", name)

# -------------------------
# Main
# -------------------------
def main():
    driver = create_driver()
    try:
        wait_for_login(driver)
    except Exception:
        logging.error("Cannot continue without login.")
        driver.quit()
        return

    load_and_schedule(driver, csv_path="contacts.csv")

    # run pending scheduled jobs
    logging.info("Scheduler started. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Stopping by user request.")
    finally:
        driver.quit()
        logging.info("Closed browser and exiting.")

if __name__ == "__main__":
    main()
