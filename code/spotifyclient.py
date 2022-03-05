import requests, json
from dataclient import *
from retry.api import retry_call



class SpotifyApiClient():

    def __init__(self, access_token):

        self.API_BASE_URL = "https://api.spotify.com/v1"
        self.auth_body = {
            "Authorization" : f"Bearer {access_token}"
        }
        self.auth_playlist = {
            
            "Authorization" : f"Bearer {access_token}",
            "Content-Type" : "application/json"
            
        }



    def get_playlist_to_genre(self,genres):

        """
        Find playlists on spotify via an api call for each given genre 

        Parameters:
        genres : 

        Return:
        playlists_uris: 
        """


        # get genre

        playlists_uris = []
        for genre in genres:

            # à la place d'un espace mette : %20

            encoded_genre = genre.replace(' ', '%20')

            

        
            playlist_url = self.API_BASE_URL + "/search?q=playlist:"+encoded_genre+"&type=playlist&limit=1"
            
            playlist_get = requests.get(playlist_url, headers=self.auth_playlist)
            playlists_data = json.loads(playlist_get.text)

            playlists_uris.append(playlists_data['playlists']['items'][0]['id'])



        return playlists_uris



    def get_user_info(self):

        output_dict = lambda **data: data #to format the returned data nicely and readable

        # playlist_url = self.API_BASE_URL + "/me/playlists"

        playlist_url = self.API_BASE_URL + "/me/playlists?offset=0&limit=50"
        followed_artist_url = self.API_BASE_URL + "/me/following?type=artist&limit=50"
        shows_url = self.API_BASE_URL + "/shows"

        # offset=0
        # while no error do:
        #     playlist_url = self.API_BASE_URL + "/me/playlists?offset="+str(offset)+"&limit=50"
        #     playlist_get = requests.get(playlist_url, headers=self.auth_body)
        #     playlists_data = json.loads(playlist_get.text)

        #     offset +=50


        



        user_info_get = requests.get(f"{self.API_BASE_URL}/me", headers=self.auth_body)
        playlist_get = requests.get(playlist_url, headers=self.auth_body)
        followed_artists_get = requests.get(followed_artist_url, headers=self.auth_body)
        shows_get = requests.get(shows_url, headers=self.auth_body)

        user_info_data = json.loads(user_info_get.text)
        playlists_data = json.loads(playlist_get.text)
        followed_artists_data = json.loads(followed_artists_get.text)
        shows_data = json.loads(shows_get.text)

        


        return output_dict(user_info=user_info_data, playlist_info=playlists_data, following_info=followed_artists_data, podcasts=shows_data)

    def get_user_top_info(self, limit, time_range, top_type):

        url = self.API_BASE_URL + f"/me/top/{top_type}?time_range={time_range}&limit={limit}"
        get = requests.get(url, headers=self.auth_body)
        data = retry_call(json.loads, fargs=[get.text]) #resends request if failure; avoids 500+ errors


        data_dict = {}

        if limit > len(data['items']): #incase the user does not have as many songs as the limit
            list_limit = len(data['items'])

        else:
            list_limit = limit

        for i in range(list_limit):

            data_dict[i] = {}
            data_dict[i]['name'] = data['items'][i]["name"] #artist/track name
            data_dict[i]['id'] = data['items'][i]["id"] #artist/track id

            if top_type == "tracks":
                data_dict[i]["image"] = data['items'][i]["album"]["images"][1]["url"]  #track cover image
                data_dict[i]["trackartistname"] = data['items'][i]["album"]['artists'][0]['name'] #artist who released track
                data_dict[i]["trackalbumname"] = data['items'][i]["album"]['name'] #album the track is in
            
            else:
                data_dict[i]['image'] = data['items'][i]["images"][1]["url"] #artist cover image

        return get_user_top_data(data_dict)

    def get_track_or_artist_info(self, type_id, info_type):

        output_dict = lambda **data: data

        url = self.API_BASE_URL + f"/{info_type}/{type_id}"
        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)

        popularity = data['popularity']
        name = data['name']

        if info_type == "artists":
            followers = data['followers']['total']
            genres = data['genres']
            image = data['images'][2]['url']
            return output_dict(followers=followers, genres=genres, name=name, image=image, popularity=popularity)
        
        else:
            artist_name = data['artists'][0]['name']
            return output_dict(name=name, artist=artist_name, popularity=popularity)

    def get_multiple_track_or_artist_info(self, info_type, type_ids, feature):

        url = self.API_BASE_URL + f"/{info_type}?ids={type_ids}"
        get = requests.get(url, headers=self.auth_body)
        data = retry_call(json.loads, fargs=[get.text])
        all_info = [info[feature] for info in data[info_type]]

        # print('431224_____________________________________________________-')
        # print(all_info)


        
        return all_info

    def create_new_playlist(self, user_id, name):

        url = self.API_BASE_URL + f"/users/{user_id}/playlists"

        request_body = {
            "name": name,
            "description": "Your customized recommendations from Diversify!",
            "public": False
        }

        post = requests.post(url, headers=self.auth_body, json=request_body)
        data = json.loads(post.text)

        return data

    def add_items_to_playlist(self, playlist_id, csv_ids):

        url = self.API_BASE_URL + f"/playlists/{playlist_id}/tracks?uris={csv_ids}"
        post = requests.post(url, headers=self.auth_body)
    
    def get_audio_features_for_multiple_songs(self, ids):

        url = self.API_BASE_URL + f"/audio-features?ids={ids}"
        get = requests.get(url, headers=self.auth_body)
        data = retry_call(json.loads, fargs=[get.text])
        all_features = []

        for audio in data['audio_features']:

            features = [audio['danceability'], audio['energy'], audio['acousticness'],
                        audio['speechiness'], audio['valence'], audio['instrumentalness']]

            all_features.append(features)
        
        print("audio features==============================================================================")
        print(all_features)

        return all_features