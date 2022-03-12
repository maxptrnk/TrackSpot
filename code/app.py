from flask import Flask, render_template, url_for, redirect, request, session
from sqlalchemy import JSON
from authorization import *
from spotifyclient import *
from collections import Counter
from dataclient import *

import time







app = Flask(__name__)
app.secret_key = "YOUR SECRET KEY"

oauth_client = SpotifyOauthClient()

# data_client = None

global data_client
global artist_per_genre




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
    session['artists_per_genre']= {}


    
    



    # data_client------------------------------------------------------------------------------------------
    api_client = init_api_client()
    request_data = api_client.get_user_info()

    session['username'] = request_data["user_info"]["display_name"]


    
    # data_client------------------------------------------------------------------------------------------
    user_top_songs = api_client.get_user_top_info(50, session.get('time_frame'), "tracks")
    user_top_artists = api_client.get_user_top_info(50, session.get('time_frame'), "artists")

    if not user_top_songs or not user_top_artists: 
        return "error"
    else:
        song_ids = user_top_songs['id']
        artist_ids = user_top_artists['id']

    
    # print('mpmpmpmppmppmpmmpmpmpmpppmpmpmpmmpmpmpmpmpmpmp')
    # print(data_client.__dict__)

    global data_client
    data_client = DataClient(api_client, song_ids, artist_ids)

    global artist_per_genre
    artist_per_genre = {}
    

    # print(data_client.__dict__)
    # data_client------------------------------------------------------------------------------------------

    return redirect(url_for('myhomepage', _external=True))
   




@app.route('/moregenres')
def genres():   


    # dic avec toutes les occurences pour chaque genres 
    user_top_genres = data_client.get_user_top_genres()

    # selection des genres le plus populaire de l'utilisateur
    top_genres = dict(Counter(user_top_genres).most_common(5)) 

    # calcule des pourcentages
    list_pourcentage_top = []
    pourcentage_reste =100

    for c in top_genres:
        pourcentage_relatif = round((top_genres[c]/sum(top_genres.values()))*100, 2)
        list_pourcentage_top.append(str(pourcentage_relatif)    +'%')
        pourcentage_reste -= top_genres[c]

    # tous ceux qui ne sont pas dans le top : compteur+1, nom ajouter ajouté dans une liste et les top_genres
    list_top_genres_keys = list(top_genres.keys())
    list_top_genres_values = list(top_genres.values())


    no_top_genres = top_genres.copy()
    no_top_genres_compteur = 0
    other_genres_listened = []

    for genre in user_top_genres :
        if genre not in list(top_genres):
            no_top_genres_compteur +=1
            other_genres_listened.append(genre)

    # dict for doughnut graph with top genre, other and their proportion
    no_top_genres['others'] = no_top_genres_compteur   



    # --------------------------------------------------------------

    # f = open("static/minor_genres.txt", "a")
    # f.write(key)
    # f.close()


    # TXT_FILE = Path.cwd() / "minor_genres.txt"

    # # Read text
    # text = open(TXT_FILE, mode="r", encoding="utf-8").read()


    # wc = WordCloud(background_color="black", height=350, width=600,min_font_size=14, max_font_size=55, font_step=0)
    # wc.generate(text)

    # # store to file
    # wc.to_file("wordcloud_output.png")

    # --------------------------------------------------------------

    # wc = WordCloud(background_color="black", height=350, width=600,min_font_size=14, max_font_size=55, font_step=0)

    # wc.generate(key)
    # print('okokokokokokookokokokok2')

    # # store to file
    # wc.to_file("static/photos/wordcloud_output.png")

    # --------------------------------------------------------------


    

    return render_template('moregenres.html',username=session['username'], zip=zip,other_genres_listened=other_genres_listened,pourcentage_reste=pourcentage_reste,list_pourcentage_top=list_pourcentage_top, list_top_genres_values=list_top_genres_values, list_top_genres_keys=list_top_genres_keys)


