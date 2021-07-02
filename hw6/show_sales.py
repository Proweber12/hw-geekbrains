import sys


def show_sales_from_before(num1, num2):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        line = f.readlines()
        while int(num1) < int(num2) + 1:
            print(line[int(num1) - 1], end="")
            num1 = int(num1) + 1


def show_sales_from_end(number):
    # чтоб от заданного начала до конца
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        line = f.readlines()
        while number < len(max(line)) + 1:
            print(line[int(number) - 1], end="")
            number = int(number) + 1


def show_sales_all():
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())



