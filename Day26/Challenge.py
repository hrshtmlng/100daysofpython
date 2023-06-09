# It was the challenge of the day It plays the song via importing audio module

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False 
  while True:
    stop_playback = int(input("Press 2 anything to stop playback and go back to the menu : "))
    if stop_playback == 2:
      source.paused = True
      return
    else:
      continue

while True:
  os.system("clear")
  print("🎵 MyPOD Music Player")
  time.sleep(2)
  print("Press 1 to Play")
  time.sleep(2)
  print("Press 2 to Exit")
  time.sleep(2)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue

