from tkinter import *
import os

if os.path.isfile("path/to/config/file.json"):
    os.remove("path/to/config/file.json")

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

        # Dashboard button
        dashboard_button = Button(frame_menu, text="Dashboard", command="set")
        dashboard_button.place(x=0, y=0, height=100, width=300)

        # Follow button
        follow_button = Button(frame_menu, text="Follow", command="set")
        follow_button.place(x=0, y=100, height=100, width=300)

        # Unfollow button
        unfollow_button = Button(frame_menu, text="Unfollow", command="set")
        unfollow_button.place(x=0, y=200, height=100, width=300)

        # Like and dislike button
        l_d_button = Button(frame_menu, text="Like & Dislike", command="set")
        l_d_button.place(x=0, y=300, height=100, width=300)

        # Direct button
        direct_button = Button(frame_menu, text="Direct", command="set")
        direct_button.place(x=0, y=400, height=100, width=300)

        # Auto publish button
        auto_publish_button = Button(frame_menu, text="Auto publish", command="set")
        auto_publish_button.place(x=0, y=500, height=100, width=300)

        # Frame manege
        auto_publish_frame = Frame(self.root, bd=5, bg="white")
        auto_publish_frame.place(x=300, y=0, height=600, width=900)

        statistics_frame = Frame(self.root, bd=5, bg="white")
        statistics_frame.place(x=300, y=0, height=600, width=900)

        direct_frame = Frame(self.root, bd=5, bg="white")
        direct_frame.place(x=300, y=0, height=600, width=900)

        like_dislike_frame = Frame(self.root, bd=5, bg="white")
        like_dislike_frame.place(x=300, y=0, height=600, width=900)

        follow_frame = Frame(self.root, bd=5, bg="white")
        follow_frame.place(x=300, y=0, height=600, width=900)

        dashboard_frame = Frame(self.root, bd=5, bg="white")
        dashboard_frame.place(x=300, y=0, height=600, width=900)

        def auto_publish(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=600, width=900)

        def unfollow(event):
            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=600, width=900)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

        def direct(event):
            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=600, width=900)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

        def like_dislike(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=600, width=900)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

            # Set Titles
            likes_label = Label(like_dislike_frame, text="Like", bg="steelblue", fg="white")
            likes_label.place(x=0, y=0, height=50, width=100)

            # Start likes bot
            start_likes_bot_button = Button(like_dislike_frame, text="Start", command="set")
            start_likes_bot_button.place(x=100, y=0, height=50, width=100)

            # Save likes option button
            save_likes_options_button = Button(like_dislike_frame, text="Save", command="set")
            save_likes_options_button.place(x=200, y=0, height=50, width=100)

            hashtag = IntVar()
            location = IntVar()
            account = IntVar()

            def hashtag_button():
                if hashtag.get() == 1:
                    hashtag_check_button["bg"] = "green"
                if hashtag.get() == 0:
                    hashtag_check_button["bg"] = "steelblue"

            def location_button():
                if location.get() == 1:
                    location_check_button["bg"] = "green"
                if location.get() == 0:
                    location_check_button["bg"] = "steelblue"

            def account_button():
                if account.get() == 1:
                    account_check_button["bg"] = "green"
                if account.get() == 0:
                    account_check_button["bg"] = "steelblue"

            hashtag_check_button = Checkbutton(like_dislike_frame, text="Likes by hashtag", bg="steelblue",
                                               variable=hashtag, command=hashtag_button)
            hashtag_check_button.place(x=10, y=75, width=900)

            location_check_button = Checkbutton(like_dislike_frame, text="Likes by location", bg="steelblue",
                                                variable=location, command=location_button)
            location_check_button.place(x=10, y=275, width=900)

            account_check_button = Checkbutton(like_dislike_frame, text="Likes by account", bg="steelblue",
                                               variable=account, command=account_button)
            account_check_button.place(x=10, y=400, width=900)

            # Set likes by hashtag
            hashtag_likes_label = Label(like_dislike_frame, text="Enter hashtag", bg="whitesmoke")
            hashtag_likes_label.place(x=20, y=100, height=50, width=100)

            hashtag_likes_frame = Frame(like_dislike_frame, bd=5, bg="silver")
            hashtag_likes_frame.place(x=20, y=140, height=100, width=700)

            hashtag_likes_frame.grid_columnconfigure(0, weight=1)
            hashtag_likes_frame.grid_rowconfigure(0, weight=1)

            hashtag_text = Text(hashtag_likes_frame, height=10)
            hashtag_text.grid(row=0, column=0, sticky="ew")

            # Create a scrollbar for the hashtag text
            hashtag_scrollbar = Scrollbar(hashtag_likes_frame, orient="vertical", command=hashtag_text.yview)
            hashtag_scrollbar.grid(row=0, column=1, sticky="ns")

            hashtag_text['yscrollcommand'] = hashtag_scrollbar.set

            # Set likes by account
            account_likes_label = Label(like_dislike_frame, text="Enter account")
            account_likes_label.place(x=20, y=425, height=50, width=100)

            account_likes_frame = Frame(like_dislike_frame, bd=5, bg="silver")
            account_likes_frame.place(x=20, y=465, height=100, width=700)

            account_likes_frame.grid_columnconfigure(0, weight=1)
            account_likes_frame.grid_rowconfigure(0, weight=1)

            account_text = Text(account_likes_frame, height=10)
            account_text.grid(row=0, column=0, sticky="ew")

            # Create a scrollbar for the account text
            account_scrollbar = Scrollbar(account_likes_frame, orient="vertical", command=account_text.yview)
            account_scrollbar.grid(row=0, column=1, sticky="ns")

            account_text['yscrollcommand'] = account_scrollbar.set

            # Set likes by location


        def follow(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=600, width=900)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

            # Set titles

            follow_label = Label(follow_frame, text="Follow", bg="grey", fg="white")
            follow_label.place(x=0, y=0, height=50, width=100)

            # set options

            # Start follower bot

            start_follower_bot_button = Button(follow_frame, text="Start", command="set")
            start_follower_bot_button.place(x=100, y=0, height=50, width=100)

            # Save follower options button

            save_follower_option_button = Button(follow_frame, text="Save", command="set")
            save_follower_option_button.place(x=200, y=0, height=50, width=100)

            hashtag_check_var = IntVar()
            location_check_var = IntVar()
            account_check_var = IntVar()

            def hashtag_options():
                if hashtag_check_var.get() == 1:
                    follow_by_hashtag_check_button["bg"] = "green"
                if hashtag_check_var.get() == 0:
                    follow_by_hashtag_check_button["bg"] = "grey"

            def location_option():
                if location_check_var.get() == 1:
                    follow_by_location_check_button["bg"] = "green"
                if location_check_var.get() == 0:
                    follow_by_location_check_button["bg"] = "grey"

            def account_options():
                if account_check_var.get() == 1:
                    follow_by_account_check_button["bg"] = "green"
                if account_check_var.get() == 0:
                    follow_by_account_check_button["bg"] = "grey"

            follow_by_hashtag_check_button = Checkbutton(follow_frame, text="Follow by hashtag:", bg="grey",
                                                         variable=hashtag_check_var, command=hashtag_options)
            follow_by_hashtag_check_button.place(x=10, y=75, width=900)

            follow_by_location_check_button = Checkbutton(follow_frame, text="Follow by location:", bg="grey",
                                                          variable=location_check_var, command=location_option)
            follow_by_location_check_button.place(x=10, y=275, width=900)

            follow_by_account_check_button = Checkbutton(follow_frame, text="Follow by account:", bg="grey",
                                                         variable=account_check_var, command=account_options)
            follow_by_account_check_button.place(x=10, y=475, width=900)

        def dashboard(event):

            dashboard_frame.place(x=300, y=0, height=600, width=900)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

        auto_publish_button.bind("<Button-1>", auto_publish)
        unfollow_button.bind("<Button-1>", unfollow)
        direct_button.bind("<Button-1>", direct)
        l_d_button.bind("<Button-1>", like_dislike)
        follow_button.bind("<Button-1>", follow)
        dashboard_button.bind("<Button-1>", dashboard)
