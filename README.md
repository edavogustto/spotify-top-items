# Spotify Top Tracks and Artists

Spotify console app to list top tracks, artists and create a playlist.


------------

## Setup:
1. Create an app in [Spotify developer API](https://developer.spotify.com/dashboard/login "Spotify developer API")
![](https://i.imgur.com/HPWIZWn.png)
2. Add a name and a description

![](https://i.imgur.com/5DixrMg.png)

3. Set the redirect url to "http://localhost:8080" (if you are going to use the terminal)
![](https://i.imgur.com/H5ExtSJ.png)
![](https://i.imgur.com/sS1EEzs.png)
4. Copy the Client ID, Client secret and the Redirect Url to the .env file.

`SPOTIPY_CLIENT_ID = YourClientID
SPOTIPY_CLIENT_SECRET = YourClientSecret
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'`

## Usage
Clone the repo:
`git clone $REPO_URL /path/to/local/directory`

Install dependencies:
`pip install -r requirements.txt`

Run Program:
`python3 main.py`

------------

### Documentations and tutorials referenced:
- https://www.youtube.com/watch?v=nBfbkp7A8a4
- https://spotipy.readthedocs.io
- https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-top-artists-and-tracks
- https://developer.spotify.com/documentation/general/guides/authorization/scopes/

