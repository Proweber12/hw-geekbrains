import sys
from requests import get
from bs4 import BeautifulSoup


def currency_rates(rate):
    for i in range(len(currency)):
        if rate.lower() == currency[i].text.lower():
            value_currency = round(float(value_currencies[i].text.replace(",", ".")), 2)
            return (f'{currency[i].text} {nominal_value[i].text} {name_currency[i].text} стоит {value_currency} руб. Дата:{date[0].replace(".", "-")}')


response = get('http://www.cbr.ru/scripts/XML_daily.asp')

my_parser = BeautifulSoup(response.content, 'html.parser')

date = [valcurs['date'] for valcurs in my_parser.findAll('valcurs', date = True)]
currency = my_parser.findAll("charcode")
nominal_value = my_parser.findAll("nominal")
name_currency = my_parser.findAll("name")
value_currencies = my_parser.findAll("value")

print(currency_rates(sys.argv[1]))