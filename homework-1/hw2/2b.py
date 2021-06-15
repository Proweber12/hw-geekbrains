list_first = []
list_copy = []
new_list = []

for i in range(1, 1001):
    if i % 2 != 0:
        list_first.append(i ** 3 + 17)
        list_copy.append(i ** 3 + 17)

for n in range(len(list_first)):
    sum_digits = 0
    while list_first[n] != 0:
        sum_digits = sum_digits + list_first[n] % 10
        list_first[n] = list_first[n] // 10
    if sum_digits % 7 != 0:
        new_list.append(n)

for r in sorted(new_list, reverse=True):
    del list_copy[r]

result = 0

for t in range(len(list_copy)):
    result = result + list_copy[t]

print(result)