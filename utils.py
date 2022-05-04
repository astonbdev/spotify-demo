def serializeTopTracks(results):
    """Parses backend response from spotify web API, returns list like:
    {name: track_name, artists: [artist1, artist2...], album: album_url"""
    tracks_info = []
    for track in results['items']:
        artists = []
        for artist in track['artists']:
            artists.append(artist['name'])
        tracks_info.append({
            "name": track['name'],
            "artists": artists,
            "album": (
                track['album']['name'],
                track['album']['external_urls']['spotify'])
        })

    return tracks_info


def serializeRecentTracks(results):
    """Parses backend response from spotify web API, returns list like:
    {name: track_name, artists: [artist1, artist2...], album: album_url"""
    tracks_info = []
    for track in results['items']:
        artists = []
        for artist in track['track']['artists']:
            artists.append(artist['name'])
        tracks_info.append({
            "name": track['track']['name'],
            "artists": artists,
            "album": (
                track['track']['album']['name'],
                track['track']['album']['external_urls']['spotify'])
        })

    return tracks_info
