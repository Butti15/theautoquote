#!/usr/bin/env python3
import requests
from requests import get
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
import telebot # pyTelegramBotAPI library
import pyfiglet
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from instabot import Bot
from requests import get
import time
import os
import textwrap

#Advertisment
belowmsg="@theautoquote"

#Extracting Quote from website //Step-1
def quote():
	url = 'http://t.me/s/UQuotes'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='tgme_widget_message_text')

	List = []
	count=0 #to get only top 5 news
	for i in cl:
		count=count+1
		if(count==2):
			break
		List.append(i.text)
	return [i.replace('"','').
	replace(",",",\n").
	replace(".","\n").
	replace("➖ @uQuotes ➖","") for i in List]

List=quote()
List.append("\n"+belowmsg)
abcd = " ".join(List)
#print (abcd)

#Removing Old Files //Step-2
#Removing Old Config Json Folder
'''
directory = "theautoquote_uuid_and_cookie.json" #Directory name
parent = "config" #Parent Directory
'''
path = r'/mnt/build2/butti/test/quote/config/theautoquotes_uuid_and_cookie.json' #Path

#Remove the Directory
try:
    os.remove(path)
    print("Directory of Config has been removed successfully")
except OSError as error:
    print(error)
    print("Directory of Config can not be removed")

#Removing the old Image
path2 = 'quote.jpeg.REMOVE_ME'

try:
    os.remove(path2)
    print("Directory of Image has been removed successfully")
except OSError as error:
    print(error)
    print("Directory of Image can not be removed")

#Create Image object with the input image //Step-3
img = Image.open(r'/mnt/build2/butti/test/quote/Backgrounds/testo.png')

#Initialise the drawing context with the image object as background
draw = ImageDraw.Draw(img)

#Create font object with the font file and specify desired size
font_path = r'/mnt/build2/butti/test/quote/Font/calibrili.ttf'
font = ImageFont.truetype(font_path, size=42, encoding='unic')

#Breaking Lines
def break_fix(text, width, font, draw):
    if not text:
        return
    lo = 0
    hi = len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        t = text[:mid]
        w, h = draw.textsize(t, font=font)
        if w <= width:
            lo = mid
        else:
            hi = mid - 21
    t = text[:lo]
    w, h = draw.textsize(t, font=font)
    yield t, w, h
    yield from break_fix(text[lo:], width, font, draw)

def fit_text(img, text, color, font):
    width = img.size[0] - 2
    draw = ImageDraw.Draw(img)
    pieces = list(break_fix(text, width, font, draw))
    height = sum(p[2] for p in pieces)
    if height > img.size[1]:
        raise ValueError("text doesn't fit")
    y = (img.size[1] - height) // 2
    for t, w, h in pieces:
        x = (img.size[0] - w) // 2
        draw.text((x, y), t, font=font, fill=color, align="center")
        y += h

fit_text(img, abcd, (0,0,0), font)
img = img.convert("RGB")
img.save('quote.jpeg', "JPEG", quality=100, optimize=True)

#If You want to displayimage
#img.show()

#Sending to Instagram //Step-4
bot = Bot()
bot.login(username = "theautoquote",
		password = "Butti@1432")

bot.upload_photo('quote.jpeg',
                caption ="#Quote of the day :) #TheAutoQuote")
