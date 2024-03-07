
import requests
from datetime import datetime

class ForecastAPI:
    def __init__(self):
        self.api_key = 'your_api_key'  

    def fetch_forecast_data(self, city):
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch forecast data.")
            return None

    def parse_forecast_data(self, forecast_data):
        if forecast_data:
            parsed_forecast = []
            for item in forecast_data['list']:
                timestamp = item['dt']
                date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
                time = datetime.utcfromtimestamp(timestamp).strftime('%H:%M:%S')
                temperature = item['main']['temp']
                min_temp = item['main']['temp_min']
                max_temp = item['main']['temp_max']
                humidity = item['main']['humidity']
                weather_desc = item['weather'][0]['description']
                parsed_forecast.append({
                    'date': date,
                    'time': time,
                    'temperature': temperature,
                    'min_temperature': min_temp,
                    'max_temperature': max_temp,
                    'humidity': humidity,
                    'weather_description': weather_desc
                })
            return parsed_forecast
        else:
            return None
