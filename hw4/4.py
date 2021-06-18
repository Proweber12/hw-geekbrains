list_description = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in list_description:
    list_name = i.split(' ')
    value = f'Привет, {list_name[-1].capitalize()}'
    print(value)