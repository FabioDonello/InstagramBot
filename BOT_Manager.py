from instabot import Bot
import os
import glob
import time

import datetime
import MainPage
from geopy.geocoders import Nominatim
from apscheduler.schedulers.blocking import BlockingScheduler

import shutil

file_path = r'C:\Users\39377\Desktop\InstaBot\config\log'
shutil.rmtree(file_path)
bot = Bot()
file_id = format(id(bot))
x = 0


def ig_login(proxy_list, username, password, var):
    # cookie_del = glob.glob("config/*cookie.json")
    # os.remove(cookie_del[0])
    if var == 1:
        # bot.login(username=username, password=password, is_threaded=True)
        f = open("Credenziali", "w")
        f.write(username)
        f.write("\n")
        f.write(password)
        f.close()

        print("Login riuscito A")

    if var == 0:
        f = open("Credenziali", "r")
        username = f.readline()
        password = f.readline()
        f.close()
        # bot.login(username=username, password=password, is_threaded=True)
        x = 1
        print("Login riuscito B")


def ig_logout():
    f = open("Credenziali", "r")
    username = f.readline()
    f.close()
    f = open("Credenziali", "w").close()
    # bot.logout(username=username, is_threaded=True)
    print("Logout eseguito")


# Set follow
def ig_follow_hashtag(hashtags):
    while x == 0:
        print("aspetto il login")
        time.sleep(2)

    print(hashtags)
    for hashtag in hashtags:
        users = bot.get_hashtag_users(hashtag)
        print(time.sleep(300))
        for user in users:
            bot.follow(user)
            print(time.sleep(300))


def ig_follow_location(location):
    app = Nominatim(user_agent="tutorial")
    localization = app.geocode(location).raw

    latitude = localization['lat']
    longitude = localization['lon']
    position = bot.get_locations_from_coordinates(latitude=latitude, longitude=longitude)

    for positions in position:
        user_position = bot.get_geotag_users(geotag=positions)
        for users in user_position:
            bot.follow_followers(user_id=users)
            time.sleep(240)


def ig_follow_account(accounts):
    while x == 0:
        print("aspetto il login")
        time.sleep(2)

    print(accounts)
    for account in accounts:
        users = bot.get_user_followers(account)
        print(time.sleep(300))
        for user in users:
            bot.follow(user)
            print(time.sleep(300))


# Set Likes
def ig_likes_hashtag(hashtags):
    for hashtag in hashtags:
        medias = bot.get_hashtag_medias(hashtag)
        for media in medias:
            bot.like(media)
            time.sleep(30)


def ig_likes_location(location):
    app = Nominatim(user_agent="tutorial")
    localization = app.geocode(location).raw

    latitude = localization['lat']
    longitude = localization['lon']
    position = bot.get_locations_from_coordinates(latitude=latitude, longitude=longitude)

    amount = 850
    while amount != 0:
        bot.like_location_feed(place=position, amount=1)
        time.sleep(40)
        amount = amount - 1


def ig_likes_account(accounts):
    for account in accounts:
        bot.like_followers(user_id=account, nlikes=3)
        time.sleep(90)


# Set auto-publish
'''def ig_upload_photo():
    print("Done")
    print(datetime.datetime.now())

def schedule_upload_photo():

    scheduler = BlockingScheduler(timezone='Europe/Rome')
    n = 2
    while n != 0:
        scheduler.add_job(ig_upload_photo, 'interval', seconds=20)
         print(datetime.datetime.now())
        n = n - 1
        scheduler.get_jobs()
        time.sleep(10)

scheduler.start()
'''


def ig_unfollow(list_value, white_list):
    f_name = r"/Users/fabiodonello/Desktop/Esame OOP/InstgramBot_2/config/followed.txt"

    def file_len(f_name):
        with open(f_name, "r") as followed_file:
            for i, l in enumerate(followed_file):
                pass
        return i + 1

    followed_file_len = file_len(f_name)
    print(followed_file_len)
    with open(f_name, "r") as followed_file:
        for y in range(followed_file_len):
            user_id = followed_file.readline()
            print(user_id)
            """user_info = bot.get_user_info(user_id)            
            time.sleep(3)
            if list_value[0][0] == 1:
                if user_info['giorno in cui mi ha iniziato a seguire'] + list_value[0][1] > "data odierna":
                    if user_info['username'] not in white_list:
                        bot.unfollow(user_id)
                        time.sleep(3)
            if list_value[1][0] == 1:
                if user_info['follower'] < list_value[1][1] :
                    if user_info['username'] not in white_list:
                        bot.unfollow(user_id)
                        time.sleep(3)
            if list_value[2][0] == 1:
                if user_info['numero media'] < list_value[2][1] :
                    if user_info['username'] not in white_list:
                        bot.unfollow(user_id)
                        time.sleep(3)
            if list_value[3][0] == 1:
                if (user_info['data ultimo post'] and user_info['data ultimo storia']) < list_value[3][1]:
                    if user_info['username'] not in white_list:
                        bot.unfollow(user_id)
                        time.sleep(3) """


def ig_direct(list_value, message):
    # Direct your follower
    if list_value[0][0] == 1:
        f = open("Credenziali", "r")
        username = f.readline()
        f.close()
        following = bot.get_user_following(username)
        following_id = bot.convert_to_user_id(following)
        for user in following_id:
            bot.send_message(user, message)

    # Direct your following
    if list_value[1][0] == 1:
        print("sono dentro")
        f_name = r"/Users/fabiodonello/Desktop/Esame OOP/InstgramBot_2/config/followed.txt"

        def file_len(f_name):
            with open(f_name, "r") as followed_file:
                for i, l in enumerate(followed_file):
                    pass
            return i + 1

        followed_file_len = file_len(f_name)
        print(followed_file_len)
        with open(f_name, "r") as followed_file:
            for y in range(followed_file_len):
                user_id = followed_file.readline()
                print(user_id)
                bot.send_message(user_id, message)
                time.sleep(3)

    # Direct your account follower
    if list_value[2][0] == 1:
        for account in list_value[2][1]:
            account_id = bot.convert_to_user_id(account)
            account_followers = bot.get_user_followers(account_id)
            time.sleep(3)
            for account_follower in account_followers:
                bot.send_message(account_follower, message)
                time.sleep(3)

    # Direct with hashtag
    if list_value[3][0] == 1:
        for hashtag in list_value[3][1]:
            hashtag_users = bot.get_hashtag_users(hashtag)
            time.sleep(3)
            for hashtag_user in hashtag_users:
                bot.send_message(hashtag_user, message)
                time.sleep(3)
