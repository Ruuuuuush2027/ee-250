import requests
import sys

# WeatherAPI key

def get_joke():
    base_url = "https://official-joke-api.appspot.com/random_joke"
    params = {}
    
    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            result = response.json()
            print('Joke id:', result['id'])
            print('Type of joke:', result['type'])
            print('Set up:', result['setup'])
            print('Punchline:', result['punchline'])
        elif response.status_code == 400:
            print(f"Error: {response.status_code}. Bad Request.")
        elif response.status_code == 404:
            print(f"Error: {response.status_code}. Not Found.")
        else:
            print(f"Error: {response.status_code}. Something went wrong.")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")

if __name__ == '__main__':
    while True:
        try:
            get = input('get a joke (y/n)? ')
            if get == 'y':
                get_joke()
            elif get == 'n':
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print("Please only input 'y' or 'n'!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)