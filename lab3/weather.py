import requests
import sys

# WeatherAPI key
WEATHER_API_KEY = 'c225f7ef90e1488ebe203411260602'

def get_weather(city):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': WEATHER_API_KEY,
        'q': city
    }
    
    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            current = data['current']
            location = data['location']
            
            print(f"\nWeather data for {location['name']}, {location['country']}...")
            print(f"Temperature: {current['temp_f']}°F (Feels like: {current['feelslike_f']}°F)")
            print(f"Condition: {current['condition']['text']}")
            print(f"Humidity: {current['humidity']}%")
            print(f"Wind: {current['wind_mph']} mph {current['wind_dir']}")
            print(f"Pressure: {current['pressure_mb']} mb")
            print(f"UV Index: {current['uv']}")
            print(f"Cloud Cover: {current['cloud']}%")
            print(f"Visibility: {current['vis_miles']} miles")
            
        elif response.status_code == 400:
            print(f"Error: {response.status_code}. Bad Request. Please check the city name.")
        elif response.status_code == 401:
            print(f"Error: {response.status_code}. Unauthorized. Invalid API Key.")
        elif response.status_code == 404:
            print(f"Error: {response.status_code}. Not Found.")
        else:
            print(f"Error: {response.status_code}. Something went wrong.")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")

if __name__ == '__main__':
    print("Weather App (Type 'quit' or 'exit' to stop)")
    while True:
        try:
            city_input = input("\nEnter city name: ").strip()
            if city_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            
            if not city_input:
                continue
                
            get_weather(city_input)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)