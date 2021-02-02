class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  # TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    #   1. List of all words that have to be in lower case.
    #   2. Check if any of the words in the title parameter is in the words that need to be lower case.
    #   3. If yes ignore the word, if no capitalize its first character.
    articles = ["a", "an", "the"]
    conjuctions = ["for", "and", "nor", "but", "or", "yet", "so"]
    prepositions = ["about", "above", "across", "after", "against", "among", "around", "at", "before", "behind", "below", "beside", "between", "by", "down", "during", "for", "from", "in", "inside", "into", "near", "of", "off", "on", "out", "over", "through", "to", "toward", "under", "up", "with"]
    lowercase_words = articles + conjuctions + prepositions

    words_in_title = title.split(" ")    
    reformatted_title = ""

    for word in words_in_title:

        if word == words_in_title[0]:
            reformatted_title += word.title() + " "
        elif word in lowercase_words:
            reformatted_title += word + " "
        else:
            reformatted_title += word.title() + " "
    
    reformatted_title = reformatted_title[:-1] # Getting rid of last space character at the end.
    self.__title = reformatted_title


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