@app.route('/moregraphs')
def graphs():
    api_client = init_api_client()
    # #genres
    # user_top_songs = api_client.get_user_top_info(50, session.get('time_frame'), "tracks")
    # user_top_artists = api_client.get_user_top_info(33, session.get('time_frame'), "artists")

    # if not user_top_songs or not user_top_artists: #if the user has no data (i.e the returned dict is empty)
    #     return 'error'
    #     # return error_page("Sorry, your account does not seem to have any data I can analyze. Please go back to the 'My Music' section and try switching the timeframe to see if you have any data there!")

    # else:
    #     song_ids = user_top_songs['id']
    #     artist_ids = user_top_artists['id']

    # data_client = DataClient(api_client, song_ids, artist_ids, session.get('time_frame'))



    #audio features info
    cols = ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Valence', 'Instrumentalness']
    user_avg_features = data_client.get_user_top_avg_audio_features(cols)
    top_avg_features = data_client.get_spotify_charts_avg_features(cols)  #audio features info

    # graph group bar, audio features evolution

    # init with short_term because already stored
    audio_features_evolution = [data_client.get_user_top_avg_audio_features(cols)]
    for time in ['medium_term','long_term']:
        user_top_songs = api_client.get_user_top_info(50, time, "tracks")
        user_top_artists = api_client.get_user_top_info(5, time, "artists")

        if not user_top_songs or not user_top_artists: #if the user has no data (i.e the returned dict is empty)
            user_top_songs = api_client.get_user_top_info(50, time, "tracks")
            user_top_artists = api_client.get_user_top_info(5, time, "artists")
            
            # return 'error'
            # return error_page("Sorry, your account does not seem to have any data I can analyze. Please go back to the 'My Music' section and try switching the timeframe to see if you have any data there!")

        # else:
        #     song_ids = user_top_songs['id']
        #     artist_ids = user_top_artists['id']

        if not user_top_songs or not user_top_artists: #if the user has no data (i.e the returned dict is empty)
            song_ids = user_top_songs['id']
            artist_ids = user_top_artists['id']
        else:
            song_ids = user_top_songs['id']
            artist_ids = user_top_artists['id']

        data_client_mid_long = DataClient(api_client, song_ids, artist_ids)
        user_avg_features= data_client_mid_long.get_user_top_avg_audio_features(cols)
        audio_features_evolution.append(user_avg_features)
        
    return render_template('moregraphs.html',username=session['username'],user_avg_features_recent=audio_features_evolution[0], user_avg_features_mid=audio_features_evolution[1],user_avg_features_long=audio_features_evolution[2], user_avg_features=user_avg_features, top_avg_features=top_avg_features )



@app.route("/test")
def testgraph():
    # api_client = init_api_client()
    # time_frame = session.get('time_frame')

    # #genres
    # user_top_songs = api_client.get_user_top_info(50, session.get('time_frame'), "tracks")
    # user_top_artists = api_client.get_user_top_info(33, session.get('time_frame'), "artists")

    # if not user_top_songs or not user_top_artists: #if the user has no data (i.e the returned dict is empty)
    #     return 'error'
    #     # return error_page("Sorry, your account does not seem to have any data I can analyze. Please go back to the 'My Music' section and try switching the timeframe to see if you have any data there!")

    # else:
    #     song_ids = user_top_songs['id']
    #     artist_ids = user_top_artists['id']
    # data_client = DataClient(api_client, song_ids, artist_ids, session.get('time_frame'))


    #audio features info
    cols = ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Valence', 'Instrumentalness']
    user_avg_features = data_client.get_user_top_avg_audio_features(cols)
    spotify_avg_features = data_client.get_spotify_charts_avg_features(cols)  #audio features info

    return render_template('testgraph.html',user_avg_features=user_avg_features, top_avg_features=spotify_avg_features)

