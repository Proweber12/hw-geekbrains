def thesaurus(*args):
    dict_name = {}
    for name in args:
        key = name[0].capitalize()
        if key not in dict_name:
            dict_name[key] = []
        dict_name[key].append(name)
    print(dict_name)

thesaurus("Иван", "Мария", "Петр", "Илья")