import json

import requests

time_zone = "GMT"
latitude = 11.000218
longitude = 75.979162

result = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily'
                      f'=weathercode,temperature_2m_max,temperature_2m_min&timezone={time_zone.upper()}')
weather = result.json()

weather_code = weather['daily']['weathercode'][0]
min_weather = weather['daily']['temperature_2m_min'][0]
max_weather = weather['daily']['temperature_2m_max'][0]


def get_code(code):
    if code == 0:
        return "Clear Sky"
    elif code == 1 or code == 2 or code == 3:
        return "Mainly clear, partly cloudy, and overcast"
    elif code == 45 or code == 48:
        return "Fog and depositing rime fog"
    elif code == 51 or code == 53 or code == 55:
        return "Drizzle: Light, moderate, and dense intensity"
    elif code == 56 or code == 57:
        return "Freezing Drizzle: Light and dense intensity"
    elif code == 61 or code == 63 or code == 65:
        return "Rain: Slight, moderate and heavy intensity"
    elif code == 66 or code == 67:
        return "Freezing Rain: Light and heavy intensity"
    elif code == 71 or code == 73 or code == 75:
        return "Snow fall: Slight, moderate, and heavy intensity"
    elif code == 77:
        return "Snow grains"
    elif code == 80 or code == 81 or code == 82:
        return "Rain showers: Slight, moderate, and violent"
    elif code == 85 or code == 86:
        return "Snow showers slight and heavy"
    elif code == 95:
        return "Thunderstorm: Slight or moderate"
    elif code == 96 or  code == 98:
        return "Thunderstorm with slight and heavy hail"


print(f'{get_code(weather_code)}\n🥵: {max_weather}\t🥶: {min_weather}')
