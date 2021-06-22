from random import choice


def get_jokes(jokes_volume):
    i = 1
    """Создаем список, в котором будут содержатся сгенерированные шутки"""
    jokes = []
    while i <= jokes_volume:
        """Создаем переменную в которой через форматирование строк создаются шутки"""
        joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        """Добавляем шутки в список"""
        jokes.append(joke)
        i = i + 1
    """Выводим полученные шутки"""
    print(jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(50)
