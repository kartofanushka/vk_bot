import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'xml')

def cource():

    names = xml.find_all('Name')
    codes = xml.find_all('CharCode')
    codes=[code.text for code in codes]
    # print(codes[:50])
    values = xml.find_all('Value')
    nominals = xml.find_all('Nominal')
    return(codes)
        # dl=72
        # print('-'.center(dl, '-'))
        # print('|' + 'Name'.center(40) + '|' + ' Nominal'.center(9) + '|' + 'Value'.center(9) + '|' + 'CharCode |')
        # for i in range(0, len(names)):
        #     print('-'.center(dl, '-'))
        #     print(
        #         f'|{names[i].text.center(40)}|{nominals[i].text.center(9)}|{values[i].text.center(9)}|{codes[i].text.center(9)}|')
        # print('-'.center(dl, '-'))

# cource()
def get_course(currency):
    currency=currency.upper()
    try:
        if currency.startswith("R") and currency[1:].isdigit():
            return(xml.find("Valute", {'ID': currency}).Value.text)
        
        cur_to=float(xml.find("CharCode", text=currency).parent.Value.text.replace(',','.'))
        cur_nom=xml.find("CharCode", text=currency).parent.Nominal.text
        cur_name=xml.find("CharCode", text=currency).parent.Name.text
        return(f"{cur_to} руб. за {cur_nom} {cur_name}")
    except:
        usd=xml.find("Valute", {'ID': "R01235"}).Value.text
        return (f'Доллар США на сегодня {usd}.\nТого, что ты спросил не нашлось. \nКоманда "-k код валюты", например "-kusd". \nКоды можно выбрать из этого: {cource()} .\n Удачи') 

# print(get_course('ThB'))

# if __name__ == '__main__':
#     print(get_course("R01235"), "рублей за 1 доллар")
#     print(get_course("R01239"), "рублей за 1 евро")
#     print(get_course("R01375"), "рублей за 10 юаней")
    

