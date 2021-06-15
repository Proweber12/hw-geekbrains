duration = int(input("Введите продолжительность времени в секундах: "))
seconds = duration % 60
minutes = duration // 60
minutes_remains = minutes % 60
hours = minutes // 60
hours_remains = hours % 24
days = hours // 24
days_remains = days % 30
months = days // 30
months_remains = months % 12
years = months // 12

# секунды
if duration <= 60:
    print("{} сек".format(duration))
# минуты
elif duration > 60 and duration <= 3600:
    print("{} мин {} сек".format(minutes, seconds))
# часы
elif duration > 3600 and duration <= 86400:
    print("{} час {} мин {} сек".format(hours, minutes_remains, seconds))
# дни
elif duration > 86400 and duration <= 2592000:
    print("{} дн {} час {} мин {} сек".format(days, hours_remains, minutes_remains, seconds))
# месяца
elif duration > 2592000 and duration <= 31104000:
    print("{} мес {} дн {} час {} мин {} сек".format(months, days_remains, hours_remains, minutes_remains, seconds))
# года
elif duration > 31104000:
    print("{} лет {} мес {} дн {} час {} мин {} сек".format(years, months_remains, days_remains, hours_remains, minutes_remains, seconds))