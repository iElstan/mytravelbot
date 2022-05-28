import requests
from bs4 import BeautifulSoup as bs

url = 'http://dict.ruslang.ru/magn.php?act=search&orderby=context&magn_lex=&context_lex=&magn_ps=&context_ps=' \
      '%F1%F3%F9%E5%F1%F2%E2%E8%F2%E5%EB%FC%ED%EE%E5&magn_sem='
html_text = requests.get(url)


def get_phrase_list():
    phrase_list = []
    soup = bs(html_text.text, 'html.parser')
    tags = soup.find_all("span")
    for tag in tags:
        text = tag.get_text()
        phrase_list.append(text)
    return phrase_list


if __name__ == '__main__':
    get_phrase_list()
