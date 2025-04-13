import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

def search_youtube(query, excluded_channel_ids, api_key):
    """Searches YouTube for videos related to the query, excluding the specified channels."""
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        q=query,
        maxResults=10,  # You can adjust the number of videos to fetch
        order='relevance',
        type='video'
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        if item['snippet']['channelId'] not in excluded_channel_ids:
            video = {
                'video_id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                'channel': item['snippet']['channelTitle'],
                'publication_date': item['snippet']['publishTime']
            }
            videos.append(video)

    return videos


def get_transcript(video_id):
    """Fetches the transcript for a YouTube video."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([entry['text'] for entry in transcript])
        return text
    except Exception as e:
        print(f"Error fetching transcript for video {video_id}: {e}")
        return ""


if __name__ == '__main__':
    # Replace with your actual API key and search query
    api_key = os.environ.get('YOUTUBE_API_KEY')
    query = "increase grip strength"
    excluded_channel_ids = ['UCqvYPK5Ss22I-NBTAleODfw']  # Kaizen Mentality channel ID

    if not api_key:
        print("Error: YOUTUBE_API_KEY environment variable not set.")
    else:
        videos = search_youtube(query, excluded_channel_ids, api_key)
        for video in videos:
            print(f"Title: {video['title']}")
            print(f"Description: {video['description']}")
            print(f"URL: {video['url']}")
            print(f"Channel: {video['channel']}")
            print(f"Publication Date: {video['publication_date']}")

            transcript = get_transcript(video['video_id'])
            if transcript:
                print(f"Transcript: {transcript[:200]}...")  # Print first 200 characters
            print("-" * 20)