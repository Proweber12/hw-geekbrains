import re
import datetime

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def split_date(cls, date):
        SPLIT_DATE = re.split(r'[-/.]', date)
        print(f'Число - {SPLIT_DATE[0]}\nМесяц - {SPLIT_DATE[1]}\nГод - {SPLIT_DATE[2]}')

    @staticmethod
    def validation_date(date):
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print("Неверный формат даты")
        else:
            print(date)

Date.split_date('26-07-2021')
Date.validation_date('24-05-2021')