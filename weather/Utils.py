from datetime import datetime
import requests
import datetime

APIkey1 = '3ca2a253a882ec9e7b479e623f4a842f'
APIkey2 = '28862a7de012e2fc9df168ad47a855ec'

city_cood = { "London":[51.50,-0.11],
              "Toronto":[43.65,-79.34],
              "NewYork":[40.73,-73.93],
              "Colombo":[6.92,79.86],
              "Paris":[48.86,2.34],
              "Mumbai":[19.07,72.87],
              "Singapore":[1.29,103.85],
              "Melbourne":[-37.84,144.94],
              "Tokyo":[35.65,139.83],
            }



def extract_forecast_temp(data_forecast):
    row = []
    for i in data_forecast:
        dt = datetime.datetime.utcfromtimestamp(int(i["dt"])).strftime('%Y-%m-%d %H:%M:%S')
        t = ("Hour",dt,i["temp"])
        row.append(t)
    return row

def extract_forecast_humty(data_forecast):
    row = []
    for i in data_forecast:
        dt = datetime.datetime.utcfromtimestamp(int(i["dt"])).strftime('%Y-%m-%d %H:%M:%S')
        t = ("Humidity",dt,i["humidity"])
        row.append(t)
    return row

def extract_forecast_wind_spd(data_forecast):
    row = []
    for i in data_forecast:
        dt = datetime.datetime.utcfromtimestamp(int(i["dt"])).strftime('%Y-%m-%d %H:%M:%S')
        t = ("Wind Speed",dt,i["wind_speed"]*3.6)
        row.append(t)
    return row

