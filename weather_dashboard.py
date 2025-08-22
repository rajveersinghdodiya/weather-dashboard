import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------- CONFIGURATION --------
API_KEY =  "YOUR_API_KEY_HERE"

CITY = "Ujjain"          
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -------- FETCHING DATA --------
response = requests.get(URL)
if response.status_code != 200:
    print("❌ Error fetching data! Check your API Key or City name.")
    exit()

data = response.json()

# Extract forecast list
forecast_list = data['list']

# Data ko DataFrame me convert karna
weather_data = {
    "datetime": [],
    "temperature": [],
    "humidity": [],
    "pressure": [],
}

for entry in forecast_list:
    weather_data["datetime"].append(entry["dt_txt"])
    weather_data["temperature"].append(entry["main"]["temp"])
    weather_data["humidity"].append(entry["main"]["humidity"])
    weather_data["pressure"].append(entry["main"]["pressure"])

df = pd.DataFrame(weather_data)

# -------- VISUALIZATION --------
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="datetime", y="temperature", marker="o", color="orange")
plt.xticks(rotation=45)
plt.title(f"🌡 Temperature Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="datetime", y="humidity", color="skyblue")
plt.xticks(rotation=45)
plt.title(f"💧 Humidity Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="datetime", y="pressure", marker="o", color="red")
plt.xticks(rotation=45)
plt.title(f"📊 Pressure Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Pressure (hPa)")
plt.tight_layout()
plt.show()

print("✅ Dashboard generated successfully!")

