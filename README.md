# Moodify – Mood-Based Spotify Playlist Generator

Moodify is a Python-based application that detects a user's mood from text input and generates a personalized Spotify playlist based on that mood. It uses mood analysis, keyword matching, and the Spotify Web API to suggest relevant songs.


# Project Overview

Moodify is designed to interpret a user's emotional state from their message and recommend music that fits their mood.  
It combines text processing, API integration, and modular Python programming to create an interactive and user-friendly experience.

Key workflow:
1. User enters how they feel.
2. The system detects the mood.
3. Spotify API is queried for suitable songs.
4. A playlist matching the mood is displayed.


# Features

"Functional Features"
- "Mood Detection:"Identifies moods such as happy, sad, romantic, angry, and calm.
- "Spotify Search Integration:" Uses Spotify Web API (via Spotipy) to fetch matching songs.
- "Playlist Generation:" Produces a curated playlist of ~10 songs based on mood.
- "Fallback Handling:" Generates a mixed playlist when mood is unclear.

"Additional Capabilities"
- Clean terminal-based interaction  
- Modular code split across multiple Python files  
- Clear input → process → output flow  


# Technologies / Tools Used

- "Python 3"
- "Spotipy (Spotify Web API wrapper)"
- "Random module"
- "Visual Studio Code"
- "Git & GitHub" for version control
- "Spotify Developer API" for song retrieval


# How to Install & Run the Project

1. "Download or clone the repository"
   ```bash
   git clone https://github.com/itsananyag25/Moodify.git
3. Install the required library
    pip install spotipy
5. Run the main Python file
   python main_source_code.py
6. Enter your mood when prompted
   Example: “I am happy today”.

The program will detect your mood and generate a playlist accordingly.


# Testing Instructions

To test Moodify:

1. "Run the program" using:
   ```bash
   python main_source_code.py
2. Enter any mood-based text, such as:
   "I am happy today"
   "Feeling emotional"
   "I want calm music"
   "I'm angry right now"
3. Verify the output:
   The detected mood should match the mood in your sentence.
   The playlist generated should contain songs related to that mood.
4. Test edge cases:
   Enter unclear or neutral text (e.g., "okay", "hmm").
   The program should generate a fallback playlist.


# Screenshots

1. Program starts successfully — Mood-Based Playlist Generator welcomes the user and prompts for mood input.
<img width="1366" height="731" alt="image" src="https://github.com/user-attachments/assets/d9e46fbb-c8b7-4aa9-8113-b4a675b1e40a" />
2. User enters their mood (“I am feeling very happy today.”) in the terminal.
<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/3306683c-0e9d-4b74-a390-d74d8c1f1b37" />
3. Detected mood: happy. The system fetches and displays 10 happy-themed songs from Spotify.
<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/cca531f7-e80d-45e4-9f89-7faea012bc90" />
4. Detected mood: romantic. The system generates a romantic playlist using Spotify API results.
<img width="1366" height="721" alt="image" src="https://github.com/user-attachments/assets/99d7c484-0d0c-4d19-ab8d-1d16ebaabe5e" />
5. Detected mood: sad. A list of sad/lofi-themed songs is fetched and displayed based on Spotify search results
<img width="1366" height="725" alt="image" src="https://github.com/user-attachments/assets/011bda3a-032e-42d2-9c10-e31f4164b121" />






