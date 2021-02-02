from helper_functions import title_case
class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  # TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self.__title = title_case(title)


  # TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song


  # TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.__next_song = next_title


  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    # song_title = "The name of the song is: " + self.__title
    return f'The name of the song is: {self.__title}'


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return f'{self.__title} -> {self.__next_song}'

if __name__ == "__main__":
    song_one = Song("The quick brown fox jumps over")
    # print(song_one.get_title())
    song_one.set_title("The quick brown fox jumps over")
    # print(song_one.get_title())
    song_one.set_title("a tale of two cities")
    # print(song_one.get_title())
    print(song_one.__str__())
    print(song_one.__repr__())