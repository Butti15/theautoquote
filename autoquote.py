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
	#replace(",",",\n").
	#replace(".","\n").
	replace("➖ @uQuotes ➖","\n\n") for i in List]

List=quote()
List.append("\n"+"")
abcd = " ".join(List)
#print (abcd)

#Removing Old Files //Step-2
#Removing Old Config Json Folder
path = r'/mnt/build2/butti/test/quote/config/theautoquote_uuid_and_cookie.json' #Path
#For PC :) path = r'config/theautoquotes_uuid_and_cookie.json' #Path

#Remove the Directory
try:
    os.remove(path)
    print("Directory of Config has been removed successfully")
except OSError as error:
    print(error)
    print("Directory of Config can not be removed")

#Removing the old Image
path2 = '/mnt/build2/butti/test/quote/quote.jpeg.REMOVE_ME'

try:
    os.remove(path2)
    print("Directory of Image has been removed successfully")
except OSError as error:
    print(error)
    print("Directory of Image can not be removed")

#New Path Remove
path33 = r'/mnt/build2/butti/config/theautoquote_uuid_and_cookie.json'
try:
    os.remove(path33)
except OSError as error:
    print("Cant be rmfed")
	
#Create Image object with the input image //Step-3
def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=60)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height

def main():
    #image_width
    image = Image.open(r'/mnt/build2/butti/test/quote/Backgrounds/testo.png')
    font_path = r'/mnt/build2/butti/test/quote/Font/calibrili.ttf'
    fontsize = 40  # starting font size
    font = ImageFont.truetype(font_path, fontsize)
    text1 = (abcd)
    #text2 = "You could use textwrap.wrap to break text into a list of strings, each at most width characters long"

    text_color = (0, 0, 0)
    text_start_height = 500
    draw_multiple_line_text(image, text1, font, text_color, text_start_height)
    #draw_multiple_line_text(image, text2, font, text_color, 400)
    image.save('/mnt/build2/butti/test/quote/quote.png')
    #image.show('quote.jpeg')

if __name__ == "__main__":
    main()

#Converting Files
im = Image.open("/mnt/build2/butti/test/quote/quote.png")
rgb_im = im.convert('RGB')
rgb_im.save('/mnt/build2/butti/test/quote/quote.jpg')

'''
#Sending to Instagram //Step-4
bot = Bot()
bot.login(username = "theautoquote",
		password = "Butti@1432")

bot.upload_photo('/mnt/build2/butti/test/quote/quote.jpg',
                caption ="#Quote of the day :) #TheAutoQuote")
'''
