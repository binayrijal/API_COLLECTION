import requests

api_key='100bafaea7e45eab26bb2780f763dd0b'
try:
 user_input=input("enter city: ")

 weather_data=requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
 weather=weather_data.json()['weather'][0]['main']
 temp=weather_data.json()['main']['temp']
 print(f"The weather of {user_input} is {weather}")
 print(f"The temperature of {user_input} is {temp}F")
except:
  print("the given city is not exist")

finally:
  print("this much")

