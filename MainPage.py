from tkinter import *
from instabot import Bot
import os
import glob




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

            def start_bot(event):

                cookie_del = glob.glob("config/*cookie.json")
                os.remove(cookie_del[0])

                bot = Bot()
                bot.login(username="giudoinstambot", password="Giuseppefabio1")

                # Following by hashtag
                print("Ho eseguito l'accesso correttamente")

                hashtag_text = text.get(1.0, "end-1c")
                print("il numero di hashtag ionseriti è" + hashtag_text)
                for hashtag in hashtag_text:
                    hashtag_users = bot.get_hashtag_users("vnhgb")
                    print("il numero di utenti trovati con questo hashtag è" + str(len(hashtag_users)))
                    bot.follow(hashtag_users)

                """hashtag_users = bot.get_hashtag_users("#cfttbcs")
                print(hashtag_users)

                print("ho seguito tutti")
                """
            start_follower_bot_button.bind("<Button-1>", start_bot)



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