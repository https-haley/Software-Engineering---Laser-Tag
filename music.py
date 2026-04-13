import os
import random
import pygame


class MusicPlayer:
	def __init__(self):
		pygame.mixer.init()
		self.current_track = None

		base_dir = os.path.dirname(os.path.abspath(__file__))

		# Auto-load all audio files in this folder
		self.tracks = []
		for file_name in os.listdir(base_dir):
			if file_name.lower().endswith((".mp3", ".wav", ".ogg")):
				self.tracks.append(os.path.join(base_dir, file_name))

	def play_random_track(self):
		if not self.tracks:
			print("No music tracks found.")
			return

		self.current_track = random.choice(self.tracks)

		pygame.mixer.music.load(self.current_track)
		pygame.mixer.music.play(-1)  # loop forever

		print(f"Playing: {os.path.basename(self.current_track)}")

	def stop_music(self):
		pygame.mixer.music.stop()
		print("Music stopped.")
