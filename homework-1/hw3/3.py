# оканчивается на -а
list_a = [2, 3, 4]
# оканчивается на -ов
list_ov = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def procent(num):
    if num == 1:
        print("{} процент".format(num))

    for i in list_a:
        if num == i:
            print("{} процента".format(num))

    for x in list_ov:
        if num == x:
            print("{} процентов".format(num))

t = 1
while t < 21:
    procent(t)
    t = t + 1
