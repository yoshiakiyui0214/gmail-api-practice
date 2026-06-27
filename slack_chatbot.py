from slack_sdk import WebClient

SLACK_BOT_TOKEN = "your_slack_token_here"
CHANNEL = "#all-python学習"

slack_client = WebClient(token=SLACK_BOT_TOKEN)

def simple_chatbot(question):
    responses = {
        "天気": "今日は晴れのち曇りです。気温は25度前後でしょう。",
        "Python": "Pythonはシンプルで読みやすい構文、豊富なライブラリ、幅広い用途が特徴です。",
        "おはよう": "おはようございます！今日も一日頑張りましょう！",
    }
    for key, response in responses.items():
        if key in question:
            return response
    return "すみません、その質問にはまだ対応していません。"

def send_to_slack(question):
    answer = simple_chatbot(question)
    message = f"Q: {question}\n\nA: {answer}"
    slack_client.chat_postMessage(channel=CHANNEL, text=message)
    print("Slackに送信しました")
    print(message)

send_to_slack("Pythonについて教えてください")