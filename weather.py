import requests

class WeatherAPI:
    def __init__(self):
        self.api_key = 'e6df251613c11107a906aa5ffa18e1ac'

    def fetch_weather_data(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch weather data.")
            return None
