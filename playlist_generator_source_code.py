from spotify_client_source_code import create_spotify_client

def get_spotify_tracks_for_mood(user_mood):
    import random
    offset_value = random.randint(0,999)
    sp = create_spotify_client()
    mood_text = user_mood + " songs"
    result = sp.search(q=mood_text, type="track", limit=10 , offset=offset_value)
    playlist = []
    for each_song in result["tracks"]["items"]:
        song_name = each_song["name"]
        artist_name = each_song["artists"][0]["name"]
        playlist.append(song_name + "-" + artist_name)
    return playlist

def generate_playlist_from_mood(mood):
    print(f"\nFetching songs for mood: {mood} ...")
    playlist = get_spotify_tracks_for_mood(mood)
    return playlist