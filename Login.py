from tkinter import *
from PIL import ImageTk
from MainPage import MainPage
from validate_email import validate_email
import DB_Manager
from tkinter import messagebox


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
        frame_login = Frame(self.root, bd=5, bg="white")
        frame_login.place(x=400, y=100, height=300, width=400)

        # Set title of login frame
        frame_login_title = Label(frame_login, text="Login", bg="white")
        frame_login_title.place(x=150, y=25)

        # Insertion box Email & password

        email_label = Label(frame_login, text="Email", bg="grey", fg="white")
        email_label.place(x=0, y=85, height=50, width=150)
        password_label = Label(frame_login, text="Password", bg="grey", fg="white")
        password_label.place(x=0, y=136, height=50, width=150)

        email_entry = Entry(frame_login, bg="yellow")
        email_entry.place(x=150, y=85, height=50, width=240)
        password_entry = Entry(frame_login, bg="yellow", show="*")
        password_entry.place(x=150, y=135, height=50, width=240)

        check_var1 = IntVar()

        def show_password():
            if check_var1.get() == 1:
                password_entry["show"] = ""
            if check_var1.get() == 0:
                password_entry["show"] = "*"

        password_check_box = Checkbutton(frame_login, text="show password",
                                         variable=check_var1, command=show_password)
        password_check_box.place(x=0, y=190)

        # Username & password button
        access_button = Button(frame_login, text="Login", command="set")
        access_button.place(x=20, y=230, height=50, width=150)
        registration_button = Button(frame_login, text="Registration", command="set")
        registration_button.place(x=190, y=230, height=50, width=150)

        # Access management

        def access_try(event):
            username_text = email_entry.get()
            password_text = password_entry.get()

            db_table = DB_Manager.db_update(username_text[0])

            print(db_table)

            if db_table:
                for a in db_table:
                    if username_text == a[0] and password_text == a[1]:
                        frame_login.destroy()
                        MainPage(self.root)
                    else:
                        messagebox.showinfo("Login fail", "Username or password wrong")
            else:
                messagebox.showinfo("Login fail", "Username or password wrong")

        access_button.bind("<Button-1>", access_try)

        # Registration manage
        def register_try(event):

            # Creation of registration frame
            registration_frame = Frame(self.root, bd=5, bg="white")
            registration_frame.place(x=350, y=100, height=400, width=500)

            # Registration frame title
            frame_registration_title = Label(registration_frame, text="Registration", bg="white")
            frame_registration_title.place(x=20, y=25)

            # Register label
            name_label_register = Label(registration_frame, text="Name", bg="grey", fg="white")
            name_label_register.place(x=0, y=85, height=50, width=150)

            surname_label_register = Label(registration_frame, text="Surname", bg="grey", fg="white")
            surname_label_register.place(x=0, y=136, height=50, width=150)

            email_label_register = Label(registration_frame, text="Email", bg="grey", fg="white")
            email_label_register.place(x=0, y=187, height=50, width=150)

            password_label_register = Label(registration_frame, text="Password", bg="grey", fg="white")
            password_label_register.place(x=0, y=238, height=50, width=150)

            # Register insertion box
            first_name_entry_register = Entry(registration_frame, bg="yellow")
            first_name_entry_register.place(x=150, y=85, height=50, width=300)

            last_name_entry_register = Entry(registration_frame, bg="yellow")
            last_name_entry_register.place(x=150, y=136, height=50, width=300)

            email_entry_register = Entry(registration_frame, bg="yellow")
            email_entry_register.place(x=150, y=187, height=50, width=300)

            password_entry_register = Entry(registration_frame, bg="yellow")
            password_entry_register.place(x=150, y=238, height=50, width=300)

            # Registration button
            registration_confirm = Button(registration_frame, text="Registration", command="set")
            registration_confirm.place(x=175, y=300, height=50, width=150)

            # Registration manage
            def registration_manage(event):

                first_name_text = first_name_entry_register.get()
                last_name_text = last_name_entry_register.get()
                email_text = email_entry_register.get()
                password_text = password_entry_register.get()

                # Check email
                check_email = validate_email(email_text, check_mx=True)
                if check_email:
                    DB_Manager.db_add(first_name_text, last_name_text, email_text, password_text)
                    registration_frame.destroy()
                else:
                    messagebox.showerror(title='Message', message='Email is not valid')

            registration_confirm.bind("<Button-1>", registration_manage)

        registration_button.bind("<Button-1>", register_try)
