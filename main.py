import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from collections import Counter

load_dotenv()

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_term(range):
    if range == 1:
        term = 'short_term'
    elif range == 2:
        term = 'medium_term'
    elif range == 3:
        term = 'long_term'
    return term

def print_results(op, term):
    if op == 1:
        results = sp.current_user_top_tracks(time_range=term)
        for idx, item in enumerate(results['items']):
            print(idx, item['name'], [a['name'] for a in item['artists']])

    elif op == 2:
        results = sp.current_user_top_artists(time_range=term)
        for idx, item in enumerate(results['items']):
            print(idx, item['name'])
    
    if op ==  3:
        results = sp.current_user_top_artists(time_range=term)
        for item in enumerate(results['items']):
            genres = [item['genres'] for item in results['items']]

        genres = [g for genre in genres for g in genre]

        genres = Counter(genres)

        top_genres = genres.most_common(10)

        for idx, genre in enumerate(top_genres):
            print(idx, (genre[0].capitalize()))
    



if __name__ == '__main__':

    print('**---TopT&A Spotify--**')
    op = int(input('''What do you want to list?
    1) Top Tracks
    2) Top Artists
    3) Top Genres\n'''))

    range = int(input('''Select range:
    1) Last 4 Weeks
    2) Last 6 Months
    3) All time \n'''))

    term = get_term(range)

    print_results(op, term)

        

