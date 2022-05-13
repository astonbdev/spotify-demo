# spotify-demo
playing with the spotify api

## Setting Up The Environment
1. create a venv `python -m venv venv`
2. Install the required python libraries from requirements.txt `pip install -r requirements.txt`

## Running the flask server
1. In the CLI use `flask run` to start the server.
2. Access the site at `localhost:5001`

## Required Environment Variables

### these variables will be derived by creating a developer app on spotifys web pages
- APP_SECRET_KEY=
- SPOTIPY_CLIENT_SECRET=
- SPOTIPY_CLIENT_ID=
- SPOTIPY_REDIRECT_URI=
- USERNAME=

### these variables must be derived from a request that you make on your local server
- ACCESS_TOKEN=
- TOKEN_TYPE=
- EXPIRES_IN=
- REFRESH_TOKEN=
- SCOPE=
- EXPIRES_AT=
