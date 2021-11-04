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
        auto_publish_frame = Frame(self.root, bd=5, bg="white")
        auto_publish_frame.place(x=300, y=0, height=600, width=900)

        statistics_frame = Frame(self.root, bd=5, bg="white")
        statistics_frame.place(x=300, y=0, height=600, width=900)

        direct_frame = Frame(self.root, bd=5, bg="white")
        direct_frame.place(x=300, y=0, height=600, width=900)

        like_dislike_frame = Frame(self.root, bd=5, bg="white")
        like_dislike_frame.place(x=300, y=0, height=600, width=900)

        follow_unfollow_frame = Frame(self.root, bd=5, bg="white")
        follow_unfollow_frame.place(x=300, y=0, height=600, width=900)

        dashboard_frame = Frame(self.root, bd=5, bg="white")
        dashboard_frame.place(x=300, y=0, height=600, width=900)

        # Page title
        page_title_label = Label(self.root, text="Dashboard", bg="white")
        page_title_label.place(x=350, y=50)

        def auto_publish(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_unfollow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=600, width=900)
            page_title_label["text"] = "Auto publish"

        def statistics(event):
            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_unfollow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=600, width=900)
            page_title_label["text"] = "Statistics"

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

        def direct(event):
            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_unfollow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=600, width=900)
            page_title_label["text"] = "Direct"

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

        def like_dislike(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_unfollow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=600, width=900)
            page_title_label["text"] = "Like and dislike"

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

        def follow_unfollow(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_unfollow_frame.place(x=300, y=0, height=600, width=900)
            page_title_label["text"] = "Follow and unfollow"

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

        def dashboard(event):

            dashboard_frame.place(x=300, y=0, height=600, width=900)
            page_title_label["text"] = "Dashboard"

            follow_unfollow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            statistics_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)


        auto_publish_button.bind("<Button-1>", auto_publish)
        statistics_button.bind("<Button-1>", statistics)
        direct_button.bind("<Button-1>", direct)
        l_d_button.bind("<Button-1>", like_dislike)
        follow_unfollow_button.bind("<Button-1>", follow_unfollow)
        dashboard_button.bind("<Button-1>", dashboard)





















































