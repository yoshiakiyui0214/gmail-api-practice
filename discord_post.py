import requests

WEBHOOK_URL = "your_webhook_url_here"

def send_discord_message(message):
    payload = {
        "content": message
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    
    if response.status_code == 204:
        print("✅ メッセージ送信成功！")
    else:
        print(f"❌ エラー: {response.status_code}")

send_discord_message("Hello from Python! 🎉")