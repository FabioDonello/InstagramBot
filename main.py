from tkinter import *
from Login import Login
import DB_Manager

if __name__ == "__main__":

    print("Apro la finestra di login")

    DB_Manager.db_create()
    root = Tk()
    step1 = Login(root)
    root.mainloop()