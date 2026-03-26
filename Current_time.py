from tkinter import Tk;
from tkinter import Label;
import time;

root = Tk()
root.title("Time")

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label1.config(text = current_time)
    label1.after(500, update_time)

label1 = Label(root, font=("Arial", 50), fg="red", bg="black", bd=10)
label1.pack()
update_time()

root.mainloop()
