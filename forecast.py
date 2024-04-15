import requests

class ForecastAPI:
    def __init__(self):
        self.api_key = 'e6df251613c11107a906aa5ffa18e1ac'

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
                date_time = item['dt_txt']
                temperature = item['main']['temp']
                humidity = item['main']['humidity']
                pressure = item['main']['pressure']
                wind_speed = item['wind']['speed']
                wind_direction = self.get_wind_direction(item['wind']['deg'])
                parsed_forecast.append({
                    'date_time': date_time,
                    'temperature': temperature,
                    'humidity': humidity,
                    'pressure': pressure,
                    'wind_speed': wind_speed,
                    'wind_direction': wind_direction
                })
            return parsed_forecast
        else:
            return None

    def get_wind_direction(self, degrees):
        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        index = round(degrees / (360. / len(directions)))
        return directions[index % len(directions)]
