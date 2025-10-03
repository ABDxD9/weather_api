import requests

API_KEY = "5c2edbb2f30e3e603685850085cb0b3e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    print(response.status_code, response.text)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        print(f"\nWeather in {city}:")
        print(f"Description: {weather}")
        print(f"Temperature:🌡 {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Error fetching weather data. Please check the city name or API key.")


print("=== Welcome to the Weather App! ===")
while True:
    city = input("Enter a city name (or 'exit' to quit): ").strip()
    if city.lower() == 'exit':
        print("Exiting the Weather App. Goodbye!")
        break
    get_weather(city)   