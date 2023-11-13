import requests

def weather(city):
    api_key = '2aaa723a5716caa180e3e3e3068995b3'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print(f"Failed to retrieve weather information. Status code: {response.status_code}")


city_input = input("Enter the Name of Any City :  ")
weather(city_input)
