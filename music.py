import os
import random
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_track = None

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.tracks = [
            os.path.join(base_dir, "music", "Track01.mp3"),
            os.path.join(base_dir, "music", "Track02.mp3"),  
            os.path.join(base_dir, "music", "Track03.mp3"),
            os.path.join(base_dir, "music", "Track04.mp3"),
            os.path.join(base_dir, "music", "Track05.mp3"),
            os.path.join(base_dir, "music", "Track06.mp3"),
            os.path.join(base_dir, "music", "Track07.mp3"),
            os.path.join(base_dir, "music", "Track08.mp3")
        ]

    def play_random_track(self):
        available_tracks = [track for track in self.tracks if os.path.exists(track)]

        if not available_tracks:
            print("No music tracks found in the 'music' directory.")
            return
        
        self.current_track = random.choice(available_tracks)
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.play(-1)  # Loop indefinitely
        print(f"Playing: {os.path.basename(self.current_track)}")

    def stop_music(self):
        pygame.mixer.music.stop()
        print("Music stopped.")
