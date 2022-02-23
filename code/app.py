from flask import Flask, render_template, url_for, redirect, request, session
from sqlalchemy import JSON
from authorization import *
from spotifyclient import *

import time


app = Flask(__name__)
app.secret_key = "YOUR SECRET KEY"

oauth_client = SpotifyOauthClient()

@app.route('/')
def index():
    auth_url = oauth_client.get_auth_url()
    return render_template("Mlogin.html", url=auth_url)

@app.route("/redirect/")
def redirectPage():
    auth_code = request.args.get('code')
    auth_info = oauth_client.get_token_info(auth_code)

    session['oauth_info'] = auth_info
    session['start_time'] = int(time.time())
    session['time_frame'] = "short_term"
    # session['cols'] = ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Valence', 'Instrumentalness']

    return redirect(url_for('myhomepage', _external=True))
   


# -------------------------------------------------m
@app.route('/settings')
def mysettings():    
    return render_template('settings.html')



@app.route("/index")
def myhomepage():

    api_client = init_api_client()
    time_frame = session.get('time_frame')



    #genres
    user_top_songs = api_client.get_user_top_info(50, session.get('time_frame'), "tracks")
    user_top_artists = api_client.get_user_top_info(33, session.get('time_frame'), "artists")

    if not user_top_songs or not user_top_artists: #if the user has no data (i.e the returned dict is empty)
        return error_page("Sorry, your account does not seem to have any data I can analyze. Please go back to the 'My Music' section and try switching the timeframe to see if you have any data there!")

    else:
        song_ids = user_top_songs['id']
        artist_ids = user_top_artists['id']

    data_client = DataClient(api_client, song_ids, artist_ids, session.get('time_frame'))

    user_top_genres = data_client.get_user_top_genres()



    # get playlist of top genres

    # playlists_top_genres = []
    # for genre in user_top_genres:
    #     playlists_top_genres.append()



    # Tracks and artists
    user_top_tracks = api_client.get_user_top_info(5, time_frame, "tracks")
    user_top_artists = api_client.get_user_top_info(5, time_frame, "artists")

    if not user_top_tracks: #if the returned data is empty it will set the values to empty
        songs = ['']
        song_ids = ['']
        song_covers = ['']
        song_artists = ['']
        song_albums = ['']
    
    else:
        songs = user_top_tracks['name']
        song_ids = user_top_tracks['id']
        song_covers = user_top_tracks['image']
        song_artists = user_top_tracks['trackartistname']
        song_albums = user_top_tracks['trackalbumname']

    if not user_top_artists:
        artists = ['']
        artist_ids = ['']
        artist_covers = ['']
    
    else:
        artists = user_top_artists['name']
        artist_ids = user_top_artists['id']
        artist_covers = user_top_artists['image']
    
    

    return render_template('Mindex.html', genres=user_top_genres, songs=songs, song_ids=song_ids, song_covers=song_covers, song_artists=song_artists, song_albums=song_albums, artists=artists, artist_ids=artist_ids, artist_covers=artist_covers, zip=zip, time=time_frame)




@app.route('/Mmoretracks', methods=['POST', 'GET'])
def mymoretracks():

    api_client = init_api_client()
    time_frame = session.get('time_frame')
    user_top_tracks = api_client.get_user_top_info(50, time_frame, "tracks")

    if not user_top_tracks: #if the returned data is empty it will set the values to empty
        songs = ['']
        song_ids = ['']
        song_covers = ['']
        song_artists = ['']
        song_albums = ['']
    
    else:
        songs = user_top_tracks['name']
        song_ids = user_top_tracks['id']
        song_covers = user_top_tracks['image']
        song_artists = user_top_tracks['trackartistname']
        song_albums = user_top_tracks['trackalbumname']
    

    
    if request.method == "POST":
            print("--------------------------------------CREATE PLAYYYYYYYYYYYYYYYYYYYLIST------------------------------")

            user_id = api_client.get_user_info()['user_info']['id']
            playlist_name = "My Top 50 tracks - TrackSpot"

            get_new_playlist_id = api_client.create_new_playlist(user_id, playlist_name)['id']
            modified_ids = ["spotify:track:" + track_id for track_id in song_ids]
            csv_ids = ','.join(modified_ids)
            print("---------------------------------------:////////////////////////////>-------------------------------")
            print(modified_ids)

            api_client.add_items_to_playlist(get_new_playlist_id, csv_ids)


    return render_template('Mmoretracks.html', songs=songs, song_ids=song_ids, song_covers=song_covers, song_artists=song_artists, song_albums=song_albums, zip=zip, time=time_frame)



@app.route('/Mmoreartists', methods=['POST', 'GET'])
def mymoreartists():

    # list of ids
    api_client = init_api_client()
    time_frame = session.get('time_frame')
    user_top_artists = api_client.get_user_top_info(50, time_frame, "artists")
        
    if not user_top_artists: 
        artists = ['']
        artist_ids = ['']
        artist_covers = ['']
    
    else:
        artists = user_top_artists['name']
        artist_ids = user_top_artists['id']
        artist_covers = user_top_artists['image']
        artists_followers = []
        artists_genres = []
        artists_pop = []
        for artist in artist_ids :
            artist_info = api_client.get_track_or_artist_info(artist, "artists")
            artists_followers.append(f"{artist_info['followers']:,d}")
            artists_genres.append(artist_info['genres'])
            artists_pop.append(artist_info['popularity'])
    
    if request.method == "POST":
            print("--------------------------------------CREATE PLAYYYYYYYYYYYYYYYYYYYLIST------------------------------")

            user_id = api_client.get_user_info()['user_info']['id']
            playlist_name = "My Top 50 atists - TrackSpot"

            get_new_playlist_id = api_client.create_new_playlist(user_id, playlist_name)['id']
            modified_ids = ["spotify:track:" + track_id for track_id in artist_ids]
            csv_ids = ','.join(modified_ids)
            print("---------------------------------------:////////////////////////////>-------------------------------")
            print(modified_ids)

            api_client.add_items_to_playlist(get_new_playlist_id, csv_ids)

    
    return render_template('Mmoreartists.html', f=artists_followers, g=artists_genres, p=artists_pop, artists=artists, artist_ids=artist_ids, artist_covers=artist_covers, zip=zip, time=time_frame)

    



@app.route('/change-time/<string:id>')
def changeTime(id):
    
    if id[-1] == "M":
        session['time_frame'] = id[:-1]
        return redirect(url_for('mymoreartists', _external=True))
    
    elif id[-1] == "A":
        session['time_frame'] = id[:-1]
        return redirect(url_for('mymoretracks', _external=True))

    else:      
        session['time_frame'] = id
        return redirect(url_for('myhomepage', _external=True, _anchor='#tops'))


def init_api_client(): 
    
    oauth_info = session.get('oauth_info')
    start_time = session.get('start_time') #gets the time at which access_token was first given
    
    current_time = int(time.time()) #gets the time when this function is called
    token_expiry = oauth_info['expires_in']  #sets the token expiry time which is 3600 seconds or 1 hour
    time_diff = current_time - start_time #how much time has passed since token was given

    if time_diff > token_expiry: #if more than an hour has passed, a new access_token will be provided
        new_token = oauth_client.refresh_token(oauth_info['refresh_token'])   #logic for refreshing access token
        start_time = int(time.time())
        return SpotifyApiClient(new_token['access_token'])
    
    else:
        return SpotifyApiClient(oauth_info['access_token'])


if __name__ == "__main__":
    app.run()