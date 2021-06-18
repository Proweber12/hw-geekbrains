prices = [43.2, 53.1, 75.15, 96.53, 95, 1134.93, 559.6, 452.25, 41.61, 45, 531.51, 656.36]
prices_new = prices.copy()
prices_new.sort(reverse=True)
print(prices)
print(prices_new)

for i in prices:
    prices = str(i).split('.')
    if len(prices) > 1:
        prices[0] = f'{int(prices[0])} руб'
        prices[1] = f'{int(prices[1]):02d} коп'
    else:
        prices[0] = f'{int(prices[0])} руб'
    value = ' '.join(prices)
    print(value, end=', ')

print()

for i in prices_new:
    prices_new = str(i).split('.')
    if len(prices_new) > 1:
        prices_new[0] = f'{int(prices_new[0])} руб'
        prices_new[1] = f'{int(prices_new[1]):02d} коп'
    else:
        prices_new[0] = f'{int(prices_new[0])} руб'
    value = ' '.join(prices_new)
    print(value, end=', ')