def get_Data_forecast(city):
    lat,lon = city_cood[city][0],city_cood[city][1]
    r2 = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' + str(lat) + '&lon=' + str(lon) + '&exclude=daily,minutely&appid=3ca2a253a882ec9e7b479e623f4a842f')
    r_dictionary= r2.json()
    if(len(r_dictionary.keys()) > 3):return r_dictionary
    else :
        r_dictionary = {
    "lat": 33.44,
    "lon": -94.04,
    "timezone": "America/Chicago",
    "timezone_offset": -18000,
    "current": {
        "dt": 1636020549,
        "sunrise": 1636029466,
        "sunset": 1636068100,
        "temp": 277.87,
        "feels_like": 276.13,
        "pressure": 1026,
        "humidity": 90,
        "dew_point": 276.37,
        "uvi": 0,
        "clouds": 90,
        "visibility": 10000,
        "wind_speed": 2.06,
        "wind_deg": 30,
        "weather": [
            {
                "id": 804,
                "main": "Clouds",
                "description": "overcast clouds",
                "icon": "04n"
            }
        ]
    },
    "hourly": [
        {
            "dt": 1636020000,
            "temp": 277.87,
            "feels_like": 275.83,
            "pressure": 1026,
            "humidity": 90,
            "dew_point": 276.37,
            "uvi": 0,
            "clouds": 90,
            "visibility": 10000,
            "wind_speed": 2.37,
            "wind_deg": 28,
            "wind_gust": 5.92,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636023600,
            "temp": 277.89,
            "feels_like": 275.48,
            "pressure": 1026,
            "humidity": 87,
            "dew_point": 275.91,
            "uvi": 0,
            "clouds": 89,
            "visibility": 10000,
            "wind_speed": 2.82,
            "wind_deg": 32,
            "wind_gust": 6.91,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636027200,
            "temp": 277.47,
            "feels_like": 274.92,
            "pressure": 1026,
            "humidity": 86,
            "dew_point": 275.34,
            "uvi": 0,
            "clouds": 83,
            "visibility": 10000,
            "wind_speed": 2.89,
            "wind_deg": 35,
            "wind_gust": 6.87,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636030800,
            "temp": 277.13,
            "feels_like": 274.83,
            "pressure": 1027,
            "humidity": 83,
            "dew_point": 274.51,
            "uvi": 0,
            "clouds": 37,
            "visibility": 10000,
            "wind_speed": 2.51,
            "wind_deg": 42,
            "wind_gust": 6.92,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636034400,
            "temp": 278.77,
            "feels_like": 276.41,
            "pressure": 1028,
            "humidity": 71,
            "dew_point": 273.93,
            "uvi": 0.28,
            "clouds": 19,
            "visibility": 10000,
            "wind_speed": 2.98,
            "wind_deg": 55,
            "wind_gust": 6.56,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636038000,
            "temp": 281.32,
            "feels_like": 279.23,
            "pressure": 1028,
            "humidity": 53,
            "dew_point": 272.5,
            "uvi": 0.98,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.38,
            "wind_deg": 58,
            "wind_gust": 5.53,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636041600,
            "temp": 283.38,
            "feels_like": 281.61,
            "pressure": 1028,
            "humidity": 44,
            "dew_point": 271.8,
            "uvi": 1.99,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.61,
            "wind_deg": 54,
            "wind_gust": 5.07,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636045200,
            "temp": 285.03,
            "feels_like": 283.29,
            "pressure": 1027,
            "humidity": 39,
            "dew_point": 271.78,
            "uvi": 3.03,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.59,
            "wind_deg": 49,
            "wind_gust": 4.58,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636048800,
            "temp": 286.32,
            "feels_like": 284.66,
            "pressure": 1026,
            "humidity": 37,
            "dew_point": 272.09,
            "uvi": 3.59,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.42,
            "wind_deg": 45,
            "wind_gust": 4.12,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636052400,
            "temp": 287.18,
            "feels_like": 285.58,
            "pressure": 1025,
            "humidity": 36,
            "dew_point": 272.46,
            "uvi": 3.6,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.28,
            "wind_deg": 42,
            "wind_gust": 3.83,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636056000,
            "temp": 287.61,
            "feels_like": 286.05,
            "pressure": 1024,
            "humidity": 36,
            "dew_point": 272.8,
            "uvi": 2.76,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 3.02,
            "wind_deg": 45,
            "wind_gust": 3.51,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636059600,
            "temp": 287.63,
            "feels_like": 286.1,
            "pressure": 1023,
            "humidity": 37,
            "dew_point": 273.04,
            "uvi": 1.63,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.81,
            "wind_deg": 48,
            "wind_gust": 3.34,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636063200,
            "temp": 287.1,
            "feels_like": 285.57,
            "pressure": 1023,
            "humidity": 39,
            "dew_point": 273.59,
            "uvi": 0.67,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.79,
            "wind_deg": 52,
            "wind_gust": 3.4,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636066800,
            "temp": 284.36,
            "feels_like": 282.87,
            "pressure": 1023,
            "humidity": 51,
            "dew_point": 274.62,
            "uvi": 0.14,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.33,
            "wind_deg": 58,
            "wind_gust": 2.59,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636070400,
            "temp": 282.19,
            "feels_like": 280.95,
            "pressure": 1023,
            "humidity": 56,
            "dew_point": 273.87,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.35,
            "wind_deg": 65,
            "wind_gust": 2.49,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636074000,
            "temp": 281.34,
            "feels_like": 279.86,
            "pressure": 1024,
            "humidity": 59,
            "dew_point": 273.79,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.46,
            "wind_deg": 80,
            "wind_gust": 2.55,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636077600,
            "temp": 280.57,
            "feels_like": 278.9,
            "pressure": 1024,
            "humidity": 62,
            "dew_point": 273.82,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.52,
            "wind_deg": 87,
            "wind_gust": 2.94,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636081200,
            "temp": 279.88,
            "feels_like": 278.05,
            "pressure": 1025,
            "humidity": 65,
            "dew_point": 273.88,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.57,
            "wind_deg": 89,
            "wind_gust": 3.26,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636084800,
            "temp": 279.3,
            "feels_like": 277.26,
            "pressure": 1026,
            "humidity": 68,
            "dew_point": 273.8,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.7,
            "wind_deg": 93,
            "wind_gust": 4.23,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636088400,
            "temp": 278.7,
            "feels_like": 276.64,
            "pressure": 1025,
            "humidity": 69,
            "dew_point": 273.57,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.57,
            "wind_deg": 90,
            "wind_gust": 3.76,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636092000,
            "temp": 278.24,
            "feels_like": 276.23,
            "pressure": 1025,
            "humidity": 70,
            "dew_point": 273.3,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.42,
            "wind_deg": 83,
            "wind_gust": 3.17,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636095600,
            "temp": 277.85,
            "feels_like": 275.86,
            "pressure": 1025,
            "humidity": 71,
            "dew_point": 273.03,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.32,
            "wind_deg": 78,
            "wind_gust": 2.64,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636099200,
            "temp": 277.45,
            "feels_like": 275.36,
            "pressure": 1025,
            "humidity": 71,
            "dew_point": 272.79,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.35,
            "wind_deg": 75,
            "wind_gust": 2.77,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636102800,
            "temp": 277.07,
            "feels_like": 274.9,
            "pressure": 1025,
            "humidity": 72,
            "dew_point": 272.57,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.36,
            "wind_deg": 68,
            "wind_gust": 2.72,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636106400,
            "temp": 276.74,
            "feels_like": 274.46,
            "pressure": 1025,
            "humidity": 73,
            "dew_point": 272.32,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.41,
            "wind_deg": 67,
            "wind_gust": 3.03,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636110000,
            "temp": 276.43,
            "feels_like": 274.08,
            "pressure": 1025,
            "humidity": 73,
            "dew_point": 272.09,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.43,
            "wind_deg": 69,
            "wind_gust": 3.25,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636113600,
            "temp": 276.13,
            "feels_like": 273.68,
            "pressure": 1025,
            "humidity": 73,
            "dew_point": 271.86,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.48,
            "wind_deg": 69,
            "wind_gust": 3.31,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636117200,
            "temp": 276.15,
            "feels_like": 273.77,
            "pressure": 1026,
            "humidity": 72,
            "dew_point": 271.7,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.41,
            "wind_deg": 71,
            "wind_gust": 3.55,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636120800,
            "temp": 278.86,
            "feels_like": 276.87,
            "pressure": 1027,
            "humidity": 61,
            "dew_point": 271.9,
            "uvi": 0.29,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.53,
            "wind_deg": 74,
            "wind_gust": 4.36,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636124400,
            "temp": 281.7,
            "feels_like": 280.09,
            "pressure": 1027,
            "humidity": 50,
            "dew_point": 271.95,
            "uvi": 1.02,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.73,
            "wind_deg": 77,
            "wind_gust": 4.06,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636128000,
            "temp": 284.06,
            "feels_like": 282.33,
            "pressure": 1027,
            "humidity": 43,
            "dew_point": 272.09,
            "uvi": 2.16,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.77,
            "wind_deg": 81,
            "wind_gust": 3.67,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636131600,
            "temp": 285.87,
            "feels_like": 284.19,
            "pressure": 1026,
            "humidity": 38,
            "dew_point": 272.12,
            "uvi": 3.3,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.54,
            "wind_deg": 84,
            "wind_gust": 2.89,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636135200,
            "temp": 287.27,
            "feels_like": 285.65,
            "pressure": 1025,
            "humidity": 35,
            "dew_point": 272.3,
            "uvi": 3.92,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.37,
            "wind_deg": 82,
            "wind_gust": 2.5,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636138800,
            "temp": 288.26,
            "feels_like": 286.71,
            "pressure": 1024,
            "humidity": 34,
            "dew_point": 272.57,
            "uvi": 3.81,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.14,
            "wind_deg": 80,
            "wind_gust": 2.13,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636142400,
            "temp": 288.79,
            "feels_like": 287.27,
            "pressure": 1023,
            "humidity": 33,
            "dew_point": 272.82,
            "uvi": 2.92,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.17,
            "wind_deg": 83,
            "wind_gust": 2.14,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636146000,
            "temp": 288.91,
            "feels_like": 287.43,
            "pressure": 1023,
            "humidity": 34,
            "dew_point": 273.06,
            "uvi": 1.71,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.97,
            "wind_deg": 76,
            "wind_gust": 1.96,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636149600,
            "temp": 288.41,
            "feels_like": 286.93,
            "pressure": 1023,
            "humidity": 36,
            "dew_point": 273.68,
            "uvi": 0.69,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.87,
            "wind_deg": 73,
            "wind_gust": 2.1,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636153200,
            "temp": 285.24,
            "feels_like": 283.73,
            "pressure": 1023,
            "humidity": 47,
            "dew_point": 274.35,
            "uvi": 0.14,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.86,
            "wind_deg": 78,
            "wind_gust": 1.92,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636156800,
            "temp": 282.95,
            "feels_like": 282.17,
            "pressure": 1023,
            "humidity": 51,
            "dew_point": 273.43,
            "uvi": 0,
            "clouds": 1,
            "visibility": 10000,
            "wind_speed": 1.93,
            "wind_deg": 80,
            "wind_gust": 1.95,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636160400,
            "temp": 281.99,
            "feels_like": 280.92,
            "pressure": 1024,
            "humidity": 54,
            "dew_point": 273.38,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.08,
            "wind_deg": 94,
            "wind_gust": 2.12,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636164000,
            "temp": 281.3,
            "feels_like": 280.02,
            "pressure": 1024,
            "humidity": 57,
            "dew_point": 273.36,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.19,
            "wind_deg": 101,
            "wind_gust": 2.24,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636167600,
            "temp": 280.75,
            "feels_like": 279.5,
            "pressure": 1024,
            "humidity": 59,
            "dew_point": 273.29,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.05,
            "wind_deg": 95,
            "wind_gust": 2.06,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636171200,
            "temp": 280.24,
            "feels_like": 279.06,
            "pressure": 1025,
            "humidity": 61,
            "dew_point": 273.21,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.89,
            "wind_deg": 84,
            "wind_gust": 1.94,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636174800,
            "temp": 279.72,
            "feels_like": 278.3,
            "pressure": 1025,
            "humidity": 63,
            "dew_point": 273.16,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 2.05,
            "wind_deg": 94,
            "wind_gust": 2.09,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636178400,
            "temp": 279.17,
            "feels_like": 277.78,
            "pressure": 1025,
            "humidity": 65,
            "dew_point": 273.12,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.93,
            "wind_deg": 100,
            "wind_gust": 1.95,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636182000,
            "temp": 278.76,
            "feels_like": 277.28,
            "pressure": 1025,
            "humidity": 67,
            "dew_point": 273.09,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.95,
            "wind_deg": 104,
            "wind_gust": 1.98,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636185600,
            "temp": 278.42,
            "feels_like": 276.94,
            "pressure": 1025,
            "humidity": 68,
            "dew_point": 273.06,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.9,
            "wind_deg": 106,
            "wind_gust": 1.96,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1636189200,
            "temp": 278.11,
            "feels_like": 276.73,
            "pressure": 1025,
            "humidity": 69,
            "dew_point": 273.02,
            "uvi": 0,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 1.76,
            "wind_deg": 101,
            "wind_gust": 1.78,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "pop": 0
        }
    ]
    }
    return r_dictionary
    
def get_Data_current(city):
    lat,lon = city_cood[city][0],city_cood[city][1]
    r2 = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&cnt=1&appid=3ca2a253a882ec9e7b479e623f4a842f')
    r_dictionary= r2.json()
    if(r_dictionary["cod"] == 200):return r_dictionary
    else :
        r_dictionary = {
            "coord": {
                "lon": 37.5,
                "lat": 55.5
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 282.8,
                "feels_like": 281.75,
                "temp_min": 282.13,
                "temp_max": 283.38,
                "pressure": 1017,
                "humidity": 78
            },
            "visibility": 10000,
            "wind": {
                "speed": 2.24,
                "deg": 230
            },
            "clouds": {
                "all": 40
            },
            "dt": 1636024360,
            "sys": {
                "type": 2,
                "id": 2036130,
                "country": "RU",
                "sunrise": 1636000887,
                "sunset": 1636033538
            },
            "timezone": 10800,
            "id": 495260,
            "name": "Shcherbinka",
            "cod": 200
        }
    return r_dictionary