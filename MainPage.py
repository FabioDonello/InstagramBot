from tkinter import *


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

        # Frame manege
        dashboard_frame = Frame(self.root, bd=5, bg="white")
        dashboard_frame.place(x=300, y=0, height=600, width=900)

        # Set title of login frame
        dashboard_label = Label(dashboard_frame, text="Dashboard", bg="white")
        dashboard_label.place(x=150, y=25)

        def auto_publish():
            auto_publish_frame = Frame(self.root, bd=5, bg="white")
            auto_publish_frame.place(x=300, y=0, height=600, width=900)
            auto_publish_label = Label(auto_publish_frame, text="auto public", bg="white")
            auto_publish_label.place(x=150, y=25)

        def statistics():
            statistics_frame = Frame(self.root, bd=5, bg="white")
            statistics_frame.place(x=300, y=0, height=600, width=900)
            statistics_label = Label(statistics_frame, text="statistics", bg="white")
            statistics_label.place(x=150, y=25)

        def direct():
            direct_frame = Frame(self.root, bd=5, bg="white")
            direct_frame.place(x=300, y=0, height=600, width=900)
            direct_label = Label(direct_frame, text="direct", bg="white")
            direct_label.place(x=150, y=25)

        def like_dislike():
            like_dislike_frame = Frame(self.root, bd=5, bg="white")
            like_dislike_frame.place(x=300, y=0, height=600, width=900)
            like_dislike_label = Label(like_dislike_frame, text="like & dislike", bg="white")
            like_dislike_label.place(x=150, y=25)

        def follow_unfollow():
            follow_unfollow_frame = Frame(self.root, bd=5, bg="white")
            follow_unfollow_frame.place(x=300, y=0, height=600, width=900)
            follow_unfollow_label = Label(follow_unfollow_frame, text="follow & unfollow", bg="white")
            follow_unfollow_label.place(x=150, y=25)

        def dashboard():
            dashboard_frame = Frame(self.root, bd=5, bg="white")
            dashboard_frame.place(x=300, y=0, height=600, width=900)
            dashboard_label = Label(dashboard_frame, text="dashboard", bg="white")
            dashboard_label.place(x=150, y=25)

        dashboard_button.bind("<Button-1>", dashboard())
        follow_unfollow_button.bind("<Button-1>", follow_unfollow())
        l_d_button.bind("<Button-1>", like_dislike())
        direct_button.bind("<Button-1>", direct())
        auto_publish_button.bind("<Button-1>", auto_publish())
        statistics_button.bind("<Button-1>", statistics())
