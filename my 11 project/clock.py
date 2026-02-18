import tkinter as tk
from time import strftime

root = tk.Tk()

# title for  Digital clock ......
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 80, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

time()

root.mainloop()
