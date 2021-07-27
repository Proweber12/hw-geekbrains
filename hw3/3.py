class ExceptionOnlyNumber(Exception):
    pass


numbers = []

while True:
    try:
        num = input("Введите число: ")
        if num == "stop":
            print(numbers)
            break
        elif num.isdecimal():
            numbers.append(int(num))
        else:
            raise ExceptionOnlyNumber
    except ExceptionOnlyNumber:
        print('Нужно ввести число!')