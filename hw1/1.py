def num_translate(translate):
    dict_translate = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                      "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if translate in dict_translate:
        print(dict_translate[translate])
    else:
        print(dict_translate.get('translate'))


num_translate("ten")
