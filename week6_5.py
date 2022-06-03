import json
import re
from urllib import request

from bs4 import BeautifulSoup
import requests
import lyricsgenius as lg


# Group by
from lyricsgenius import Genius


def group_by(func, iterable):
    """
    Gets a function and an iterable and returns a dictionary which the keys are what the function
    returns on the item of the iterable and the value is a list of the items that the result
    on those items it is this key.
    Possible input:   len, ["hi", "bye", "yo", "try"]
    Output:           {2: ["hi", "yo"], 3: ["bye", "try"]}
    :param func: A function
    :param iterable: An iterable
    :return: Dictionary of key and value like explained
    """
    dictionary = {}
    for item in iterable:
        if func(item) in dictionary:
            dictionary[func(item)].append(item)
        else:
            dictionary[func(item)] = [item]
    return dictionary


# zipwith


def zip_with(func, *args):
    """
    Gets a function (func) and an unlimited number of iterables with the same length, and activate the
    function on all the items of the iterable that are on same place in order.
    Input (possible):  sum, [1, 2, 3], [4, 5, 6]
    Output:            [5, 7, 9]
    :param func: A function
    :param args: A list of iterables with the same length
    :return: List of the results that the function passed returns on each item of the iterables in order
    """
    return [func(item) for item in zip(*args)]


def find_most_popular_songs_and_their_producers(url):
    response = requests.get(url)
    page = BeautifulSoup(response.content, 'html.parser')

    div_carts = page.find_all('div', {'class': 'o-chart-results-list-row-container'})

    dictionary = {}
    for div in div_carts:
        name_of_song = div.find('h3', {'id': 'title-of-a-story', 'class': 'c-title'}).text.strip()
        artist_name = div.find('li', {'class': 'lrv-u-width-100p'}).find('span', {'class', 'c-label'}).text.strip()
        dictionary[name_of_song] = artist_name

    return dictionary


def find_lyrics_of_songs():
    output_file = open("out.txt", "w", encoding='UTF8')
    for song_of_name, artist_name in my_dict_top_100.items():
        write_lyrics(output_file, artist_name, song_of_name)

    output_file.close()


def write_lyrics(file, artist, song_name):
    first_artist = artist.split(',')[0]
    url = 'https://api.lyrics.ovh/v1/' + first_artist + '/' + song_name
    response = requests.get(url)
    json_data = json.loads(response.content)
    lyrics = json_data['lyrics']
    file.write(f"----------------------------\nSong: {song_name} - Artist: {artist}\n")
    file.write(lyrics)


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
    print("------------------------------------------")

    print(zip_with(sum, [1, 2, 3], [4, 5, 6]))
    print(zip_with(max, (5, 4), (2, 5), (6, -6)))
    print(zip_with(max, (5, 4), (2, 5), (6, -6), (11, 9)))
    print("-------------------------------------------")

    url_billboard = "https://www.billboard.com/charts/hot-100/"
    my_dict_top_100 = find_most_popular_songs_and_their_producers(url_billboard)
    for song_name, artist in my_dict_top_100.items():
        print(f"Song: {song_name}\nArtist: {artist}\n")

    find_lyrics_of_songs()
