import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID="7c75f40f2c454269be62150af5b48a7f"
CLIENT_SECRET="6ad9afa73ea146ada7c32412bdc4ff26"

def create_spotify_client():
    AUTH_MANAGER = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=AUTH_MANAGER)
    return sp