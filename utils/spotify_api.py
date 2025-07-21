import os 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Creditials are set as enviromental variables for saftey

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')  
CLIENT_SECRET = os.getenc('SPOTIFY_CLIENT_SECRET')

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError ("Set spotify client enviromental variables")
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_playlist_tracks(playlist_id, limit= 100):
    """
    Fetches tracks from a Spotify playlist ID.
    Returns list of track dictionariies.
    """
    results = sp.playlist_tracks(playlist_id, limit=limit)
    tracks = results['items']
    all_tracks = []
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for item in tracks:
        track = item['track']
        all_tracks.append({
            
            'id': track['id'],
            'name' : track['name'],
            'artists' : [artist['name'] for artist in track['artits']],
            'popularity': track['popularity'],
            'duration_ms': track['duration_ms'],

        })
def get_playlist_name(playlist_id):
    """
    Fetches the name of a Spotify playlist using the playlist ID
   
    """
    results = sp.playlist(playlist_id=playlist_id, fields="name")
    return results["name"]

if __name__ == "__main__":
    playlist_id = input("Enter the id of the playlist")
    playlist_name = get_playlist_name(playlist_id)
    tracks = get_playlist_tracks(playlist_id)
    print(f"Fetched {len(tracks)} tracks from {playlist_name}")