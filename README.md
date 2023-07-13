# simple-streaming
A very simple YouTube streaming web app designed for kids.

This is a web app that presents a predefined and categorised amount of YouTube videos a child is able to access.
The significant amount of available options on YouTube and the ease at which one can switch between videos may create a degree of decision fatigue and may also negatively impact one's attention span.

The aim of this app is to reduce the amount of choices that one is exposed to when streaming videos on YouTube.
With the hope that the viewer will be better able to focus on each video and will also maintain a decent level of focus.

The web app utilises Google's YouTube API and is made using Python and Django.

The app presents a web interface with access to 6 video categories (presented as icons in a sidebar).
The videos of each category are randomly selected each day from user-made YouTube playlists.

The architecture is as follows:
    - A Django URLs file: urls.py
    - A date log file: last_shuffle_date.txt
    - A config file: config.py


For each category there are:
    - A YouTube playlist: App_[Category_name] (e.g."App_Sport")
    - A Python view file: [category_name]_views.py (e.g. sport_views.py
    - A HTML template: [category]_videos.html (e.g. sport_videos.html)
    - A TXT log file: [category]_shuffle_list.txt (e.g. sport_shuffle_list.txt)


Step-up Guide

1. Set up a YouTube API key
    https://developers.google.com/youtube/registering_an_application

2. Create 6 playlists on the YouTube account you used to obtained the API key
    For ease of use it is suggested that the playlist names reflect the 6 video categories:
        'TV', 'Education', 'Documentaries', 'Video Games', 'Sport', and 'Music'.

3. Edit Gandalf/Frodo/config.py
    Replace "YOUR_API_KEY" and the 6 "PLAY_LIST_ID" fields with your API and playlist IDs.

4. Edit each [category]_view.py file according to the instructions outline on line 8-12
    Find and replace "EDIT" with the relevant [category] name:
        # The following details need to be edited for each category
        # Line 17: Frodo.config.EDIT_playlist_id
        # Line 20: html_file = 'EDIT_videos.html'
        # Line 45: with open('EDIT_shuffle_list.txt', 'r') as file:
        # Line 107: with open('EDIT_shuffle_list.txt', 'w') as file: