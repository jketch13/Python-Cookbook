import requests
import pandas as pd
import matplotlib.pyplot as plt

# Open-Meteo API endpoint
API_URL = "https://api.open-meteo.com/v1/forecast"

# Function to fetch weather data
def fetch_weather_data(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }
    response = requests.get(API_URL, params=params)
    return response.json()

# Function to process weather data
def process_weather_data(data):
    hourly_data = data['hourly']
    df = pd.DataFrame(hourly_data)
    df['time'] = pd.to_datetime(df['time'])
    return df

# Function to plot weather data
def plot_weather_data(df):
    plt.figure(figsize=(15, 8))
    plt.plot(df['time'], df['temperature_2m'], label='Temperature (°C)')
    plt.plot(df['time'], df['relative_humidity_2m'], label='Humidity (%)')
    plt.plot(df['time'], df['wind_speed_10m'], label='Wind Speed (m/s)')
    plt.title('Weather Data')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    latitude = 52.52  # Replace with your desired latitude
    longitude = 13.41  # Replace with your desired longitude
    weather_data = fetch_weather_data(latitude, longitude)
    processed_data = process_weather_data(weather_data)
    plot_weather_data(processed_data)
