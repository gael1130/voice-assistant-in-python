# To access Spotipy
import spotipy
# for error handling
from urllib.error import HTTPError
import fixed


username = fixed.username
clientID = fixed.clientID
clientSecret = fixed.clientSecret
redirectURI = fixed.redirectURI
scope = 'user-read-playback-state user-modify-playback-state'

# Create OAuth Object
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI, scope)
# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

laptop_id = fixed.laptop_id
work_playlist = fixed.work_playlist
sport_playlist = fixed.work_playlist


def start_spotify_playlist(playlist):
    try:
        spotifyObject.start_playback(device_id=laptop_id, context_uri=playlist)
    except HTTPError as err:
        if err.code == 404:
            print("error 404 because the desktop app was closed")
    except Exception as e:
        print("new exception is: ")
        print(e)
    finally:
        print("still working")


def pause_spotify():
    try:
        spotifyObject.pause_playback(device_id=laptop_id)
    except HTTPError as err:
        if err.code == 403:
            print("error 403 because the player was already on pause")
        elif err.code == 404:
            print("error 404 because the desktop app was closed")
        elif err.code == 401:
            print("error 401 because the player was already on pause")

    except Exception as e:
        print("new exception is: ")
        print(e)

    finally:
        print("I am still working")