@app.route("/index")
def myhomepage():

    try:
        data_client
    except NameError:
         return redirect(url_for('index', _external=True))

    api_client = init_api_client()
    time_frame = session.get('time_frame')

    # dic avec toutes les occurences pour chaque genres 
    user_top_genres = data_client.get_user_top_genres()
    # selection des genres le plus populaire de l'utilisateur
    top_genres = dict(Counter(user_top_genres).most_common(5)) 
    # get link to playlist suggested by genre
    playlists_uris =  api_client.get_playlist_to_genre(top_genres)
    # Top 5 genre (sans valeurs)
    top_genres = list(top_genres)

    # Tracks and artists
    user_top_tracks = api_client.get_user_top_info(5, time_frame, "tracks")
    user_top_artists_short = api_client.get_user_top_info(50, time_frame, "artists")

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

    if not user_top_artists_short:
        artists = ['']
        artist_ids = ['']
        artist_covers = ['']
    
    else:
        artists = user_top_artists_short['name']
        artist_ids = user_top_artists_short['id']
        artist_covers = user_top_artists_short['image']

        global artist_per_genre

        if artist_per_genre == {}:     
            artist_per_genre[top_genres[0]] = {}
            artist_per_genre[top_genres[1]] = {}
            artist_per_genre[top_genres[2]] = {}
            artist_per_genre[top_genres[3]] = {}
            artist_per_genre[top_genres[4]] = {}

            if artist_per_genre[top_genres[0]] == {} and artist_per_genre[top_genres[1]] == {} and artist_per_genre[top_genres[2]] == {} and artist_per_genre[top_genres[3]] == {} and artist_per_genre[top_genres[0]] == {}:            
                for artist in user_top_artists_short['id'] :

                    artist_info = api_client.get_track_or_artist_info(artist, "artists")

                    # print(artist_info['genres'])
                    # print("____________________________________________________________________________________________________________")           

                    if top_genres[0] in artist_info['genres']:
                        artist_per_genre[top_genres[0]][artist]= artist_info['image']
                    if top_genres[1] in artist_info['genres']:
                        artist_per_genre[top_genres[1]][artist]= artist_info['image']
                    if top_genres[2] in artist_info['genres']:
                        artist_per_genre[top_genres[2]][artist]= artist_info['image']
                    if top_genres[3] in artist_info['genres']:
                        artist_per_genre[top_genres[3]][artist]= artist_info['image']
                    if top_genres[4] in artist_info['genres']:
                        artist_per_genre[top_genres[4]][artist]= artist_info['image']




        # if session['artists_per_genre'] == {}:
        #     # artists_genres = []
        #     session['artists_per_genre']

        #     #  une boucle avec des if pour chaque 

        #     session['artists_per_genre'][top_genres[0]] = {}
        #     session['artists_per_genre'][top_genres[1]] = {}
        #     session['artists_per_genre'][top_genres[2]] = {}
        #     session['artists_per_genre'][top_genres[3]] = {}
        #     session['artists_per_genre'][top_genres[4]] = {}

            

        #     print('___________________________________________________565665558787')
        #     print(session['artists_per_genre'][top_genres[0]])

        #     if session['artists_per_genre'][top_genres[0]] == {} and session['artists_per_genre'][top_genres[1]] == {} and session['artists_per_genre'][top_genres[2]] == {} and session['artists_per_genre'][top_genres[3]] == {} and session['artists_per_genre'][top_genres[0]] == {}:
            
        #     # if session['artists_per_genre'][top_genres] == [{},{},{},{},{}]:
        #         for artist in user_top_artists_short['id'] :

        #             artist_info = api_client.get_track_or_artist_info(artist, "artists")
        #             # artists_genres.append(artist_info['genres'])

        #             # print(artist_info['genres'])
        #             # print("____________________________________________________________________________________________________________")           

        #             if top_genres[0] in artist_info['genres']:
        #                 session['artists_per_genre'][top_genres[0]][artist]= artist_info['image']
        #             if top_genres[1] in artist_info['genres']:
        #                 session['artists_per_genre'][top_genres[1]][artist]= artist_info['image']
        #             if top_genres[2] in artist_info['genres']:
        #                 session['artists_per_genre'][top_genres[2]][artist]= artist_info['image']
        #             if top_genres[3] in artist_info['genres']:
        #                 session['artists_per_genre'][top_genres[3]][artist]= artist_info['image']
        #             if top_genres[4] in artist_info['genres']:
        #                 session['artists_per_genre'][top_genres[4]][artist]= artist_info['image']

        #             # print('___________________________________________________5657')
        #             # print(session['artists_per_genre'][top_genres[0]])







                # print("french hip hop")
                # print(len(artists_per_genre[top_genres[0]]))
                # print("pop urbaine")
                # print(len(artists_per_genre[top_genres[1]]))
                # print("russian hip hop")
                # print(len(artists_per_genre[top_genres[2]]))
                # print("orchestral soundtrack")
                # print(len(artists_per_genre[top_genres[3]]))
                # print("soundtrack")
                # print(len(artists_per_genre[top_genres[4]]))
                

            #     print("_______________________________")
            # print(artists_per_genre)

                # structure du dict : artists_per_genre ={
                #                     genre0:{arstist:image,arstist:image,arstist:image},
                #                     genre1:{arstist:image,arstist:image,arstist:image},
                #                     genre2:{arstist:image,arstist:image,arstist:image},
                #                     genre3:{arstist:image,arstist:image,arstist:image},
                #                     genre4:{arstist:image,arstist:image,arstist:image} }    

    return render_template('Mindex.html',username=session['username'],artists_per_genre=artist_per_genre, playlists_uris=playlists_uris, genres=top_genres, songs=songs, song_ids=song_ids, song_covers=song_covers, song_artists=song_artists, song_albums=song_albums, artists=artists, artist_ids=artist_ids, artist_covers=artist_covers, zip=zip, time=time_frame)

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

            user_id = api_client.get_user_info()['user_info']['id']
            playlist_name = "My Top 50 tracks - TrackSpot"

            get_new_playlist_id = api_client.create_new_playlist(user_id, playlist_name)['id']
            modified_ids = ["spotify:track:" + track_id for track_id in song_ids]
            csv_ids = ','.join(modified_ids)
           
            api_client.add_items_to_playlist(get_new_playlist_id, csv_ids)


    return render_template('Mmoretracks.html',username=session['username'], songs=songs, song_ids=song_ids, song_covers=song_covers, song_artists=song_artists, song_albums=song_albums, zip=zip, time=time_frame)

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
        # print(artist_ids)

        artist_ids_clean = '' 
        for artist_id in artist_ids:
            artist_ids_clean = artist_ids_clean +','+ artist_id

        artist_ids_clean = artist_ids_clean[1:]

        artists_followers = api_client.get_multiple_track_or_artist_info("artists",artist_ids_clean,"followers")


        artists_genres = api_client.get_multiple_track_or_artist_info("artists",artist_ids_clean,"genres")
        artists_pop = api_client.get_multiple_track_or_artist_info("artists",artist_ids_clean,"popularity")

   

        # artists_followers = []
        # # artists_genres = []
        # # artists_pop = []

        # for artist in artist_ids :
        #       artist_info = api_client.get_track_or_artist_info(artist, "artists")
        #       artists_followers.append(f"{artist_info['followers']:,d}")
        #     #   print('_________________________________________333______________________________________________________')
        # #      print(type(artist_info['followers']))
        #     #   print((f"{artist_info['followers']:,d}"))
        #     #  artists_genres.append(artist_info['genres']))
        # #     artists_pop.append(artist_info['popularity'])
        # print('_________________________________________333______________________________________________________')
        # print(artists_followers)

    
    return render_template('Mmoreartists.html',username=session['username'], f=artists_followers, g=artists_genres, p=artists_pop, artists=artists, artist_ids=artist_ids, artist_covers=artist_covers, zip=zip, time=time_frame)

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