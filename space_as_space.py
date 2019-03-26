import requests
import os
from instabot import Bot
from dotenv import load_dotenv
load_dotenv()

def upload_picture_to_inst_account(name):
    bot = Bot()
    insta_login = os.getenv("INSTA_LOGIN")
    insta_pass = os.getenv("INSTA_PASS")
    bot.login(username=insta_login, password=insta_pass)
    bot.upload_photo("images/"+str(name), caption="")


if __name__ == '__main__':
    upload_picture_to_inst_account('spacex0.jpg')
