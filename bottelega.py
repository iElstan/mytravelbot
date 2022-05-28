import telebot
import random
import os
import data
# import config #нужно для отладки оффлайн

# bot = telebot.TeleBot(config.TOKEN)
bot = telebot.TeleBot(os.environ.get('TOKEN'))


@bot.message_handler(commands=['start'])
def booked(message):
    start_message = 'Здравствуйте, я Александр!'
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['booked'])
def booked(message):
    spb_first = 'https://ostrovok.ru/hotel/russia/st._petersburg/mid8094163/apartments_on_yegorova/?q=2042&dates=' \
                '12.06.2022-13.06.2022&guests=4&utm_source=mobile&utm_content=AB5FEE7C2939876273EB8EE9A8ADB5F0&' \
                'utm_medium=sharing&utm_campaign=hotelpage&sid=4faf46dc-1a36-43ea-8355-a2b5421bffa7'

    spb_main = 'Адрес: Санкт-Петербург, ул. Жуковского 5.\n ' \
               '\n' \
               'Заезд 13 июня в 15.00\n' \
                'Выезд 15 июня в 12.00\n' \
                '\n' \
                'Телефон +7 910 762-82-81 \n' \
               'Телефон +7 921 964-86-15 \n' \
               'Оплата при заселении 11730р\n'

    karel = 'Адрес: Республика Карелия, Лахденпохский р-он п.Микли, дальше по указателям 1-2 км до хутор Медовое.\n ' \
            '\n' \
            'GPS-координаты 61.520609, 30.331034.\n' \
            '\n' \
            'Сообщить  за 1 час о своём приезде\n' \
            'Заезд в 17.00\n' \
            'Выезд в 14.00\n' \
            '\n' \
            'По всем вопросам звонить по номеру +79216369300 Оксана\n' \
            '\n' \
            'При заселении берётся залог в размере 5000р\n' \
            'Проживание питомца за доп.плату.\n' \
            '\n' \
            'Wi-Fi: Keenetic-2574\n' \
            'Пароль: xMwM2ohx\n'

    booked_info = f'Первая бронь в Питере: \n{spb_first},\n\n' \
                  f'Основная бронь в Питере: \n{spb_main},\n\n' \
                  f'Бронь в Карелии: \n{karel}\n'
    bot.send_message(message.chat.id, booked_info)


@bot.message_handler(['wifi'])
def wifi(message):
    wifi_list = 'Карелия:\n' \
                'Wi-Fi: Keenetic-2574\n' \
                'Пароль: xMwM2ohx\n'
    bot.send_message(message.chat.id, wifi_list)


@bot.message_handler()
def who_am_i_sanya(message):
    # whoami_question = input()
    if message.text == ('Сантей кто я'):
        whoami_name = data.get_phrase_list()[random.randint(0, len(data.get_phrase_list()) - 1)]
        bot.send_message(message.chat.id, f'Ты - {whoami_name}')
    else:
        pass


if __name__ == "__main__":
    bot.polling(non_stop=True)
