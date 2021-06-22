def num_translate_adv(translate):
    dict_translate = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                      "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять",
                      "One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть",
                      "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}
    if translate in dict_translate:
        print(dict_translate[translate])
    else:
        print(dict_translate.get('translate'))


num_translate_adv("Ten")
