import tkinter as tk
import requests
from tkinter import messagebox

# Function to get weather data from OpenWeatherMap API
def get_weather():
    api_key = "8a52e1c95657c427fe7d7c834cecba52"  # Replace with your own API key
    city = city_entry.get()
    
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    # Build the URL to request weather data
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        weather_data = response.json()
        
        if weather_data["cod"] != "404":
            # Extract relevant data
            city_name = weather_data["name"]
            temperature = weather_data["main"]["temp"]
            weather_desc = weather_data["weather"][0]["description"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            # Update the labels with the weather data
            result_label.config(text=f"City: {city_name}\nTemperature: {temperature}°C\nWeather: {weather_desc.title()}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found. Please enter a valid city name.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve data. Check your internet connection or try again later.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Label for the app title
title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Entry widget for city input
city_entry = tk.Entry(root, width=20, font=("Arial", 14))
city_entry.pack(pady=10)

# Button to get weather data
get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather)
get_weather_button.pack(pady=5)

# Label to display the weather information
result_label = tk.Label(root, text="Enter a city and press 'Get Weather'.", font=("Arial", 14), justify="left")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
