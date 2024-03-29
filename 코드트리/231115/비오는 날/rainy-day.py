n = int(input())
arr = [list(input().split()) for _ in range(n)]

forecast = []
for i in range(len(arr)):
    if arr[i][-1] == "Rain":
        forecast.append(arr[i])

forecast.sort()
yymmdd, day, weather = forecast[0]
print(yymmdd, day, weather)