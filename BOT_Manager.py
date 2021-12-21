from instabot import Bot
import os
import glob
import time
from geopy.geocoders import Nominatim
import requests
from requests.auth import HTTPProxyAuth
import shutil
from instabot import API
import math
from PIL import Image
import threading

file_path = r'C:\Users\39377\Desktop\InstaBot\config\log'
shutil.rmtree(file_path)
bot = Bot(filter_private_users=False, filter_users=False)
file_id = format(id(bot))


def richieste():
    print(bot.api.total_requests)


def is_login():
    return bot.api.is_logged_in


def ig_login(username, password, var):
    # cookie_del = glob.glob("config/*cookie.json")
    # os.remove(cookie_del[0])
    # proxy="Selfabiodonello989:J0q9FyC@45.8.197.222:45785"
    richieste()
    print("faccio il login")
    if var == 1:
        bot.login(username=username, password=password, use_cookie=True, is_threaded=True)
        f = open("Credenziali", "w")
        f.write(username)
        f.write(":")
        f.write(password)
        f.close()
        print("Login riuscito senza avere le credenziali")
    if var == 0:
        f = open("Credenziali", "r")
        text = f.read()
        text = text.split(":")
        username = text[0]
        password = text[1]
        print(username)
        print(password)
        f.close()
        bot.login(username=username, password=password, use_cookie=True, is_threaded=True)
        print("Login riuscito avendo le credenziali")
        b = bot.api.is_logged_in
        print(b)


def ig_logout():
    f = open("Credenziali", "r")
    username = f.readline()
    f.close()
    f = open("Credenziali", "w").close()
    # bot.logout(username=username, is_threaded=True)
    print("Logout eseguito")


# Set follow
def ig_follow_hashtag(hashtags):
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
    print(accounts)
    for account in accounts:
        users = bot.get_user_followers(account)
        print(time.sleep(300))
        for user in users:
            bot.follow(user)
            print(time.sleep(300))


# Set Likes
def ig_likes_hashtag(hashtags):
    if hashtags:
        for hashtag in hashtags:
            print('like by hashtag')
            bot.like_hashtag(hashtag=hashtag)
            # ensures 40 likes/h
            time.sleep(90)


def ig_likes_location(location):
    if location:
        app = Nominatim(user_agent="tutorial")
        localization = app.geocode(location).raw

        latitude = float(localization['lat'])
        longitude = float(localization['lon'])
        position = bot.get_locations_from_coordinates(latitude=latitude, longitude=longitude)

        for positions in position:
            bot.like_location_feed(place=positions, amount=1)
            print('like by location')
            time.sleep(90)


def ig_likes_account(accounts):
    if accounts:
        for account in accounts:
            bot.like_followers(user_id=account)
            print('Like by account')
            time.sleep(90)


def likes_stp(var):
    global tmp
    if var == 1:
        tmp = True
    if var == 2:
        tmp = False


# Set auto-publish
def ig_upload_photo(photo, caption):
    im = Image.open(photo)
    new_size = (1080, 1080)
    im1 = im.resize(new_size)
    im1.save(photo)
    bot.upload_photo(photo=photo, caption=caption)
    bot.approve_pending_thread_requests()


val = False


def unfollow_stp(a):
    global val
    if a == 1:
        val = True
    if a == 2:
        val = False


def ig_unfollow(list_value, white_list):
    f_name = r"C:\Users\39377\Desktop\InstaBot\config\followed.txt"

    def file_len(f_name):
        with open(f_name, "r") as followed_file:
            for i, l in enumerate(followed_file):
                pass
        return i + 1

    followed_file_len = file_len(f_name)
    print(followed_file_len)
    with open(f_name, "r") as followed_file:
        for y in range(followed_file_len):
            if val:
                print("unfollow interrotto")
                return
            user_id = followed_file.readline()
            print(user_id)
            time.sleep(2)
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
        f_name = r"C:\Users\39377\Desktop\InstaBot\config\followed.txt"

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


def ig_get_follow_number():
    """f = open("Credenziali", "r")
    username = f.readline()
    f.close()
    bot.get_user_followers(username)
    n_folloewr = len(username)
    f_name = r"/Users/fabiodonello/Desktop/Esame OOP/InstgramBot_2/config/data/followed_data.txt"
    f1 = open(f_name, "a")
    print(str(n_folloewr)+":")
    f1.close()"""


def ig_get_like_number():
    """f = open("Credenziali", "r")
    username = f.readline()
    f.close()
    medias_id = bot.get_user_medias(username)
    n_like = 0
    n_post = len(medias_id)
    for media in medias_id:
        like = 20
        media_info = bot.get_media_info(media)
        like = like + media['like']
    f_name = r"/Users/fabiodonello/Desktop/Esame OOP/InstgramBot_2/config/data/like_data.txt"
    f2 = open(f_name, "a")
    print(str(n_like) + ":")
    f2.close()"""
