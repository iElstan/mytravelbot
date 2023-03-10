import telebot
import random
import os
import data
import requests
from bs4 import BeautifulSoup


if data.DEBUG:
    import secretconfig #нужно для отладки оффлайн
    bot = telebot.TeleBot(secretconfig.TOKEN)
else:
    bot = telebot.TeleBot(os.environ.get('TOKEN'))

html_text = requests.get(data.url)

# Function to receive a list of phrases to answer "who_am_i" question
def get_phrase_list():
    phrase_list = []
    soup = BeautifulSoup(html_text.text, 'html.parser')
    tags = soup.find_all("span")
    for tag in tags:
        text = tag.get_text()
        phrase_list.append(text)
    return phrase_list

@bot.message_handler(commands=['start'])
def start(message):
    start_message = data.start_message
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['info'])
def info(message):
    info = data.current_info
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['wifi'])
def wifi(message):
    wifi_list = data.wifi_list
    bot.send_message(message.chat.id, wifi_list)


@bot.message_handler()
def who_am_i_sanya(message):
    if message.text == (data.message_text):
        whoami_name = get_phrase_list()[random.randint(0, len(get_phrase_list()) - 1)]
        bot.send_message(message.chat.id, f'Ты - {whoami_name}')


if __name__ == "__main__":
    bot.polling(non_stop=True)