import requests

CHANNEL_ACCESS_TOKEN = "your_line_token_here"
WEATHER_API_KEY = "your_weather_api_key_here"
USER_ID = "your_user_id_here"
CITY = "Tokyo"

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": CITY,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "ja"
    }
    response = requests.get(url, params=params)
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    message = f"今日の東京の天気\n{weather}\n気温：{temp}C\n最高：{temp_max}C / 最低：{temp_min}C"
    return message

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"ステータスコード: {response.status_code}")

message = get_weather()
print(message)
send_line_message(message)