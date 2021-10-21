from tkinter import *
from PIL import ImageTk
from MainPage import MainPage
import DB_Add
import DB_Update


class Login:

    # Constructor della class

    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Tool")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)

        # Background image
        self.bg_login_image = ImageTk.PhotoImage(file="rid1.png")
        self.bg_login = Label(self.root, image=self.bg_login_image).place(x=0, y=0, relheight=2, relwidth=2)

        # Create login frame
        frame_login = Frame(self.root, bd=5, bg="black")
        frame_login.place(x=330, y=150, height=400, width=500)

        # Set title of login frame
        frame_login_title = Label(frame_login, text="Login", bg="white")
        frame_login_title.place(x=20, y=25)

        # Insertion box username & password
        username = Entry(frame_login, bg="yellow")
        username.place(x=20, y=75, height=50, width=300)
        password = Entry(frame_login, bg="yellow")
        password.place(x=20, y=140, height=50, width=300)

        # Username & password button
        access_button = Button(frame_login, text="Login", command="set")
        access_button.place(x=20, y=210, height=50, width=150)
        registration_button = Button(frame_login, text="Registration", command="set")
        registration_button.place(x=190, y=210, height=50, width=150)

        # Access management

        def access_try(event):
            username_text = username.get()
            password_text = password.get()

            db_table = DB_Update.main()


            for a in db_table:
                print(a[0])
                print(a[1])
                if username_text == a[0] and password_text == a[1]:
                    frame_login.destroy()
                    MainPage(self.root)
               # else:
                    #     if username_text != a[0] and password_text == a[1]:
                    #   username["background"] = "red"
                    #   password["background"] = "green"

                    # if username_text == a[0] and password_text != a[1]:
                        #username["background"] = "green"
                        #password["background"] = "red"

                    # if username_text != a[0] and password_text != a[1]:
                        #username["background"] = "red"
                        #password["background"] = "red"
        access_button.bind("<Button-1>", access_try)

        # Registration manage
        def register_try(event):
            # Creation of registration frame
            registration_frame = Frame(self.root, bd=5, bg="black")
            registration_frame.place(x=330, y=150, height=500, width=600)

            # Registration frame title
            frame_registration_title = Label(registration_frame, text="Registration", bg="white")
            frame_registration_title.place(x=20, y=25)

            # Username & password insertion box
            first_name = Entry(registration_frame, bg="yellow")
            first_name.place(x=20, y=75, height=50, width=300)
            last_name = Entry(registration_frame, bg="yellow")
            last_name.place(x=20, y=140, height=50, width=300)
            email = Entry(registration_frame, bg="yellow")
            email.place(x=20, y=205, height=50, width=300)

            # Registration button
            registration_confirm = Button(registration_frame, text="Registration", command="set")
            registration_confirm.place(x=20, y=280, height=50, width=150)

            # Registration manage

            def registration_manage():
                first_name_text = first_name.get()
                last_name_text = last_name.get()
                email_text = email.get()

                DB_Add.main(first_name_text, last_name_text, email_text)

                registration_frame.destroy()

            registration_confirm.bind("<Button-1>", registration_manage)

        registration_button.bind("<Button-1>", register_try)
