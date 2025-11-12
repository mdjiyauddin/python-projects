from tkinter import *
import time

# Create main window
clock = Tk()
clock.title("***** Digital Clock *****")
clock.geometry("1000x500")
clock.config(bg="light green")

# Heading label
title_label = Label(clock, text="Digital Clock", font=("times new roman", 50, "bold"), bg="yellow", fg="red")
title_label.pack(pady=40)

# Time display label
time_label = Label(clock, font=("ds-digital", 100, "bold"), bg="yellow", fg="blue")
time_label.pack(pady=50)

# Date display label
date_label = Label(clock, font=("times new roman", 30, "bold"), bg="yellow", fg="green")
date_label.pack()

# Function to update time every second
def update_time():
    current_time = time.strftime("%H:%M:%S %p")  # Hour:Minute:Second AM/PM
    current_date = time.strftime("%A, %d %B %Y")  # Day, Date Month Year
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    clock.after(1000, update_time)  # update every 1 second

# Start the clock
update_time()

# Run window
clock.mainloop()
