# -*- coding: cp1251 -*-
import telebot

TOKEN = '5341499463:AAEOJubGaKgro0R2NuSmPQZG1-HYciJqu48'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def booked(message):
    start_message = '������������, � ���������!'
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['booked'])
def booked(message):
    spb_first = 'https://ostrovok.ru/hotel/russia/st._petersburg/mid8094163/apartments_on_yegorova/?q=2042&dates=' \
                '12.06.2022-13.06.2022&guests=4&utm_source=mobile&utm_content=AB5FEE7C2939876273EB8EE9A8ADB5F0&' \
                'utm_medium=sharing&utm_campaign=hotelpage&sid=4faf46dc-1a36-43ea-8355-a2b5421bffa7'

    spb_main = 'https://sutochno.ru/front/searchapp/detail/1027985?utm_source=app&utm_campaign=android&utm_medium=' \
               'sharing&wp_processed=1&guests_adults=4&occupied=2022-06-13%3B2022-06-15&id=1&type=country&SW.' \
               'lat=55.142221&SW.lng=36.803259&NE.lat=56.021281&NE.lng=37.96779'

    karel = '�����: ���������� �������, ������������� �-�� �.�����, ������ �� ���������� 1-2 �� �� ����� �������.\n ' \
            '\n' \
            'GPS-���������� 61.520609, 30.331034.\n' \
            '\n' \
            '��������  �� 1 ��� � ���� �������\n' \
            '����� � 17.00\n' \
            '����� � 14.00\n' \
            '\n' \
            '�� ���� �������� ������� �� ������ +79216369300 ������\n' \
            '\n' \
            '��� ��������� ������ ����� � ������� 5000�\n' \
            '���������� ������� �� ���.�����.\n' \
            '\n' \
            'Wi-Fi: Keenetic-2574\n' \
            '������: xMwM2ohx\n'

    booked_info = f'������ ����� � ������: \n{spb_first},\n\n' \
                  f'�������� ����� � ������: \n{spb_main},\n\n' \
                  f'����� � �������: \n{karel}\n'
    bot.send_message(message.chat.id, booked_info)


@bot.message_handler()
def pizduk(message):
    if message.text == '������, ��� �?':
        pizduk_name = '�������� �����'
        bot.send_message(message.chat.id, f'�� - {pizduk_name}')
    else:
        pass


if __name__ == "__main__":
    bot.polling(non_stop=True)

    # spb_first = '�����-��������� ��.  �������, �. 25'
    # spb_main = '�����-���������, ��. ����������, 5'
    # karel = '���������� �������, �����������, ������� �����, 2'
