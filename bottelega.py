import telebot
import random
import os
import data
import requests
from bs4 import BeautifulSoup as bs

# import config #нужно для отладки оффлайн

# bot = telebot.TeleBot(config.TOKEN)
bot = telebot.TeleBot(os.environ.get('TOKEN'))

url = data.url
html_text = requests.get(url)

# Function to receive a list of phrases to answer "who_am_i" question
def get_phrase_list():
    phrase_list = []
    soup = bs(html_text.text, 'html.parser')
    tags = soup.find_all("span")
    for tag in tags:
        text = tag.get_text()
        phrase_list.append(text)
    return phrase_list

@bot.message_handler(commands=['start'])
def booked(message):
    start_message = data.start_message
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['booked'])
def booked(message):
    spb_first = data.spb_first

    booked_info = f'Первая бронь в Питере: \n{spb_first},\n\n' \

    bot.send_message(message.chat.id, booked_info)


@bot.message_handler(['wifi'])
def wifi(message):
    wifi_list = data.wifi_list
    bot.send_message(message.chat.id, wifi_list)


@bot.message_handler()
def who_am_i_sanya(message):
    if message.text == (data.message_text):
        whoami_name = get_phrase_list()[random.randint(0, len(get_phrase_list()) - 1)]
        bot.send_message(message.chat.id, f'Ты - {whoami_name}')
    else:
        pass


if __name__ == "__main__":
    bot.polling(non_stop=True)
