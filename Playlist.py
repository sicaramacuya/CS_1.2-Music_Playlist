from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)                          # new Song object created
    new_song.set_next_song(self.__first_song)       # sets new_song to point at whatever the head was pointing.
    self.__first_song = new_song                    # sets head to point at new_song



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    index = 0
    current_song = self.__first_song

    while current_song:

        if current_song.get_title() == title:
            return index
        index += 1
        current_song = current_song.get_next_song()

    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    previous_song = None
    current_song = self.__first_song
    
    if current_song is not None:                                # this piece of code is for the case where the first song in the playlist is the one to remove.
        if current_song.get_title() == title:
            self.__first_song = current_song.get_next_song()
            return f"{title} has been removed."

    while current_song is not None:                             # this piece of code runs for every playlist where the first song is not the one to remove.

        if current_song.get_title() == title:                   # this runs when the song has been found and it will break out of the while loop
            break
        
        previous_song = current_song          
        current_song = current_song.get_next_song()
    
    if current_song == None:                                    # runs when song is not in the playlist.
        return f"{title} is not found."

    song_to_be_swap = current_song.get_next_song()
    previous_song.set_next_song(song_to_be_swap)
    return f"{title} has been removed."


  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    count = 0
    current_song = self.__first_song

    while current_song != None:
        count += 1
        current_song = current_song.get_next_song()

    return count


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    count = 1
    current_song = self.__first_song

    while current_song != None:
        print(f"{count}. {current_song.get_title()}")

        count += 1
        current_song = current_song.get_next_song()
    
    return

if __name__ == "__main__":
    latin_hits = Playlist()

    latin_hits.add_song("Vete")
    latin_hits.add_song("Girl")
    latin_hits.add_song("Negro")


    print(latin_hits.find_song("Negro"))                                        # Index 0
    print(latin_hits.find_song("Girl"))                                         # Index 1
    print(latin_hits.find_song("Vete"))                                         # Index 2
    print(latin_hits.length())
    latin_hits.print_songs()
    print("--------------")
    print(latin_hits.find_song("La Canción"))                                   # -1 
    print("--------------")
    print(latin_hits.remove_song("Girl"))                                       # Girl has been removed.
    print(latin_hits.find_song("Girl"))                                         # -1
    print("--------------")
    print(latin_hits.find_song("Negro"))                                        # Index 0
    print(latin_hits.find_song("Vete"))                                         # Index 1
    print(latin_hits._Playlist__first_song._Song__next_song.get_next_song())    # None
    print("--------------")
    print(latin_hits.length())
    latin_hits.print_songs()


