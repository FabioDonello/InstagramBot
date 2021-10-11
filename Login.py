from tkinter import *



class Login:


    #Costruttore della classe
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Manage")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)

        # Creazione del frame per il login
        Frame_login = Frame(self.root, bd=5, bg="black")
        Frame_login.place(x=330, y=150, height=400, width=500)

        # Titolo del frame di login
        Frame_login_title = Label(Frame_login, text="Login", bg="white")
        Frame_login_title.place(x=20, y=25)

        # Campi di inserimento Username & password
        Username = Entry(Frame_login, bg="yellow")
        Username.place(x=20, y=75, height=50, width=300)
        Password = Entry(Frame_login, bg="yellow")
        Password.place(x=20, y=140, height=50, width=300)

        #Bottoni di interazione
        Accedi = Button(Frame_login, text="Accedi", command="set")
        Accedi.place(x=20, y=210, height=50, width=150)
        Registrati = Button(Frame_login, text="Registrati", command="set")
        Registrati.place(x=190, y=210, height=50, width=150)


        print("La finestra è stata aperta")










