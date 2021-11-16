from instabot import Bot
import os
import glob
import time
import MainPage
from geopy.geocoders import Nominatim

bot = Bot()
file_id = format(id(bot))
x = 0


def ig_login(proxy_list, username, password, var):
    # cookie_del = glob.glob("config/*cookie.json")
    # os.remove(cookie_del[0])
    if var == 1:
        bot.login(username=username, password=password, is_threaded=True)
        f = open("Credenziali", "w")
        f.write(username)
        f.write("\n")
        f.write(password)
        f.close()

        print("Login riuscito")

    if var == 0:
        try:
            f = open("Credenziali", "r")
            username = f.readline()
            password = f.readline()
            bot.login(username=username, password=password)
            f.close()
            x = 1
            print("Login riuscito")
        except:
            print("Login non riuscito: B ")


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
'''def ig_upload_photo(photo,date)'''