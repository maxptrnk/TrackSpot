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
        Find via an api call a playlist on spotify correspoding to each given genre 

        Parameters:
        genres: contains the 5 names of the user's favorite music genres (list of string)

        Return:
        playlists_uris: links to spotify playlists (list of string)
        """

        # get genre

        playlists_uris = []
        for genre in genres:
            encoded_genre = genre.replace(' ', '%20')
            playlist_url = self.API_BASE_URL + "/search?q=playlist:"+encoded_genre+"&type=playlist&limit=1"
            playlist_get = requests.get(playlist_url, headers=self.auth_playlist)
            playlists_data = json.loads(playlist_get.text)

            # if playlist corresponding to the particular genre not found, replace by Top global playlist
            if playlists_data['playlists']['items'] == []:
                playlists_data['playlists']['items'].append({'id':'37i9dQZEVXbMDoHDwVN2tF'})
                
            playlists_uris.append(playlists_data['playlists']['items'][0]['id'])

        return playlists_uris



    def get_user_info(self):
        """
        Resquest information about the user 

        Return:
        user_info : Get detailed profile information about the current user (dic)
        """

        output_dict = lambda **data: data #to format the returned data nicely and readable
        user_info_get = requests.get(f"{self.API_BASE_URL}/me", headers=self.auth_body)
        user_info_data = json.loads(user_info_get.text)
        return output_dict(user_info=user_info_data)


    def get_user_top_info(self, limit, time_range, top_type):
        """
        Resquest information about the user's top artists or tracks

        Parameters:
        limit: number of elements requested (int)
        time_range: period to which correspond elements requested (str)
        top_type: type of elements requested artists or tracks (str)

        Return:
        data_client : (dic)
        """

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
        """
        

        Parameters:
        type_id: 
        info_type:

        Return:
        output_dict: 
        """

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
        """
        

        Parameters:
        type_ids: 
        info_type:
        feature:

        Return:
        all_info: 
        """

        url = self.API_BASE_URL + f"/{info_type}?ids={type_ids}"
        get = requests.get(url, headers=self.auth_body)
        data = retry_call(json.loads, fargs=[get.text])

        if feature == "followers":
            all_info = []
            for info in data[info_type]:
                # print('22999_____________________________________________________-')
                all_info.append(f"{info[feature]['total']:,d}")


        else:
            all_info = [info[feature] for info in data[info_type]]

        
        return all_info

    def create_new_playlist(self, user_id, name):
        """
        

        Parameters:
        user_id:
        name:

        Return:
        data: 
        """
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
        """
        

        Parameters:
        playlist_id:
        csv_ids:
         
        """
        url = self.API_BASE_URL + f"/playlists/{playlist_id}/tracks?uris={csv_ids}"
        post = requests.post(url, headers=self.auth_body)
    
    def get_audio_features_for_multiple_songs(self, ids):
        """
        

        Parameters:
        ids:

        Return:
        all_features: 
        """
        url = self.API_BASE_URL + f"/audio-features?ids={ids}"
        get = requests.get(url, headers=self.auth_body)
        data = retry_call(json.loads, fargs=[get.text])
        all_features = []

        for audio in data['audio_features']:
            features = [audio['danceability'], audio['energy'], audio['acousticness'],
                        audio['speechiness'], audio['valence'], audio['instrumentalness']]
            all_features.append(features)
        return all_features