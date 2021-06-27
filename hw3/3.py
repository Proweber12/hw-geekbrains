from itertools import zip_longest

def generation():
    for tutor, klass in zip_longest(tutors, klasses, fillvalue=None):
        yield (tutor, klass)

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Евгений',
    'Михаил'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = generation()

print(type(gen))

for i in gen:
    print(i)