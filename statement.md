# Problem Statement
People often struggle to find music that matches their emotional state. Selecting songs manually can be time-consuming, especially when the user simply wants music that fits their current mood.  
There is a need for a lightweight application that can understand the user’s mood through text input and generate a suitable playlist automatically


# Scope of the Project
The project focuses on creating a mood-based playlist generator using Python.  
The system:
- Accepts a text message describing the user’s mood.
- Detects emotional keywords such as happy, sad, romantic, angry, or calm.
- Uses the Spotify Web API to fetch songs related to the detected mood.
- Generates and displays a playlist to the user.

The scope is limited to:
- Text-based mood detection  
- Spotify search API (no audio streaming)  
- Command-line interaction  
- Three main modules: mood detection, Spotify API handling, and playlist generation  


# Target Users
- "Music listeners" who want quick playlist suggestions based on mood  
- "Students or beginners" learning API integration and modular Python programming  
- "Users looking for simple text-based music recommendations"
- "Anyone wanting personalized music without browsing manually"


# High-Level Features
1. "Mood Detection Module"
   Analyzes the user's input and identifies their mood using keyword matching.

2. "Spotify API Integration"
   Connects to Spotify using Spotipy and retrieves relevant tracks based on mood.

3. "Playlist Generation"
   Combines mood detection and Spotify search to produce a curated playlist of 10 songs.

4. "Fallback Behavior"
   When mood is unclear, generates a mixed playlist to ensure smooth user experience.

5. "Simple Terminal Interface"
   Runs directly from Python without additional setup or UI frameworks.
