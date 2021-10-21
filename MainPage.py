from tkinter import *
from instabot import Bot

class MainPage:

    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Tool")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)

        # Create main menu frame
        frame_menu = Frame(self.root, bd=0, bg="black")
        frame_menu.place(x=0, y=0, height=600, width=300)

        # Set button of main menu

        # Dashboard button
        dashboard_button = Button(frame_menu, text="Dashboard", command="set")
        dashboard_button.place(x=0, y=0, height=100, width=300)

        # Follow and unfollow button
        follow_unfollow_button = Button(frame_menu, text="Follow & Unfollow", command="set")
        follow_unfollow_button.place(x=0, y=100, height=100, width=300)

        # Like and dislike button
        l_d_button = Button(frame_menu, text="Like & Dislike", command="set")
        l_d_button.place(x=0, y=200, height=100, width=300)

        # Direct button
        direct_button = Button(frame_menu, text="Direct", command="set")
        direct_button.place(x=0, y=300, height=100, width=300)

        # Auto publish button
        auto_publish_button = Button(frame_menu, text="Auto publish", command="set")
        auto_publish_button.place(x=0, y=400, height=100, width=300)

        # Statistics button
        statistics_button = Button(frame_menu, text="Statistics", command="set")
        statistics_button.place(x=0, y=500, height=100, width=300)

        # Create Instagram login frame
        instagram_account_frame = Frame(self.root, bd=5, bg="black")
        instagram_account_frame.place(x=330, y=150, height=400, width=500)

        # Set title of Instagram login frame
        instagram_account_label = Label(instagram_account_frame, text="Login", bg="white")
        instagram_account_label.place(x=20, y=25)

        # Insertion box username & password of Instagram account
        instagram_username = Entry(instagram_account_frame, bg="yellow")
        instagram_username.place(x=20, y=75, height=50, width=300)
        instagram_password = Entry(instagram_account_frame, bg="yellow")
        instagram_password.place(x=20, y=140, height=50, width=300)

        instagram_access_button = Button(instagram_account_frame, text="Login", command="set")
        instagram_access_button.place(x=20, y=210, height=50, width=150)

        def get_username_password(event):
            instagram_account_username = instagram_username.get()
            instagram_account_password = instagram_password.get()

            return (instagram_account_username, instagram_account_password)


        instagram_access_button.bind("<Button-1>", get_username_password)






























