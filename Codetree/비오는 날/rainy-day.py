# n = int(input())
# arr = [list(input().split()) for _ in range(n)]
#
# forecast = []
# for i in range(len(arr)):
#     if arr[i][-1] == "Rain":
#         forecast.append(arr[i])
#
# forecast.sort()
# yymmdd, day, weather = forecast[0]
# print(yymmdd, day, weather)

#-------------------------------

class Forecast:
    def __init__(self, yymmdd, day, weather):
        self.yymmdd = yymmdd
        self.day = day
        self.weather = weather

n = int(input())

forecasts = []
rainy_day = []

for _ in range(n):
    yymmdd, day, weather = tuple(input().split())
    forecasts.append(Forecast(yymmdd, day, weather))

for forecast in forecasts:
    if forecast.weather =="Rain":
        rainy_day.append(forecast)

rainy_day.sort(key = lambda x: x.yymmdd)

print(rainy_day[0].yymmdd, rainy_day[0].day, rainy_day[0].weather)