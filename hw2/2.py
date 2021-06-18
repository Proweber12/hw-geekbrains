weather_forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in weather_forecast:
    if i.isdigit() == True:
        weather_forecast.insert(weather_forecast.index(i)+1, "")
    elif i.isalpha() == False:
        weather_forecast.insert(weather_forecast.index(i)+1, "")
    print(weather_forecast)

weather_forecast_str = ' '.join(weather_forecast)
print(weather_forecast_str)
