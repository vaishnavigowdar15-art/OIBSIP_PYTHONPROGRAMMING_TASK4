import tkinter as tk
import urllib.request
import json

API_KEY = "bd75792caa9b8949fbd39524fe8d0cc4"

def get_weather():
    city = entry.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]

            result = "City: " + city + "\nTemperature: " + str(temp) + "°C\nWeather: " + weather
        else:
            result = "City not found"

    except:
        result = "Error fetching data"

    label.config(text=result)


# Window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

# Title
tk.Label(root, text="Weather App").pack()

# Input
entry = tk.Entry(root)
entry.pack()

# Button
tk.Button(root, text="Get Weather", command=get_weather).pack()

# Result
label = tk.Label(root, text="")
label.pack()

root.mainloop()
