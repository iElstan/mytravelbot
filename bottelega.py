import telebot
import random
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def booked(message):
    start_message = 'Здравствуйте, я Александр!'
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['booked'])
def booked(message):
    spb_first = 'https://ostrovok.ru/hotel/russia/st._petersburg/mid8094163/apartments_on_yegorova/?q=2042&dates=' \
                '12.06.2022-13.06.2022&guests=4&utm_source=mobile&utm_content=AB5FEE7C2939876273EB8EE9A8ADB5F0&' \
                'utm_medium=sharing&utm_campaign=hotelpage&sid=4faf46dc-1a36-43ea-8355-a2b5421bffa7'

    spb_main = 'https://sutochno.ru/front/searchapp/detail/1027985?utm_source=app&utm_campaign=android&utm_medium=' \
               'sharing&wp_processed=1&guests_adults=4&occupied=2022-06-13%3B2022-06-15&id=1&type=country&SW.' \
               'lat=55.142221&SW.lng=36.803259&NE.lat=56.021281&NE.lng=37.96779'

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
def pizduk(message):
    pizduk_list = ['убрано цензурой', 'Вася']
    if message.text == 'Пиздюк, кто я?':
        pizduk_name = pizduk_list[random.randint(0, len(pizduk_list))]
        bot.send_message(message.chat.id, f'Вы - {pizduk_name}')
    else:
        pass


if __name__ == "__main__":
    bot.polling(non_stop=True)
