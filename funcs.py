import requests

class Spotify:
    def __init__(self, token):
        self.token = token

    def create_playlist(self, playlist_name, description):
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + self.token}
        data = {
                    "name": playlist_name,
                    "description": description,
                    "public": False
        }
        response = requests.post(f"https://api.spotify.com/v1/users/piggyawesomeyt/playlists", json=data, headers=headers)
        return response

    def convert_tracks(self, tracks):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
        }
        spotify_tracks = []
        errors = []

        for track in tracks:
            name = track[0].replace('\'', '')
            artist = track[1].replace('\'', '')

            params = {
                'q': f"track:{name} artist:{artist}",
                'type': 'track,artist',
                'market': 'ES',
                'limit': '1',
                'offset': '0',
            }

            response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)

            try:
                print("[SPOTIFY] Found: " + response.json()["tracks"]["items"][0]["name"] + " | " + str(response.status_code))
                spotify_tracks.append(response.json()["tracks"]["items"][0]["id"])
            except IndexError:
                print("ERROR: " + name + " | " + artist +  " | " + str(response.status_code))
                errors.append([name, artist])
                pass
            except KeyError:
                print("ERROR: " + name + " | " + artist +  " | " + str(response.status_code))
                errors.append([name, artist])
                pass

        return spotify_tracks, errors


    def add_tracks(self, tracks, playlist):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
        }

        uris = []
        for track in tracks:
            uris.append(f'spotify:track:{track}')

        params = {
            'uris': ','.join(uris),
        }
        print(playlist, params, headers)
        response = requests.post(playlist + "/tracks", params=params, headers=headers)

        return response

class Deezer:
    def __init__(self, playlist):
        self.playlist = playlist

    def get_tracks(self, data):
        response = requests.get(f"https://api.deezer.com/playlist/{self.playlist}/tracks?{data}")
        return response