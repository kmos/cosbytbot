from twx.botapi import TelegramBot, InputFile, InputFileInfo
from os import path
import random

bot = TelegramBot('116398301:AAExKC9Z86OgL94KnV2bklCnQEpX6Ic7_EY')

rndnumber = random.randint(2,9)
paths = 'images/bill/'
paths += `rndnumber`
paths += '.jpg'
file_path = path.relpath(paths)
file = open (file_path);
file_info = InputFileInfo('2.jpg',file,'image/jpg')
inp = InputFile('photo', file_info)
bot.send_photo(23263342,inp).wait()

