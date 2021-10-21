from tkinter import *
from Login import Login
import DB_Create

if __name__ == "__main__":

    print("Apro la finestra di login")

    DB_Create.main()
    root = Tk()
    step1 = Login(root)
    root.mainloop()