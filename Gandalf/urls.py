"""
URL configuration for Gandalf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from Frodo.views import get_videos
from Frodo.tv_views import get_tv_videos
from Frodo.education_views import get_education_videos
from Frodo.doco_views import get_doco_videos
from Frodo.game_views import get_game_videos
from Frodo.sport_views import get_sport_videos
from Frodo.music_views import get_music_videos

urlpatterns = [
    path('', get_videos, name='get_videos'),
    path('daily_videos/', get_videos, name='get_videos'),
    path('tv-videos/', get_tv_videos, name='tv_videos'),
    path('education-videos/', get_education_videos, name='education_videos'),
    path('doco-videos/', get_doco_videos, name='doco_videos'),
    path('game-videos/', get_game_videos, name='game_videos'),
    path('sport-videos/', get_sport_videos, name='sport_videos'),
    path('music-videos/', get_music_videos, name='music_videos'),
    path('admin/', admin.site.urls),
]
