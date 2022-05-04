import os
from flask import Flask, render_template
from utils import serializeTopTracks, serializeRecentTracks
from spotipy.cache_handler import MemoryCacheHandler
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

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
    spotify_data = {'top_short': None,
                    'top_long': None,
                    'recent': None,
                    }

    scope = 'user-read-recently-played, user-top-read'

    # setup spotify credentials to get user data
    # using stored data about the token so that we can avoid the redirect when
    # using Heroku
    mem_token = {
        'access_token': os.getenv("ACCESS_TOKEN"),
        'token_type': os.getenv("TOKEN_TYPE"),
        'expires_in': int(os.getenv("EXPIRES_IN")),
        'refresh_token': os.getenv("REFRESH_TOKEN"),
        'scope': os.getenv("SCOPE"),
        'expires_at': int(os.getenv("EXPIRES_AT"))
    }

    # storing token template in the MemoryCacheHandler
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        show_dialog=False,
        cache_handler=MemoryCacheHandler(
            token_info=mem_token
        )
    ))

    # get top tracks over short_term
    top_short = spotify.current_user_top_tracks(
        limit=10, offset=10, time_range='short_term')
    spotify_data['top_short'] = serializeTopTracks(top_short)

    # get top tracks over long_term
    top_long = spotify.current_user_top_tracks(
        limit=10, offset=10, time_range='medium_term'
    )
    spotify_data['top_long'] = serializeTopTracks(top_long)

    # get recent tracks
    recent = spotify.current_user_recently_played(limit=20)
    spotify_data['recent'] = serializeRecentTracks(recent)

    return render_template('results.html', data=spotify_data)
