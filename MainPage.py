from tkinter import *
from PIL import ImageTk

class MainPage:

    def __init__(self, root):
        self.root = root



        #Aggiunta dell'immagine di background
        self.bg = ImageTk.PhotoImage(file="dim-gunger-oKN104dsNsY-unsplash.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

