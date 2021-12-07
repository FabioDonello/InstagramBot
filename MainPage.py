import os

if os.path.isfile("path/to/config/file.json"):
    os.remove("path/to/config/file.json")

from tkinter import *
from tkcalendar import *
from tkinter import filedialog
from datetime import date
from tkinter import ttk
from threading import Thread
from BOT_Manager import *
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
import re
import threading
import csv
from datetime import datetime
from PIL import Image, ImageTk


class MainPage:

    def __init__(self, root):
        self.root = root
        self.is_login = 0
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
        l_d_button = Button(frame_menu, text="Like", command="set")
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

        unfollow_frame = Frame(self.root, bd=5, bg="white")
        unfollow_frame.place(x=300, y=0, height=600, width=900)

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

            unfollow_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=600, width=900)

            # Set title
            auto_publish_label = Label(auto_publish_frame, text="Auto-publish", bg="steelblue", fg="white")
            auto_publish_label.place(x=0, y=0, height=50, width=200)

            # Set calendar

            cal = Calendar(auto_publish_frame, setmode='day', date_pattern='dd/mm/yyyy', mindate=date.today(),
                           background="steelblue", headersbackground="lightsteelblue", headersforeground="whitesmoke")

            cal.place(x=0, y=100, height=150, width=300)

            # Select datetime button

            def select_date():
                my_date = cal.get_date()
                selected_date = Label(auto_publish_frame, text=my_date)
                selected_date.place(x=550, y=100, height=50, width=100)
                return my_date

            select_date_button = Button(auto_publish_frame, text="Select date", command=select_date)
            select_date_button.place(x=350, y=100, height=50, width=100)

            # Set time button

            hours = ["--", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                     "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
            minutes = ["--", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                       "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                       "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46",
                       "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]

            var_hours = StringVar(auto_publish_frame)
            var_hours.set(hours[0])

            var_minutes = StringVar(auto_publish_frame)
            var_minutes.set(minutes[0])

            hours_menu = ttk.Combobox(auto_publish_frame, textvariable=var_hours, values=hours, state='readonly')
            hours_menu.place(x=450, y=175, width=50)

            minutes_menu = ttk.Combobox(auto_publish_frame, textvariable=var_minutes, values=minutes, state='readonly')
            minutes_menu.place(x=500, y=175, width=50)

            def select_time():
                time_selected = var_hours.get() + " : " + var_minutes.get()
                selected_time = Label(auto_publish_frame, text=time_selected)
                selected_time.place(x=550, y=165, height=50, width=100)
                return time_selected

            select_time_button = Button(auto_publish_frame, text="Select time", command=select_time)
            select_time_button.place(x=350, y=165, height=50, width=100)

            # Set view files selected
            table = ttk.Treeview(auto_publish_frame)
            table.place(x=0, y=285, height=150, width=350)

            table_scroll_y = ttk.Scrollbar(auto_publish_frame, orient="vertical", command=table.yview)
            table_scroll_y.place(x=350, y=285, height=150)
            table.configure(yscrollcommand=table_scroll_y.set)

            table_scroll_x = ttk.Scrollbar(auto_publish_frame, orient="horizontal", command=table.xview)
            table_scroll_x.place(x=0, y=435, width=350)
            table.configure(xscrollcommand=table_scroll_x.set)

            table['columns'] = ('File', 'Datetime')

            table.column('#0', width=0, stretch=NO)
            table.column("File", anchor=W, width=200)
            table.column("Datetime", anchor=W, width=140)

            table.heading("#0", text="")
            table.heading("File", text="File", anchor=W)
            table.heading("Datetime", text="Datetime", anchor=W)

            # Remove selected file
            def remove_file():
                global item_text
                for item in table.selection():
                    item_text = table.item(item, 'values')[0]
                    print(item_text + "\n")
                    table.delete(item)

                with open("File photo.txt", "r") as my_file:
                    lines = my_file.readlines()
                with open("File photo.txt", "w")as my_file:
                    for line in lines:
                        if line.split(sep=', ')[0] != item_text:
                            print(line.split(sep=', ')[0])
                            my_file.write(line)

            remove = Button(auto_publish_frame, text="Remove", command=remove_file)
            remove.place(x=0, y=470, height=50, width=100)

            # Sort column
            def tree_view_sort_column(tv, col):
                l = [(tv.set(k, col), k) for k in tv.get_children('')]
                l.sort(key=lambda x: datetime.strptime(x[0], '%d/%m/%Y %H:%M'))

                for index, (val, k) in enumerate(l):
                    tv.move(k, '', index)

            # Set Enter the caption
            caption_label = Label(auto_publish_frame, text="Enter the caption", bg="whitesmoke")
            caption_label.place(x=450, y=285, height=50, width=100)

            caption_frame = Frame(auto_publish_frame, bd=5, bg="silver")
            caption_frame.place(x=450, y=325, height=110, width=400)
            caption_frame.grid_columnconfigure(0, weight=1)
            caption_frame.grid_rowconfigure(0, weight=1)

            caption_text = Text(caption_frame, height=10)
            caption_text.grid(row=0, column=0, sticky="ew")

            caption_scroll = Scrollbar(caption_frame, orient="vertical", command=caption_text.yview)
            caption_scroll.grid(row=0, column=1, sticky="ns")

            caption_text['yscrollcommand'] = caption_scroll.set

            # Set Choose file button

            def choose_file():
                auto_publish_frame.filename = filedialog.askopenfilename(initialdir="/desktop",
                                                                         title="Select a file",
                                                                         filetypes=(
                                                                             ("all files", "*.*"),
                                                                             ("jpg files", "*.jpg"),
                                                                             ("jpeg files", "*.jpeg"),
                                                                             ("gif files", "*.gif"),
                                                                             ("png files", "*.png")))
                ext = os.path.splitext(auto_publish_frame.filename)
                name_file = os.path.relpath(auto_publish_frame.filename)
                date_time = (select_date() + " " + var_hours.get() + ":" + var_minutes.get())

                if name_file:
                    if ext[1] == ".jpeg" or ext[1] == ".jpg" or ext[1] == ".png" or ext[1] == ".gif":
                        if select_time() != "-- : --":
                            table.insert(parent='', index='end', values=(name_file, date_time))
                            tree_view_sort_column(table, "Datetime")
                            with open("File photo.txt", "a") as my_file:
                                my_file.write(name_file + ", " + date_time + "\n")
                            messagebox.showinfo(title='INFO',
                                                message='Do not delete or move the file to your computer, it could cause an error!')
                        else:
                            messagebox.showerror(title='ERROR', message='Select date and time')
                    else:
                        messagebox.showerror(title='ERROR', message='The file chosen is not a photo')

            choose_file_button = Button(auto_publish_frame, text="Choose file", command=choose_file,
                                        bg="whitesmoke")
            choose_file_button.place(x=200, y=0, height=50, width=100)

            # Search for files by comparing dates to upload
            def search_file():
                while True:
                    with open("File photo.txt") as my_file:
                        while True:
                            try:
                                line = my_file.readline().split(sep=', ')[1]
                            except IndexError:
                                break
                            datetime.strptime(line.strip(), '%d/%m/%Y %H:%M')
                            date_curr = datetime.now().strftime('%d/%m/%Y %H:%M')
                            print(line.strip())
                            print(date_curr)
                            if line.strip() == date_curr:
                                print("done")
                                # add method to shoot it on IG
                            time.sleep(10)

            threading.Thread(target=lambda: search_file()).start()

            # Function set to save user options
            def save_options():
                saved_file = open("Autopublish options", "w")

                # Save table
                with open("table file.csv", "w", newline='')as my_file:
                    csv_writer = csv.writer(my_file, delimiter=',')

                    for row_id in table.get_children():
                        row = table.item(row_id)['values']
                        print('save row: ', row)
                        csv_writer.writerow(row)

                saved_file.write(caption_text.get(1.0, 'end-1c') + ':')
                saved_file.close()

            # Function set to save user options
            def load_options():
                load_file = open("Autopublish options", "r")

                # load table
                with open("table file.csv") as my_file:
                    csv_read = csv.reader(my_file, delimiter=',')

                    for row in csv_read:
                        print('load row: ', row)
                        table.insert("", 'end', values=row)

                data = load_file.read()
                data_split = data.split(sep=':')
                caption_text.insert('1.0', data_split[0])
                load_file.close()

            # Set save and load button
            save_button = Button(auto_publish_frame, text="Save", command=save_options)
            save_button.place(x=300, y=0, height=50, width=100)

            load_button = Button(auto_publish_frame, text='Load', command=load_options)
            load_button.place(x=400, y=0, height=50, width=100)

            # Function set to view image
            def view_file():
                global item_text

                for item in table.selection():
                    item_text = table.item(item, 'values')[0]
                im = Image.open(item_text)
                im.show()

            view_button = Button(auto_publish_frame, text='View', command=view_file)
            view_button.place(x=150, y=470, height=50, width=100)

        def unfollow(event):
            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            unfollow_frame.place(x=300, y=0, height=600, width=900)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

            # Set titles

            follow_label = Label(unfollow_frame, text="Unfollow", bg="grey", fg="white")
            follow_label.place(x=0, y=0, height=50, width=100)

            # Start unfollower bot

            start_un_follower_bot_button = Button(unfollow_frame, text="Start", command="set")
            start_un_follower_bot_button.place(x=100, y=0, height=50, width=100)

            # Save unfollower options button

            save_un_follower_option_button = Button(unfollow_frame, text="Save", command="set")
            save_un_follower_option_button.place(x=200, y=0, height=50, width=100)

            # Options label
            un_follow_label = Label(unfollow_frame, text="Unfollow target:", bg="grey", fg="white")
            un_follow_label.place(x=0, y=75, width=900)
            un_follow_label = Label(unfollow_frame, text="Unfollow white list:", bg="grey", fg="white")
            un_follow_label.place(x=0, y=225, width=900)

            replacemant_check_var = IntVar()
            account_follower_check_var = IntVar()
            account_media_check_var = IntVar()
            account_activity_check_var = IntVar()

            def tick_manage1():
                un_follow_by_media_number_check_button.deselect()
                un_follow_by_activity_check_button.deselect()
                un_follow_by_follower_number_check_button.deselect()

            def tick_manage2():
                un_follow_after_replacement_check_button.deselect()
                un_follow_by_media_number_check_button.deselect()
                un_follow_by_activity_check_button.deselect()

            def tick_manage3():
                un_follow_after_replacement_check_button.deselect()
                un_follow_by_follower_number_check_button.deselect()
                un_follow_by_activity_check_button.deselect()

            def tick_manage4():
                un_follow_after_replacement_check_button.deselect()
                un_follow_by_follower_number_check_button.deselect()
                un_follow_by_media_number_check_button.deselect()

            un_follow_after_replacement_check_button = Checkbutton(unfollow_frame, text="Unfollow by replacemant:",
                                                                   bg="white",
                                                                   variable=replacemant_check_var,
                                                                   command=tick_manage1)
            un_follow_after_replacement_check_button.place(x=25, y=125)

            un_follow_by_follower_number_check_button = Checkbutton(unfollow_frame, text="Unfollow by account"
                                                                                         " follower:",
                                                                    bg="white",
                                                                    variable=account_follower_check_var,
                                                                    command=tick_manage2)
            un_follow_by_follower_number_check_button.place(x=25, y=175)

            un_follow_by_media_number_check_button = Checkbutton(unfollow_frame, text="Unfollow by account"
                                                                                      " media:",
                                                                 bg="white",
                                                                 variable=account_media_check_var,
                                                                 command=tick_manage3)
            un_follow_by_media_number_check_button.place(x=575, y=125)

            un_follow_by_activity_check_button = Checkbutton(unfollow_frame, text="Unfollow by account"
                                                                                  " activity:",
                                                             bg="white",
                                                             variable=account_activity_check_var,
                                                             command=tick_manage4)
            un_follow_by_activity_check_button.place(x=575, y=175)

            # ------------------------------------------------------------------------------------------------
            replacemant_time = [
                "",
                "1 day",
                "3 day",
                "5 day",
                "10 day",
                "20 day",
                "30 day",
                "70 day",
                "120 day",
            ]  # etc

            replacemant_time_var = StringVar(unfollow_frame)
            replacemant_time_var.set(replacemant_time[0])  # default value

            replacemant_option_menu = OptionMenu(unfollow_frame, replacemant_time_var, *replacemant_time)
            replacemant_option_menu.place(x=210, y=125)

            # ------------------------------------------------------------------------------------------------
            follow_number = [
                "",
                "< 50 followers",
                "< 100 followers",
                "< 150 followers",
                "< 200 followers",
                "< 400 followers",
                "< 800 followers",
                "< 1200 followers",
                "< 2000 followers",
            ]  # etc

            follow_number_var = StringVar(unfollow_frame)
            follow_number_var.set(follow_number[0])  # default value

            follow_number_option_menu = OptionMenu(unfollow_frame, follow_number_var, *follow_number)
            follow_number_option_menu.place(x=230, y=175)

            # ------------------------------------------------------------------------------------------------
            media_number = [
                "",
                "< 10 media",
                "< 20 media",
                "< 30 media",
                "< 40 media",
                "< 50 media",
                "< 60 media",
                "< 70 media",
                "< 80 media",
            ]  # etc

            media_number_var = StringVar(unfollow_frame)
            media_number_var.set(media_number[0])  # default value

            media_number_option_menu = OptionMenu(unfollow_frame, media_number_var, *media_number)
            media_number_option_menu.place(x=770, y=125)

            # ------------------------------------------------------------------------------------------------
            activity_time = [
                "",
                "1 day",
                "3 day",
                "5 day",
                "10 day",
                "20 day",
                "30 day",
                "70 day",
                "120 day",
            ]  # etc

            activity_time_var = StringVar(unfollow_frame)
            activity_time_var.set(activity_time[0])  # default value

            activity_time_option_menu = OptionMenu(unfollow_frame, activity_time_var, *activity_time)
            activity_time_option_menu.place(x=780, y=175)

            # White list
            un_follow_white_list_frame = Frame(unfollow_frame, bd=5, bg="grey")
            un_follow_white_list_frame.place(x=100, y=275, height=100, width=700)

            # apply the grid layout
            un_follow_white_list_frame.grid_columnconfigure(0, weight=1)
            un_follow_white_list_frame.grid_rowconfigure(0, weight=1)

            # create the text widget
            white_list_text = Text(un_follow_white_list_frame, height=10)
            white_list_text.grid(row=0, column=0, sticky='ew')

            # create a scrollbar widget and set its command to the text widget
            white_list_scrollbar = Scrollbar(un_follow_white_list_frame, orient='vertical',
                                             command=white_list_text.yview)
            white_list_scrollbar.grid(row=0, column=1, sticky='ns')

            #  communicate back to the scrollbar
            white_list_text['yscrollcommand'] = white_list_scrollbar.set

            def start_unfollow_bot(event):
                replacemant_value = re.findall("\d+", replacemant_time_var.get())
                follow_number_value = re.findall("\d+", follow_number_var.get())
                media_number_value = re.findall("\d+", media_number_var.get())
                activity_time_value = re.findall("\d+", activity_time_var.get())
                white_list_value = white_list_text
                a1 = [0, replacemant_value]
                a2 = [0, follow_number_value]
                a3 = [0, media_number_value]
                a4 = [0, activity_time_value]
                if replacemant_check_var.get() == 1:
                    a1[0] = 1
                if account_follower_check_var.get() == 1:
                    a2[0] = 1
                if account_media_check_var.get() == 1:
                    a3[0] = 1
                if account_media_check_var.get() == 1:
                    a4[0] = 1
                tuple_value = (a1, a2, a3, a4)
                print(tuple_value)
                t_unfollow = Thread(target=ig_unfollow, args=(tuple_value, white_list_value))
                t_unfollow.start()

            start_un_follower_bot_button.bind("<Button-1>", start_unfollow_bot)

        def direct(event):
            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=600, width=900)

            unfollow_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

            # Set titles

            direct_title_label = Label(direct_frame, text="Direct", bg="grey", fg="white")
            direct_title_label.place(x=0, y=0, height=50, width=100)

            # Start direct bot

            start_direct_bot_button = Button(direct_frame, text="Start", command="set")
            start_direct_bot_button.place(x=100, y=0, height=50, width=100)

            # Save direct options button

            save_direct_option_button = Button(direct_frame, text="Save", command="set")
            save_direct_option_button.place(x=200, y=0, height=50, width=100)

            # Options label
            direct_target_label = Label(direct_frame, text="Direct target:", bg="grey", fg="white")
            direct_target_label.place(x=0, y=75, width=900)
            direct_message_label = Label(direct_frame, text="Direct message:", bg="grey", fg="white")
            direct_message_label.place(x=0, y=325, width=900)

            follower_check_var = IntVar()
            following_check_var = IntVar()
            account_follower_check_var = IntVar()
            account_hashtag_check_var = IntVar()

            def tick_manage1():
                direct_following_check_button.deselect()
                direct_account_follower_check_button.deselect()
                direct_account_hashtag_check_button.deselect()

            def tick_manage2():
                direct_follower_check_button.deselect()
                direct_account_follower_check_button.deselect()
                direct_account_hashtag_check_button.deselect()

            def tick_manage3():
                direct_follower_check_button.deselect()
                direct_following_check_button.deselect()
                direct_account_hashtag_check_button.deselect()

            def tick_manage4():
                direct_follower_check_button.deselect()
                direct_following_check_button.deselect()
                direct_account_follower_check_button.deselect()

            direct_follower_check_button = Checkbutton(direct_frame, text="Direct your follower",
                                                       bg="white",
                                                       variable=follower_check_var,
                                                       command=tick_manage1)
            direct_follower_check_button.place(x=25, y=125)

            direct_following_check_button = Checkbutton(direct_frame, text="Direct your following",
                                                        bg="white",
                                                        variable=following_check_var,
                                                        command=tick_manage2)
            direct_following_check_button.place(x=575, y=125)

            direct_account_follower_check_button = Checkbutton(direct_frame, text="Direct an account follower:",
                                                               bg="white",
                                                               variable=account_follower_check_var,
                                                               command=tick_manage3)
            direct_account_follower_check_button.place(x=25, y=175)

            direct_account_hashtag_check_button = Checkbutton(direct_frame, text="Direct an account hashtag:",
                                                              bg="white",
                                                              variable=account_hashtag_check_var,
                                                              command=tick_manage4)
            direct_account_hashtag_check_button.place(x=575, y=175)

            # ---------------------------------------------------------------------------------------------------------
            # Account text box
            direct_account_frame = Frame(direct_frame, bd=5, bg="grey")
            direct_account_frame.place(x=25, y=200, height=100, width=250)

            # apply the grid layout
            direct_account_frame.grid_columnconfigure(0, weight=1)
            direct_account_frame.grid_rowconfigure(0, weight=1)

            # create the text widget
            account_text = Text(direct_account_frame, height=10)
            account_text.grid(row=0, column=0, sticky='ew')

            # create a scrollbar widget and set its command to the text widget
            direct_account_scrollbar = Scrollbar(direct_account_frame, orient='vertical',
                                                 command=account_text.yview)
            direct_account_scrollbar.grid(row=0, column=1, sticky='ns')

            #  communicate back to the scrollbar
            account_text['yscrollcommand'] = direct_account_scrollbar.set

            # ---------------------------------------------------------------------------------------------------------
            # Account text box
            direct_hashtag_frame = Frame(direct_frame, bd=5, bg="grey")
            direct_hashtag_frame.place(x=575, y=200, height=100, width=250)

            # apply the grid layout
            direct_hashtag_frame.grid_columnconfigure(0, weight=1)
            direct_hashtag_frame.grid_rowconfigure(0, weight=1)

            # create the text widget
            hashtag_text = Text(direct_hashtag_frame, height=10)
            hashtag_text.grid(row=0, column=0, sticky='ew')

            # create a scrollbar widget and set its command to the text widget
            direct_hashtag_scrollbar = Scrollbar(direct_hashtag_frame, orient='vertical',
                                                 command=account_text.yview)
            direct_hashtag_scrollbar.grid(row=0, column=1, sticky='ns')

            #  communicate back to the scrollbar
            hashtag_text['yscrollcommand'] = direct_hashtag_scrollbar.set

            # ---------------------------------------------------------------------------------------------------------
            # Message box
            direct_message_frame = Frame(direct_frame, bd=5, bg="grey")
            direct_message_frame.place(x=100, y=375, height=100, width=700)

            # apply the grid layout
            direct_message_frame.grid_columnconfigure(0, weight=1)
            direct_message_frame.grid_rowconfigure(0, weight=1)

            # create the text widget
            message_text = Text(direct_message_frame, height=10)
            message_text.grid(row=0, column=0, sticky='ew')

            # create a scrollbar widget and set its command to the text widget
            message_scrollbar = Scrollbar(direct_message_frame, orient='vertical',
                                          command=message_text.yview)
            message_scrollbar.grid(row=0, column=1, sticky='ns')

            #  communicate back to the scrollbar
            message_text['yscrollcommand'] = message_scrollbar.set

            def start_direct_bot(event):
                account_follower_value = account_text.get(1.0, "end-1c")
                account_follower_value = account_follower_value.split(' ')
                account_hashtag_value = hashtag_text.get(1.0, "end-1c")
                account_hashtag_value = account_hashtag_value.split(' ')
                direct_message_value = message_text
                a1 = [0]
                a2 = [0]
                a3 = [0, account_follower_value]
                a4 = [0, account_hashtag_value]
                if follower_check_var.get() == 1:
                    a1[0] = 1
                if following_check_var.get() == 1:
                    a2[0] = 1
                if account_follower_check_var.get() == 1:
                    a3[0] = 1
                if account_hashtag_check_var.get() == 1:
                    a4[0] = 1
                tuple_value = (a1, a2, a3, a4)
                print(tuple_value)
                t_direct = Thread(target=ig_direct, args=(tuple_value, direct_message_value))
                t_direct.start()

            start_direct_bot_button.bind("<Button-1>", start_direct_bot)

        def like_dislike(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=0, width=0)

            like_dislike_frame.place(x=300, y=0, height=600, width=900)

            direct_frame.place(x=300, y=0, height=0, width=0)

            unfollow_frame.place(x=300, y=0, height=0, width=0)

            auto_publish_frame.place(x=300, y=0, height=0, width=0)

            # Set Titles
            likes_label = Label(like_dislike_frame, text="Like", bg="steelblue", fg="white")
            likes_label.place(x=0, y=0, height=50, width=100)

            # Start likes bot
            start_likes_bot_button = Button(like_dislike_frame, text="Start", command="set")
            start_likes_bot_button.place(x=100, y=0, height=50, width=100)

            hashtag = IntVar()
            location_check = IntVar()
            account = IntVar()

            def hashtag_button():
                if hashtag.get() == 1:
                    hashtag_check_button["bg"] = "green"
                if hashtag.get() == 0:
                    hashtag_check_button["bg"] = "steelblue"

            def location_button():
                if location_check.get() == 1:
                    location_check_button["bg"] = "green"
                if location_check.get() == 0:
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
                                                variable=location_check, command=location_button)
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
            location_likes_label = Label(like_dislike_frame, text="Enter the position you prefer")
            location_likes_label.place(x=20, y=300, height=50, width=200)

            location_likes_frame = Frame(like_dislike_frame, bd=5, bg="silver")
            location_likes_frame.place(x=20, y=345, height=50, width=700)

            location_likes_frame.grid_columnconfigure(0, weight=1)
            location_likes_frame.grid_rowconfigure(0, weight=1)

            location_text = Text(location_likes_frame, height=10)
            location_text.grid(row=0, column=0, sticky="ew")

            location_scrollbar = Scrollbar(location_likes_frame, orient="vertical", command=location_text.yview)
            location_scrollbar.grid(row=0, column=1, sticky="ns")

            location_text['yscrollcommand'] = location_scrollbar.set

            # Function set to save user options
            def save_options():
                saved_file = open("Likes options", "w")

                saved_file.write(hashtag_text.get(1.0, 'end-1c') + ":")
                saved_file.write(location_text.get(1.0, 'end-1c') + ':')
                saved_file.write(account_text.get(1.0, 'end-1c') + ':')

                saved_file.close()

            # Function set to save user options
            def load_options():
                load_file = open("Likes options", "r")

                data = load_file.read()
                data_split = data.split(':')
                hashtag_text.insert('1.0', data_split[0])
                location_text.insert('1.0', data_split[1])
                account_text.insert('1.0', data_split[2])

                load_file.close()

            # Save and load likes option button
            save_likes_options_button = Button(like_dislike_frame, text="Save", command=save_options)
            save_likes_options_button.place(x=200, y=0, height=50, width=100)

            load_likes_options_button = Button(like_dislike_frame, text='Load', command=load_options)
            load_likes_options_button.place(x=300, y=0, height=50, width=100)

            # Function set for start bot

        def follow(event):

            dashboard_frame.place(x=300, y=0, height=0, width=0)

            follow_frame.place(x=300, y=0, height=600, width=900)

            like_dislike_frame.place(x=300, y=0, height=0, width=0)

            direct_frame.place(x=300, y=0, height=0, width=0)

            unfollow_frame.place(x=300, y=0, height=0, width=0)

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

            if self.is_login == 1:
                dashboard_frame.place(x=300, y=0, height=600, width=900)

                follow_frame.place(x=300, y=0, height=0, width=0)

                like_dislike_frame.place(x=300, y=0, height=0, width=0)

                direct_frame.place(x=300, y=0, height=0, width=0)

                unfollow_frame.place(x=300, y=0, height=0, width=0)

                auto_publish_frame.place(x=300, y=0, height=0, width=0)

                # Set titles

                dashboard_label = Label(dashboard_frame, text="Dashboard", bg="grey", fg="white")
                dashboard_label.place(x=0, y=0, height=50, width=100)

                # Logout
                logout_button = Button(dashboard_frame, text="Logout", command="set")
                logout_button.place(x=100, y=0, height=50, width=100)
                f = open("Credenziali", "r")
                username = f.readline()
                f.close()
                account_text = "Actually account: " + str(username)
                print(account_text)
                dashboard_label = Label(dashboard_frame, text=account_text, bg="grey", fg="white")
                dashboard_label.place(x=225, y=0, height=50)
                statistics_label = Label(dashboard_frame, text="Statistics:", bg="grey", fg="white")
                statistics_label.place(x=0, y=75, width=900)

                # Actually account:
                def logout(event):
                    t_logout = Thread(target=ig_logout)
                    t_logout.start()
                    self.is_login = 0
                    dashboard(0)

                logout_button.bind("<Button-1>", logout)

            else:
                # Login with ig credential in a file
                dashboard_frame.place(x=300, y=0, height=0, width=0)
                # Create instagram login frame
                instagram_background_login_frame = Frame(self.root, bd=5, bg="white")
                instagram_background_login_frame.place(x=300, y=0, height=600, width=900)

                # Set title of login frame
                instagram_login_frame_title = Label(instagram_background_login_frame,
                                                    text="Login in corso:",
                                                    bg="white")
                instagram_login_frame_title.place(x=400, y=250)

                background_progress = ttk.Progressbar(instagram_background_login_frame, orient=HORIZONTAL,
                                                      length=100, mode='determinate', )
                background_progress.place(x=400, y=275)
                background_progress['value'] = 0

                def progress_control():
                    for a in range(100):
                        background_progress['value'] = a
                        time.sleep(0.01)
                    ig_background_login_check()

                t_bk_pb = Thread(target=progress_control)
                t_bk_pb.start()
                var1 = 0
                proxy_list1 = getProxies()
                t1_bk_login = Thread(target=ig_login, args=(proxy_list1, "", "", var1))
                t1_bk_login.start()

                def ig_background_login_check():
                    background_progress.destroy()
                    log_file_str = os.listdir(
                        r"C:\Users\39377\Desktop\InstaBot\config\log")
                    log_file = open(r"C:\Users\39377\Desktop\InstaBot\config\log\\"
                                    + log_file_str[0], "r")
                    ll = StringVar
                    for last_line in log_file:
                        ll = last_line
                        pass
                    if "Username or password is incorrect" in ll:
                        messagebox.showinfo("Login fail", "Username or password wrong")
                        dashboard(0)
                    if "too many requests" in ll:
                        messagebox.showinfo("Login fail", "To many request from instagram, wait 5 minutes")
                        dashboard(0)
                    self.is_login = 1
                    instagram_background_login_frame.destroy()
                    dashboard(0)

                # ----------------------------------------------------------------------------------------------------
                # Login with a request of ig credential
                if credential == "":
                    print("maaaa")
                    dashboard_frame.place(x=300, y=0, height=0, width=0)
                    # Create instagram login frame
                    instagram_login_frame = Frame(self.root, bd=5, bg="white")
                    instagram_login_frame.place(x=300, y=0, height=600, width=900)

                    # Set title of login frame
                    instagram_login_frame_title = Label(instagram_login_frame,
                                                        text="Prima di accedere alle funzionalità "
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
                            instagram_info_label = Label(instagram_login_frame, text="Login in process: ",
                                                         bg="white")
                            instagram_info_label.place(x=0, y=195, height=50, width=150)
                            progress = ttk.Progressbar(instagram_login_frame, orient=HORIZONTAL,
                                                       length=100, mode='determinate', )
                            progress.place(x=175, y=215)
                            progress['value'] = 0

                            def progress_control():
                                for a in range(100):
                                    progress['value'] = a
                                    time.sleep(0.3)
                                ig_login_check()

                            t_pb = Thread(target=progress_control)
                            t_pb.start()
                            var1 = 1

                            t1_login = Thread(target=ig_login,
                                              args=(proxy_list1, username_text, password_text, var1))
                            t1_login.start()

                            def ig_login_check():
                                progress.destroy()
                                log_file_str = os.listdir(
                                    r"C:\Users\39377\Desktop\InstaBot\config\log")
                                log_file = open(r"C:\Users\39377\Desktop\InstaBot\config\log\\"
                                                + log_file_str[0], "r")
                                ll = StringVar
                                for last_line in log_file:
                                    ll = last_line
                                    pass
                                if "Username or password is incorrect" in ll:
                                    messagebox.showinfo("Login fail", "Username or password wrong")
                                    dashboard(0)
                                if "too many requests" in ll:
                                    messagebox.showinfo("Login fail",
                                                        "To many request from instagram, wait 5 minutes")
                                    dashboard(0)
                                self.is_login = 1
                                instagram_login_frame.destroy()
                                dashboard(0)

                    instagram_access_button.bind("<Button-1>", access_try)

        auto_publish_button.bind("<Button-1>", auto_publish)
        unfollow_button.bind("<Button-1>", unfollow)
        direct_button.bind("<Button-1>", direct)
        l_d_button.bind("<Button-1>", like_dislike)
        follow_button.bind("<Button-1>", follow)
        dashboard_button.bind("<Button-1>", dashboard)

        dashboard(0)
