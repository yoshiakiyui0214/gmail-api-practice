import requests

TOKEN = "your_token_here"
CHANNEL = "#all-python学習"

def send_slack_message(channel, message):
    url = "https://slack.com/api/chat.postMessage"
    
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "channel": channel,
        "text": message
    }
    
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    if result["ok"]:
        print("✅ メッセージ送信成功！")
    else:
        print(f"❌ エラー: {result['error']}")

send_slack_message(CHANNEL, "Hello from Python! 🎉")