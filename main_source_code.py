from mood_detector_source_code import detect_mood
from playlist_generator_source_code import generate_playlist_from_mood

print("Welcome to the Mood-Based Playlist Generator!")
print("-----------------------------------------------")

user_input = input("How are you feeling today?")

mood = detect_mood(user_input)
print(f"\nDetected Mood: {mood}")

playlist = generate_playlist_from_mood(mood)

print("\nYour Spotify Playlist:")
for song in playlist:
    print("- ", song)