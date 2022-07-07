import requests
from bs4 import BeautifulSoup

def weather_short():
    url = "https://www.meteoprog.ua/ru/weather/Kyiv/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html")
    temp = bs.findAll("div", class_="times-of-day")
    find_bs = temp[0]
    numbers = find_bs.findAll("strong")
    i = 0
    while i < 4:
        numbers[i] = numbers[i].text
        i += 1
    return numbers

def weather_detal(day, city):
    if city == "":
        city = "Kyiv"
    url = "https://www.meteoprog.ua/ru/meteograms/"+str(city)+"/"
    print(url)
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html")
    temp = bs.findAll("div", class_="weather-details-hourly__item")
    temp = temp[day]
    time_column = temp.findAll("div", class_="time__column")
    temperature_column_span = temp.findAll("div", class_="temperature__column")
    temperature_column = temp.findAll("div", class_="temperature__column")
    i = 0
    dicta = {}
    while i < len(temperature_column_span):
        temperature_column_span[i] = temperature_column_span[i].find("span")
        time_column[i] = time_column[i].find("span")
        temperature_column_span[i] = temperature_column_span[i].text
        time_column[i] = time_column[i].text
        a = temperature_column[i].find("div", class_="icon")
        gett = a.get("title")
        dicta[time_column[i]] = temperature_column_span[i], gett
        i += 1
    return dicta
