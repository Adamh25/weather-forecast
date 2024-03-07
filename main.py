
import tkinter as tk
from weather import WeatherAPI
from forecast import ForecastAPI

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("400x300")

        self.weather_api = WeatherAPI()
        self.forecast_api = ForecastAPI()

        self.city_label = tk.Label(self, text="Enter city:")
        self.city_label.pack()

        self.city_entry = tk.Entry(self)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(self, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.weather_label = tk.Label(self, text="")
        self.weather_label.pack()

        self.get_forecast_button = tk.Button(self, text="Get Forecast", command=self.get_forecast)
        self.get_forecast_button.pack()

        self.forecast_label = tk.Label(self, text="")
        self.forecast_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        weather_data = self.weather_api.fetch_weather_data(city)
        if weather_data:
            temperature = weather_data['main']['temp']
            self.weather_label.config(text=f"Weather in {city}: {temperature}°C")

    def get_forecast(self):
        city = self.city_entry.get()
        forecast_data = self.forecast_api.fetch_forecast_data(city)
        if forecast_data:
            forecast_text = "Forecast for {}:\n".format(city)
            for forecast in forecast_data:
                forecast_text += f"Date: {forecast['date']}, Time: {forecast['time']}, " \
                                 f"Temperature: {forecast['temperature']}°C, " \
                                 f"Min Temp: {forecast['min_temperature']}°C, " \
                                 f"Max Temp: {forecast['max_temperature']}°C, " \
                                 f"Humidity: {forecast['humidity']}%, " \
                                 f"Weather: {forecast['weather_description']}\n"
            self.forecast_label.config(text=forecast_text)

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
