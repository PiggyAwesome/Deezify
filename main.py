import json
import funcs


class config:
    class spotify:
        user = ""                   # your spotify username
        playlist_name = "Deezify"   # spotify playlist name
        description = "test"        # spotify playlist description
        token = ""                  # spotify bearer token
    class deezer:
        playlist = ""               # deezer playlist id


Spotify = funcs.Spotify(config.spotify.token)
Deezer = funcs.Deezer(config.deezer.playlist)

deezer_songs = []
data = ""

while True:
    playlist_resp = Deezer.get_tracks(data=data).json()
    tracks = playlist_resp["data"]

    for track in tracks:
        print("[DEEZER] Found: " + track["title"] + " by " + track["artist"]["name"])
        deezer_songs.append([track["title"], track["artist"]["name"]])

    try:
        data = playlist_resp["next"].split("?")[1]
    except KeyError:
        break




print(deezer_songs)
spotify_tracks, errors = Spotify.convert_tracks(deezer_songs)
print(spotify_tracks)

create_resp = Spotify.create_playlist(config.spotify.playlist_name, config.spotify.description)

print(create_resp.text, create_resp)
print(Spotify.add_tracks(spotify_tracks, json.loads(create_resp.text)["href"]))

print("ERROR TRACKS: " + str(errors))


