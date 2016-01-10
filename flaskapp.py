import os
import json
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

from twx.botapi import TelegramBot, ReplyKeyboardMarkup, InputFile, InputFileInfo
from os import path
import feedparser
import random

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

token = '<insert token bot>'
page = 'http://telegrambot-uninacar.rhcloud.com/Updates'

def vice():
 rss = 'http://www.vice.com/it/rss'
 parsedRss = feedparser.parse(rss)
 entries = len(parsedRss['entries'])
 rndEntry = random.randint(1,entries)
 link = parsedRss.entries[rndEntry]['link']
return link

def bill():
 rndnumber = random.randint(2,9)
 paths = 'images/bill/'
 paths += `rndnumber`
 paths += '.jpg'
 file_path = path.relpath(paths)
 file = open (file_path);
 file_info = InputFileInfo('2.jpg',file,'image/jpg')
 inp = InputFile('photo', file_info)
return inp

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
 return send_from_directory('static/', resource)

@app.route("/start" , methods =['GET'])
def start():
 bot = TelegramBot(token)
 bot.update_bot_info().wait()
 print(bot.username)
 #foto belle -33909375 
 #user_id = int(23263342)

 #result = bot.send_message(user_id, 'Salve ragazzi').wait()
 #XXX WebHook automatico non funzionante
 result = bot.set_webhook(token)
 print('*****Il risultato:' % (result))
 return "ok"

@app.route("/Updates" , methods=['POST'])
def update():
 bot = TelegramBot(token)
 bot.update_bot_info().wait()

 if 'chat' in request.json['message']:
  chat = request.json['message']['chat']['id']
  if 'text' in request.json['message']:
   text = request.json['message']['text']
   if text.find('vice') != -1:
    bot.send_message(chat, vice()).wait()
   if text.find('drink') != -1:
    bot.send_photo(chat,bill()).wait()

 #Print in console for fast Debugging
 print(json.dumps(request.json))
 return "ok"

if __name__ == '__main__':
 app.run()
