from bs4 import BeautifulSoup
import requests
import pandas as pd

def title_case(title):
    """This function will return a string formated to be Title Cased."""

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

    return reformatted_title

def webscrape__spotify_top200():
    """This function will collect the Top 200 songs globaly listed in Spotify and return it as a list."""

    url = "https://spotifycharts.com/regional/global/daily/latest"
    page = requests.get(url)

    page_content = BeautifulSoup(page.content, 'html.parser')

    song_titles = []
    for title in page_content.find_all('strong'):
        title = title.get_text()
        song_titles.append(title)

    return song_titles