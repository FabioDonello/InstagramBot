from tkinter import *
from Login import Login
import DB_Manager
import shutil

if __name__ == "__main__":
    DB_Manager.db_create()
    root = Tk()
    step1 = Login(root)
    root.mainloop()
