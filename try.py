from tkcalendar import *
from tkinter import *
from datetime import date
from instabot import Bot
import schedule
import time

root = Tk()
root.title("TRY")
root.geometry("1200x600")
hours = list(range(1, 25))
minutes = list(range(00, 60))

variable1 = StringVar(root)
variable1.set(hours[0])

w1 = OptionMenu(root, variable1, *hours)
w1.place(x=10, y=10, width=175)

variable2 = StringVar(root)
variable2.set(minutes[0])

w2 = OptionMenu(root, variable2, *minutes)
w2.place(x=275, y=10, width=175)


def select_time():
    my_time = variable1.get() + variable2.get()
    print(my_time)


select_time_button = Button(root, text="Select time", command=select_time)
select_time_button.place(x=300, y=350, height=50, width=100)

print(hours)
print(minutes)

root.mainloop()
