from instabot import Bot
import os
import glob
import time

bot = Bot()
file_id = format(id(bot))
x = 0

def ig_login(proxy_list, username, password, var):
    #cookie_del = glob.glob("config/*cookie.json")
    #os.remove(cookie_del[0])
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

def ig_follow_hashtag(hashtags):
    while x == 0:
        print("aspetto il login")
        time.sleep(2)

    print(hashtags)
    for hashtag in hashtags:
        users = bot.get_hashtag_users(hashtag)
        print(time.sleep(300))
        for user in users:
            bot.follow(users)
            print(time.sleep(300))


def ig_follow_location(location):
    print(location)


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




