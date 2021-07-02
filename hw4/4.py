from itertools import zip_longest

with open('hobby.csv', 'r') as f:
    hobbys = (f.read().split('\n'))

with open('users.csv', 'r') as f:
    users = (f.read().split('\n'))

with open('users_hobby.txt', 'w') as f:
    for user, hobby in zip_longest(users, hobbys):
        if user == None:
            f.write('1')
            break
        f.write(f'{user} : {hobby}\n')