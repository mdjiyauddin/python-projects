
# 📧 Simple Email Sender using Python (smtplib)
# Author: MD Jiyauddin
# Description:
# This script sends an email through Gmail using SMTP protocol.
# It demonstrates basic email automation using Python.


import smtplib as s

# Create an SMTP session
server = s.SMTP('smtp.gmail.com', 587)
server.ehlo()        # Identify yourself to the server
server.starttls()    # Secure the connection

# Login credentials
sender_email = "your_email@gmail.com"
password = "your_app_password"

# Login to Gmail
server.login(sender_email, password)

# Email details
subject = "Test Python"
body = "I love Python ❤️"

# Message formatting
message = f"Subject: {subject}\n\n{body}"

# List of recipients
receiver_list = ["receiver1@gmail.com", "receiver2@gmail.com"]

# Sending the mail
server.sendmail(sender_email, receiver_list, message)
print("✅ Email sent successfully!")

# Terminate the session
server.quit()
