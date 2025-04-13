import os
from googleapiclient.discovery import build

def get_channel_videos(channel_id, api_key):
    """Fetches the latest videos from a YouTube channel."""
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=5,  # You can adjust the number of videos to fetch
        order='date',
        type='video'
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        video = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            'channel': item['snippet']['channelTitle'],
            'publication_date': item['snippet']['publishTime']
        }
        videos.append(video)

    return videos

if __name__ == '__main__':
    # Replace with your actual API key and channel ID
    api_key = os.environ.get('YOUTUBE_API_KEY')
    channel_id = 'UCqvYPK5Ss22I-NBTAleODfw'  # Kaizen Mentality channel ID

    if not api_key:
        print("Error: YOUTUBE_API_KEY environment variable not set.")
    else:
        videos = get_channel_videos(channel_id, api_key)
        for video in videos:
            print(f"Title: {video['title']}")
            print(f"Description: {video['description']}")
            print(f"URL: {video['url']}")
            print(f"Channel: {video['channel']}")
            print(f"Publication Date: {video['publication_date']}")
            print("-" * 20)
