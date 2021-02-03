from Playlist import Playlist
from helper_functions import webscrape__spotify_top200

playlist = Playlist()

while True:

  # Prints welcome message and options menu
  print('''

  Welcome to Playlist Maker 🎶  

  =====================================
  Options:
  1: View playlist
  2: To add a new song to playlist
  3: To remove a song from playlist
  4: To search for song in playlist
  5: Return the length of the playlist
  6: Add top 200 songs from spotify to playlist
  =====================================

  ''')

  # Prints welcome message and options menu
  user_selection = int(input('Enter one of the 5 options:  '))

  # Option 1: View playlist
  if user_selection == 1:
    playlist.print_songs()


  # Option 2: To add a new song to playlist
  elif user_selection == 2:
    song_title = input('What song do you want to add? ')
    playlist.add_song(song_title)



  # Option 3: To remove a song from playlist
  elif user_selection == 3:
    song_title = input('What song do you want to remove? ')
    playlist.remove_song(song_title)


  # Option 4: To search for song in playlist
  elif user_selection == 4:

    song_title = input('Which song do you want to find? ')
    index = playlist.find_song(song_title)
    
    if index == -1:
      print(f"The song {song_title} is not in the set list.")
    else:
      print(f"The song {song_title} is song number {index+1}")


  # Option 5: Return the length of the playlist
  elif user_selection == 5:
    print(f"This set list has {playlist.length()} songs.")

  # Option 6: To add the top 200 songs on spotify to playlist
  elif user_selection == 6:
    top_200_global_songs = webscrape__spotify_top200()
    top_200_global_songs.reverse()                              # To have the linked list ordered from most to least popular
    for song in top_200_global_songs:
        playlist.add_song(song)

    print(f"Top 200 songs added to the playlist.")
    
  # Message for invalid input
  else:
    print('That is not a valid option. Try again.\n')