from instabot import Bot
import os
import glob
import time
import shutil

file_path = '/Users/fabiodonello/Desktop/Esame OOP/InstgramBot_2/config/log/'
shutil.rmtree(file_path)
bot = Bot()
file_id = format(id(bot))
x = 0

def ig_login(proxy_list, username, password, var):
    #cookie_del = glob.glob("config/*cookie.json")
    #os.remove(cookie_del[0])
    if var == 1:
        #bot.login(username=username, password=password, is_threaded=True)
        f = open("Credenziali", "w")
        f.write(username)
        f.write("\n")
        f.write(password)
        f.close()

        print("Login riuscito")

    if var == 0:
        f = open("Credenziali", "r")
        username = f.readline()
        password = f.readline()
        #bot.login(username=username, password=password, is_threaded=True)
        f.close()
        x = 1
        print("Login riuscito")


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
