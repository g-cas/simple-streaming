# Simple-streaming
### A very simple YouTube streaming web app designed for kids.

This web app presents a specified number of user-selected YouTube videos in predefined categories that a child is able to access.

The significant amount of available options on YouTube and the ease at which one can switch between videos may create a degree of decision fatigue and may also negatively impact one's attention span.
The aim of this app is to reduce the amount of choices that one is exposed to when streaming videos on YouTube.
With the hope that the viewer will be better able to focus on each video and will also maintain a decent level of focus.

The web app utilises Google's YouTube API and is made using Python and Django.

The app presents a webpage that displays six video categories:
- TV
- Education
- Documentary
- Video Games
- Sport
- Music

Each category displays 3 randomly selected videos from a set of user-made YouTube playlists.


The app is set up using the standard Django architecture (https://docs.djangoproject.com/en/4.2/) 
with the following app-specific files:
- A configuration file (config.py)
- A date log file (last_shuffle_date.txt)

And for each of the 6 video categories there is one:
- YouTube playlist
- Python view file
- HTML template
- Log file

### File Descriptions

#### Configuration file
The configuration file (config.py) is used to store the YouTube API key and the relevant playlist IDs
This file will need to be modified as part of the setup process, by inputting the users unique API key and the ID's of the 6 playlists that they create.

    # API key
    api_key = '[unique_youtube_API-Key]'

    # Playlist IDs
    sport_playlist_id = '[unique_playlist_ID]'
    doco_playlist_id = '[unique_playlist_ID]'
    game_playlist_id = '[unique_playlist_ID]'
    education_playlist_id = '[unique_playlist_ID]'
    tv_playlist_id = '[unique_playlist_ID]'
    music_playlist_id = '[unique_playlist_ID]'

#### Date log file 
The date log file (last_shuffle_date.txt) is used to log the date that the videos in each category playlist were last shuffled. The purpose of this log is so that videos are only shuffled once per day.
The Python view file associated with each playlist writes the date it was last run to this file.

#### YouTube playlist
An individual YouTube playlist must be created for each of the 6 categories, using the same Google account that setup the Youtube API.
This is where the user can add all the videos that will be randomly selected for each category on the web app.
For example: a playlist for the Documentary category called "Doco_playlist" would contain a selection of documentary style videos.

#### Python view file
Each Python view file ({category_name}_views.py) is associated with a specific category. 
The view file contains the code that: 
1. retrieves the YouTube video data from each playlist (video ID, title, and thumbnail),
2. shuffles the list of videos,
3. randomly selects 3 videos,
4. records the date of the shuffle, and
5. passes the video information to the HTML file.

#### HTML template
The HTML file ({category}_videos.html) receives the video information from each associated Python view file
and displays the video thumbnails of each video in the relevant category.
Users are able to navigate to each category using the icons in the sidebar and can play videos in an embedded YouTube player by clicking on each video thumbnail. 

#### Log file
There is a text log file ({category}_shuffle_list.txt) associated with each Python view file, which is used to record the last randomly selected list of videos.
This list acts as a source of information to pass to the HTML template file if the code, instead of reshuffling the playlist videos, if the code is run more than once on the same day.
The purpose of this is so that videos are only shuffled once per day. Removing the possibility that a new list can be generated just by reloading the web page.

### Step-up Guide

1. Set up a YouTube API key
    https://developers.google.com/youtube/registering_an_application

2. Create 6 playlists on the YouTube account that was used to obtain the API key.
    For ease of use it is suggested that the playlist names reflect the 6 video categories:
        'TV', 'Education', 'Documentaries', 'Video Games', 'Sport', and 'Music'.

3. Edit Gandalf/Frodo/config.py
    Replace "YOUR_API_KEY" and the 6 "PLAY_LIST_ID" fields with the unique API and playlist IDs.

4. Run the Django project (manage.py) on a local server.

