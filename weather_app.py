import requests

city = input("Enter City Name: ")
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=46af4979c5a4b4c150a83ef5e6d48549'.format(city)

res = requests.get(url)
data = res.json()

temp = data ["main"] ["temp"]
humid = data ["main"] ["humidity"]
feels_like = data["main"] ["feels_like"]
temp_min = data["main"] ["temp_min"]
temp_max = data["main"] ["temp_max"]
degree = data["wind"] ["deg"]
speed = data ["wind"] ["speed"]
country = data["sys"] ["country"]
sunrise = data["sys"] ["sunrise"]
sunset = data["sys"] ["sunset"]
desc = data["weather"] [0] ["description"]

print ("Description : " + desc)
print ("Temprature : ",format(temp) )
print ("Minimum Temperature : ",format(temp_min) )
print ("Maximum Temprature : ",format(temp_max) )
print ("Feels like : ",format(feels_like) )
print ("Humidity : ",format(humid))
print ("Speed : ",format(speed))
print ("Degree : ",format(degree))
print ("Country : ",format(country))
print ("Sunrise : ",format(sunrise))
print ("Sunset : ",format(sunset))
