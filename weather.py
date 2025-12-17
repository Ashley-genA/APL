import requests
import sys
import json 

API_KEY = "5222eeb8f7e1d1cbd9d0184e197c3d05" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetches and displays the current weather for a given city.
    """
    if API_KEY == "YOUR_API_KEY":
        print("🚨 ERROR: Please replace 'YOUR_API_KEY' in the script with your actual OpenWeatherMap API key.")
        return

    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric' 
    }

    try:
        
        response = requests.get(BASE_URL, params=params)
        
      
        response.raise_for_status() 
        
       
        data = response.json()

        
        if data["cod"] == "404":
            print(f" Error: City '{city_name}' not found.")
            return

        
        main_data = data['main']
        weather_data = data['weather'][0]
        
      
        temp_celsius = round(main_data['temp'], 1) 
        humidity = main_data['humidity']
        description = weather_data['description'].capitalize()
        city_display = data['name']
        country = data['sys']['country']
        wind_speed = round(data['wind']['speed'], 1) # Wind speed in m/s

        
        print(f"\n--- Weather Report for {city_display}, {country} ---")
        print(f" Temperature: {temp_celsius}°C**")
        print(f" Condition: *{description}*")
        print(f" Humidity: *{humidity}%*")
        print(f" Wind Speed: *{wind_speed} m/s*")
        print("-------------------------------------------\n")

    except requests.exceptions.RequestException as e:
        
        print(f"An error occurred during the API request: {e}")
    except KeyError:
        
        print("An error occurred: Could not parse weather data correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Handles command line arguments.
    """

    if len(sys.argv) < 2:
        print("Usage: python weather_cli.py <city_name>")
        print("Example: python weather_cli.py 'New York'")
        print("Note: Use quotes for city names with spaces.")
        sys.exit(1)

    
    city = " ".join(sys.argv[1:]) 
    get_weather(city)

if __name__ == "__main__":
    main()