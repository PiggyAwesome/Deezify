# Deezify
 Convert a Deezer playlist to a Spotify playlist




#### For this application, you will need 5 different config values.
#### config is inside main.py

## Config index:
- [Value 1:](https://github.com/PiggyAwesome/Deezify/#value-1-token)
     - [Value 1.1:](https://github.com/PiggyAwesome/Deezify/#11)
     - [Value 1.2:](https://github.com/PiggyAwesome/Deezify/#12)
     - [Value 1.3:](https://github.com/PiggyAwesome/Deezify/#13)
- [Value 2:](https://github.com/PiggyAwesome/Deezify/#value-2-playlist_name)
- [Value 3:](https://github.com/PiggyAwesome/Deezify/#value-3-description)
- [Value 4:](https://github.com/PiggyAwesome/Deezify/#value-4-user)
- [Value 5:](https://github.com/PiggyAwesome/Deezify/#value-5-playlist)
     - [Value 5.1:](https://github.com/PiggyAwesome/Deezify/#51)
     - [Value 5.2:](https://github.com/PiggyAwesome/Deezify/#52)
     - [Value 5.3:](https://github.com/PiggyAwesome/Deezify/#53)

### Value 1: `token`
#### 1.1
log into Spotify and go to [this website](https://developer.spotify.com/console/get-current-user/)
 
#### 1.2
copy the text that is circled in this image (the part after bearer)

 ![Untitled](https://user-images.githubusercontent.com/48888771/184538134-06a057e2-34b1-41a6-b4cd-1ddd348786d2.png)
#### 1.3
paste this into the `config.spotify.token` field


### Value 2: `playlist_name`
Enter the name of the Spotify playlist that will be created here.

### Value 3: `description`
Enter the description of the Spotify playlist that will be created here.

### Value 4: `user`
Enter your spotify username here.

### Value 5: `playlist`
#### 5.1
Open your Deezer playlist in a browser.

#### 5.2
Copy the the numbers in the url after "https://www.deezer.com/en/playlist/" (see image)

![image](https://user-images.githubusercontent.com/48888771/184541616-d3ab5099-3c9c-4960-98a3-a9255c3b347c.png)

#### 5.3
paste this into the `config.deezer.playlist` field
