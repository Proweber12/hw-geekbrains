from itertools import zip_longest

with open('hobby.csv', 'r') as f:
    hobbys = (f.read().split('\n'))

with open('users.csv', 'r') as f:
    users = (f.read().split('\n'))

users_hobbys = {}

for user, hobby in zip_longest(users, hobbys):
    if user == None:
        print(1)
        break
    users_hobbys[user] = hobby

print(users_hobbys)