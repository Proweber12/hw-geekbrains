weather_forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in weather_forecast:
    if i.isdigit() == True:
        new_value = f'"{int(i):02d}"'
        weather_forecast[weather_forecast.index(str(i))] = new_value
    elif i.isalpha() == False:
        new_value = f'"+{int(i):02d}"'
        weather_forecast[weather_forecast.index(str(i))] = new_value

weather_forecast_str = ' '.join(weather_forecast)
print(weather_forecast_str)
