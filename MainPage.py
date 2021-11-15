from tkinter import *

import os

if os.path.isfile("path/to/config/file.json"):
    os.remove("path/to/config/file.json")

from instabot import Bot
import glob
import argparse
import sys
from tkinter import ttk
from threading import Thread
from BOT_Manager import *
import queue
import requests
from bs4 import BeautifulSoup


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
            follow_by_account_check_button.place(x=10, y=400, width=900)

            # Follow by hashtag options

            hashtag_follow_label = Label(follow_frame, text="Insert hashtag:")
            hashtag_follow_label.place(x=20, y=100, height=50, width=100)

            hashtag_follow_frame = Frame(follow_frame, bd=5, bg="grey")
            hashtag_follow_frame.place(x=20, y=140, height=100, width=700)

            # apply the grid layout
            hashtag_follow_frame.grid_columnconfigure(0, weight=1)
            hashtag_follow_frame.grid_rowconfigure(0, weight=1)

            # create the text widget
            text = Text(hashtag_follow_frame, height=10)
            text.grid(row=0, column=0, sticky='ew')

            # create a scrollbar widget and set its command to the text widget
            scrollbar = Scrollbar(hashtag_follow_frame, orient='vertical', command=text.yview)
            scrollbar.grid(row=0, column=1, sticky='ns')

            #  communicate back to the scrollbar
            text['yscrollcommand'] = scrollbar.set

            # Follow by location option

            country_check_var = IntVar()
            region_check_var = IntVar()
            city_check_var = IntVar()

            def country_options():
                if country_check_var.get() == 1:
                    location_country_follow_check_button["bg"] = "green"
                if country_check_var.get() == 0:
                    location_country_follow_check_button["bg"] = "grey"

            def region_option():
                if region_check_var.get() == 1:
                    location_region_follow_check_button["bg"] = "green"
                if region_check_var.get() == 0:
                    location_region_follow_check_button["bg"] = "grey"

            def city_options():
                if city_check_var.get() == 1:
                    location_city_follow_check_button["bg"] = "green"
                if city_check_var.get() == 0:
                    location_city_follow_check_button["bg"] = "grey"

            location_country_follow_check_button = Checkbutton(follow_frame, text="Follow by country:", bg="grey",
                                                               variable=country_check_var, command=country_options)
            location_country_follow_check_button.place(x=70, y=330, width=175)

            country = [
                "-------",
                "Albania",
                "Andorra",
                "Armenia",
                "Austria",
                "Azerbaigian",
                "Bielorussia",
                "Belgio",
                "Bosnia",
                "Cipro",
                "Croazia",
                "Danimarca",
                "Estonia",
                "Francia",
                "Georgia",
                "Germania",
                "Grecia",
                "Italia",
                "Irlanda",
                "Islanda",
                "Lettonia",
                "Liechtenstein",
                "Lituania",
                "Lussemburgo",
                "Malta",
                "Moldavia",
                "Monaco",
                "Montenegro",
                "Norvegia",
                "Paesi Bassi",
                "Polonia",
                "Portogallo",
                "Regno Unito",
                "Repubblica ceca",
                "Romania",
                "Russia",
                "San Marino",
                "Serbia",
                "Slovacchia",
                "Slovenia",
                "Spagna",
                "Svezia",
                "Svizzera",
                "Turchia",
                "Ucraina",
                "Ungheria",

            ]  # etc

            variable1 = StringVar(follow_frame)
            variable1.set(country[0])  # default value

            w1 = OptionMenu(follow_frame, variable1, *country)
            w1.place(x=70, y=350, width=175)

            #  communicate back to the scrollbar
            text['yscrollcommand'] = scrollbar.set

            location_region_follow_check_button = Checkbutton(follow_frame, text="Follow by region:", bg="grey",
                                                              variable=region_check_var, command=region_option)
            location_region_follow_check_button.place(x=356, y=330, width=175)

            region = [
                "-------",
                "Valle d’Aosta",
                "Piemonte",
                "Liguria",
                "Lombardia",
                "Trentino Alto Adige*",
                "Veneto",
                "Friuli-Venezia Giulia",
                "Emilia-Romagna",
                "Toscana",
                "Umbria",
                "Marche",
                "Lazio",
                "Abruzzo",
                "Molise",
                "Campania",
                "Puglia",
                "Basilicata",
                "Calabria",
                "Sicilia",
                "Sardegna",
            ]  # etc

            variable2 = StringVar(follow_frame)
            variable2.set(region[0])  # default value

            w2 = OptionMenu(follow_frame, variable2, *region)
            w2.place(x=356, y=350, width=175)

            #  communicate back to the scrollbar
            text['yscrollcommand'] = scrollbar.set

            location_city_follow_check_button = Checkbutton(follow_frame, text="Follow by city:", bg="grey",
                                                            variable=city_check_var, command=city_options)
            location_city_follow_check_button.place(x=642, y=330, width=175)

            city = [
                "-------",
                "Bologna",
                "Ferrara",
                "Forlì-Cesena",
                "Modena",
                "Parma",
                "Piacenza",
                "Ravenna",
                "Reggio Emilia",
                "Rimini",
            ]  # etc

            variable3 = StringVar(follow_frame)
            variable3.set(city[0])  # default value

            w3 = OptionMenu(follow_frame, variable3, *city)
            w3.place(x=642, y=350, width=175)

            #  communicate back to the scrollbar
            text['yscrollcommand'] = scrollbar.set

            # Follow by account

            account_follow_label = Label(follow_frame, text="Insert account:")
            account_follow_label.place(x=20, y=425, height=50, width=100)

            account_follow_frame = Frame(follow_frame, bd=5, bg="grey")
            account_follow_frame.place(x=20, y=465, height=100, width=700)

            # apply the grid layout
            account_follow_frame.grid_columnconfigure(0, weight=1)
            account_follow_frame.grid_rowconfigure(0, weight=1)

            # create the text widget
            text1 = Text(account_follow_frame, height=10)
            text1.grid(row=0, column=0, sticky='ew')

            # create a scrollbar widget and set its command to the text widget
            scrollbar1 = Scrollbar(account_follow_frame, orient='vertical', command=text1.yview)
            scrollbar1.grid(row=0, column=1, sticky='ns')

            #  communicate back to the scrollbar
            text1['yscrollcommand'] = scrollbar1.set

            def start_follow_bot(event):

                # Follow by hashtag:
                if hashtag_check_var == 1:
                    hashtags = text.get(1.0, "end-1c")
                    hashtags = hashtags.split(' ')
                    if hashtags:
                        t_follow_hashtag = Thread(target=ig_follow_hashtag, args=(hashtags,))
                        t_follow_hashtag.start()
                # Follow by location
                if location_check_var == 1:
                    locations = variable1
                    if locations:
                        t_follow_location = Thread(target=ig_follow_location, args=(locations,))
                        t_follow_location.start()
                # Follow by account
                if account_check_var == 1:
                    print(account_check_var)
                    accounts = text1.get(1.0, "end-1c")
                    accounts = accounts.split(',')
                    if accounts:
                        t_follow_account = Thread(target=ig_follow_account, args=(accounts,))
                        t_follow_account.start()

            start_follower_bot_button.bind("<Button-1>", start_follow_bot)

        def dashboard(event):

            f = open("Credenziali", "r")
            credential = f.read()
            f.close()

            def getProxies():
                r = requests.get('https://free-proxy-list.net/')
                soup = BeautifulSoup(r.content, 'html.parser')
                table = soup.find('tbody')
                proxies = []
                for row in table:
                    if row.find_all('td')[4].text == 'elite proxy':
                        proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
                        proxies.append(proxy)
                    else:
                        pass
                return proxies

            if credential != "":

                dashboard_frame.place(x=300, y=0, height=600, width=900)

                follow_frame.place(x=300, y=0, height=0, width=0)

                like_dislike_frame.place(x=300, y=0, height=0, width=0)

                direct_frame.place(x=300, y=0, height=0, width=0)

                statistics_frame.place(x=300, y=0, height=0, width=0)

                auto_publish_frame.place(x=300, y=0, height=0, width=0)

                proxy_list0 = getProxies()
                var0 = 0
                t0_login = Thread(target=ig_login, args=(proxy_list0, "", "", var0))
                t0_login.start()

            else:
                dashboard_frame.place(x=300, y=0, height=0, width=0)
                # Create instagram login frame
                instagram_login_frame = Frame(self.root, bd=5, bg="white")
                instagram_login_frame.place(x=300, y=0, height=600, width=900)

                # Set title of login frame
                instagram_login_frame_title = Label(instagram_login_frame, text="Prima di accedere alle funzionalità "
                                                                                "di giudoinstabot accedi al profilo"
                                                                                " instagram che vuoi gestire: ",
                                                    bg="white")
                instagram_login_frame_title.place(x=0, y=30)

                # Insertion box Email & password

                instagram_username_label = Label(instagram_login_frame, text="Username", bg="white")
                instagram_username_label.place(x=0, y=85, height=50, width=150)
                instagram_password_label = Label(instagram_login_frame, text="Password", bg="white")
                instagram_password_label.place(x=0, y=136, height=50, width=150)

                instagram_username_entry = Entry(instagram_login_frame, bg="yellow")
                instagram_username_entry.place(x=175, y=85, height=50, width=240)
                instagram_password_entry = Entry(instagram_login_frame, bg="yellow", show="*")
                instagram_password_entry.place(x=175, y=135, height=50, width=240)

                check_var1 = IntVar()

                def show_password():
                    if check_var1.get() == 1:
                        instagram_password_entry["show"] = ""
                    if check_var1.get() == 0:
                        instagram_password_entry["show"] = "*"

                instagram_password_check_box = Checkbutton(instagram_login_frame, text="show password",
                                                           variable=check_var1, command=show_password)

                instagram_access_button = Button(instagram_login_frame, text="Login", command="set")
                instagram_access_button.place(x=0, y=195, height=50, width=150)

                # Access management

                def access_try(event):
                    username_text = instagram_username_entry.get()
                    password_text = instagram_password_entry.get()
                    print(username_text)
                    print(password_text)
                    if username_text and password_text:
                        proxy_list1 = getProxies()
                        instagram_access_button.destroy()
                        instagram_info_label = Label(instagram_login_frame, text="Login in process: ", bg="white")
                        instagram_info_label.place(x=0, y=195, height=50, width=150)
                        progress = ttk.Progressbar(instagram_login_frame, orient=HORIZONTAL,
                                                   length=30, mode='determinate', )
                        progress.place(x=175, y=215)
                        progress['value'] = 0

                        def progress_control():
                            for a in range(30):
                                progress['value'] = a
                                time.sleep(1)
                            check()

                        t_pb = Thread(target=progress_control)
                        t_pb.start()
                        var1 = 1

                        t1_login = Thread(target=ig_login, args=(proxy_list1, username_text, password_text, var1))
                        t1_login.start()

                        def check():
                            """progress.destroy()
                            time.sleep(3)
                            file_log = open(file_id + "", "r")
                            file_text = file_log.read()
                            print(file_text)
                            """

                instagram_access_button.bind("<Button-1>", access_try)

        auto_publish_button.bind("<Button-1>", auto_publish)
        unfollow_button.bind("<Button-1>", unfollow)
        direct_button.bind("<Button-1>", direct)
        l_d_button.bind("<Button-1>", like_dislike)
        follow_button.bind("<Button-1>", follow)
        dashboard_button.bind("<Button-1>", dashboard)

        dashboard(0)
