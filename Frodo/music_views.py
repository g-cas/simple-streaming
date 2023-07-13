import random
import json
from django.shortcuts import render
from googleapiclient.discovery import build
from datetime import date
import Frodo.config

# The following details need to be edited for each category
# Line 17: Frodo.config.EDIT_playlist_id
# Line 20: html_file = 'EDIT_videos.html'
# Line 45: with open('EDIT_shuffle_list.txt', 'r') as file:
# Line 59: def get_EDIT_videos(request):
# Line 108: with open('EDIT_shuffle_list.txt', 'w') as file:


# API key and playlist ID imported from config
api_key = Frodo.config.api_key
playlist_id = Frodo.config.music_playlist_id

# Link to appropriate view file
html_file = 'music_videos.html'


# Get date of last shuffle from txt file
def get_last_shuffle_date():
    try:
        with open("last_shuffle_date.txt", "r") as file:
            last_shuffle_date_str = file.read()
            return date.fromisoformat(last_shuffle_date_str)
    except FileNotFoundError:
        return None
    except ValueError:
        return None


# Write date of last shuffle to txt file
def set_last_shuffle_date(last_shuffle_date):
    with open("last_shuffle_date.txt", "w") as file:
        file.write(last_shuffle_date.isoformat())


# Get the last shuffled list
def read_last_shuffle_list():
    try:
        # Read the content of the file
        with open("music_shuffle_list.txt", "r") as file:
            videos_json = file.read()

        # Parse the JSON data into a list of dictionaries
        old_shuffle = json.loads(videos_json)
        return old_shuffle
    except FileNotFoundError:
        return []


last_shuffle_list = read_last_shuffle_list()


def get_music_videos(request):

    last_shuffle_date = get_last_shuffle_date()
    current_date = date.today()

    if last_shuffle_date == current_date:
        inner_last_shuffle_list = read_last_shuffle_list()
        static_context = {
            'last_shuffle_list': inner_last_shuffle_list
        }
        return render(request, html_file, static_context)

    else:
        # Get video data from YouTube
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
        random_videos = videos[:3]

        # Set the date of last shuffle
        set_last_shuffle_date(current_date)

        # Convert the list of dictionaries to a JSON-formatted string
        videos_json = json.dumps(random_videos, indent=4)

        # Write the JSON string to a text file
        with open("music_shuffle_list.txt", "w") as file:
            file.write(videos_json)

        # Return the random videos to the template
        random_context = {
            'random_videos': random_videos
        }

        return render(request, html_file, random_context)
