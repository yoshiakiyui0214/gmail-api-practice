from googleapiclient.discovery import build

API_KEY = 'YOUR_API_KEY'
SEARCH_KEYWORD = 'Python プログラミング'  # 検索キーワード

def search_youtube(keyword):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    request = youtube.search().list(
        part='snippet',
        q=keyword,
        maxResults=5,
        type='video'
    )
    response = request.execute()
    
    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        url = f'https://www.youtube.com/watch?v={video_id}'
        print(f'タイトル: {title}')
        print(f'URL: {url}')
        print('---')

if __name__ == '__main__':
    search_youtube(SEARCH_KEYWORD)