import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID="7c75f40f2c454269be62150af5b48a7f"
CLIENT_SECRET="6ad9afa73ea146ada7c32412bdc4ff26"

def create_spotify_client():
    AUTH_MANAGER=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
    sp=spotipy.Spotify(auth_manager=AUTH_MANAGER)
    return sp

def get_spotify_tracks_for_mood(user_mood):
    import random
    offset_value = random.randint(0,999)
    sp=create_spotify_client()
    mood_text=user_mood + " songs"
    result=sp.search(q=mood_text, type="track", limit=10 , offset=offset_value)
    playlist=[]
    for each_song in result["tracks"]["items"]:
        song_name=each_song["name"]
        artist_name=each_song["artists"][0]["name"]
        playlist.append(song_name + "-" + artist_name)
    return playlist

def detect_mood(text):
    text_lower=text.lower()
    if any(word in text_lower for word in ["happy", "excited", "joy"]):
        return "happy"
    elif any(word in text_lower for word in ["romantic","lofi","love"]):
        return "romantic"
    elif any(word in text_lower for word in ["sad", "down", "cry"]):
        return "sad"
    elif any(word in text_lower for word in ["angry", "mad", "furious"]):
        return "angry"
    elif any(word in text_lower for word in ["calm", "relaxed", "peaceful"]):
        return "calm"
    else:
        import random
        words=["hits", "top songs", "viral", "trending", "mix","bollywood"]
        random_genre=random.choice(words)
        return random_genre

def generate_playlist_from_mood(mood):
    print(f"\nFetching songs for mood: {mood} ...")
    playlist = get_spotify_tracks_for_mood(mood)
    return playlist

print("Welcome to the Mood-Based Playlist Generator!")
print("-----------------------------------------------")

user_input = input("How are you feeling today?")

mood = detect_mood(user_input)
print(f"\nDetected Mood: {mood}")

playlist = generate_playlist_from_mood(mood)

print("\nYour Spotify Playlist:")
for song in playlist:
    print("- ", song)



