import os
from flask import Flask, render_template
import json
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
    """Show homepage:

    - anon users: no messages
    - logged in: 100 most recent messages of followed_users
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
    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials())

    scope = 'user-top-read'
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope, username=os.getenv("USERNAME")))
    top_tracks = spotify.current_user_top_tracks(
        limit=1, offset=5, time_range='short_term')
    breakpoint()
    # top_tracks = json.load(top_tracks)
    tracks_info = []

    for track in top_tracks['items']:
        breakpoint()
        artists = []
        for artist in track['artists']:
            artists.append(artist['name'])
        tracks_info.append({
            "name": track['name'],
            "artists": artists,
            "album": track['album']['external_urls']['spotify']
        })

    print(tracks_info)

    return render_template('index.html')


# @app.get('/results')
# def topTracks():
#     """redirect from homepage, displays spotify results"""

#     return render_template('index.html')
