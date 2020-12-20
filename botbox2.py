#!/usr/bin/python3
import telegram
import glob
import re
import linecache
import os

#Telegram bot token
bot_token = '1472124370:AAHvfvCVm7HUUf1IFUP7Ny4JpLjImwbRwdU'

#autopi dedicated chat, chat ID
bot_chatID = '707348795'
bot = telegram.Bot(token=bot_token)


#print(bot.get_me())

      
#Post photo to telegram chat
def postTelegramPic(timeStamp):
      bot.send_photo(chat_id=bot_chatID, photo=open('./images/piPic.jpg', 'rb'))
      bot.send_message(chat_id=bot_chatID, text=timeStamp)

#Post all mp4 videos contained in the images folder to telegram chat
def postTelegramVid(timeStamp):
      for file in glob.glob('./images/*.mp4'):
         fileName = os.path.basename(file)
         bot.send_video(chat_id=bot_chatID, video=open(file, 'rb'), supports_streaming=True)
         bot.send_message(chat_id=bot_chatID, text=fileName + " : " +timeStamp)

#Send current location to telegram
def postTelegramMsg(timeStamp):
     gpsDataFile = './gps.txt'
     lat = re.sub('[\n]', '', linecache.getline(gpsDataFile, 1))
     long = re.sub('[\n]', '', linecache.getline(gpsDataFile, 2))
     bot.sendLocation(chat_id=bot_chatID, latitude=lat, longitude=long)
     bot.send_message(chat_id=bot_chatID, text="Hey, here's my current location!\n" + timeStamp)