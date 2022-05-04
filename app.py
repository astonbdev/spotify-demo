import os
from flask import Flask, render_template
from utils import serializeTopTracks, serializeRecentTracks
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv

CURR_USER_KEY = "curr_user"
BASE_URL = "http://localhost:5001"

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")
app.config['CLIENT_SECRET'] = os.getenv('CLIENT_SECRET')
app.config['SPOTIFY_ID'] = os.getenv('SPOTIFY_ID')


@app.get('/')
def homepage():
    """Show results:
    renders tables for spotify data from my user account
    includes tables for top_short tracks, top_medium tracks,
    and recently played
    """
    # client_secret = app.config['CLIENT_SECRET']
    # client_id = app.config['SPOTIFY_ID']

    # auth_options = {'url': 'https://accounts.spotify.com/api/token',
    #                 'headers': {
    #                     'Authorization': f'Basic {client_id}:{client_secret}'
    #                 },
    #                 'form': {
    #                     'grant_type': 'client_credentials'
    #                 },
    #                 'json': True
    #                 }
    print("Hello")
    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials())
    spotify_data = {'top_short': None,
                    'top_long': None,
                    'recent': None,
                    }
    # setup spotify credentials to get user data
    scope = 'user-read-recently-played, user-top-read'
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope, username=os.getenv("USERNAME")))
    print("after Spotify OAtuh creds")
    # get top tracks over short_term
    top_short = spotify.current_user_top_tracks(
        limit=10, offset=10, time_range='short_term')
    spotify_data['top_short'] = serializeTopTracks(top_short)
    print("short", top_short)

    # get top tracks over long_term
    top_long = spotify.current_user_top_tracks(
        limit=10, offset=10, time_range='medium_term'
    )
    spotify_data['top_long'] = serializeTopTracks(top_long)
    print("long", top_short)

    # get recent tracks
    recent = spotify.current_user_recently_played(limit=20)
    spotify_data['recent'] = serializeRecentTracks(recent)

    print(spotify_data)

    return render_template('results.html', data=spotify_data)
