# backup of view.py

import random
from django.shortcuts import render
from googleapiclient.discovery import build
# from django.conf import settings

# API key and playlist ID
api_key = 'AIzaSyDDauvCAPhlHSxn-8N46kr0eeg8NM66mWo'
playlist_id = 'PL_J_SBs-mT9ObdEjMhfGxWzC27lOIYpAc'


def get_videos(request):
    # Build the YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Retrieve videos from the playlist
    video_list = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50,
    ).execute()

    # Extract video details from the playlist items
    videos = []
    for item in video_list['items']:
        video_id = item['snippet']['resourceId']['videoId']
        title = item['snippet']['title']
        thumbnail_url = item['snippet']['thumbnails']['high']['url']
        videos.append({
            'video_id': video_id,
            'title': title,
            'thumbnail_url': thumbnail_url
        })

    # Shuffle the videos
    random.shuffle(videos)

    # The number of videos to display
    random_videos = videos[:6]

    # Return the random videos to the template
    context = {
        'random_videos': random_videos
    }
    return render(request, 'daily_videos.html', context)
