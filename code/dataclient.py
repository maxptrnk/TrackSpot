import pandas as pd
from collections import Counter

class DataClient():

    def __init__(self, api_client, song_ids, artist_ids):
        self.api_client = api_client
        
        self.spotify_dataset = pd.read_csv('static/assets/csv/spotifytoptracks.csv')
        self.api_client = api_client

        self.ids = {
            "artists": (artist_ids),
            "tracks": (song_ids) 
        }
        self.csv_ids = {
            "artists": ','.join(self.ids['artists']),
            "tracks": ','.join(self.ids['tracks'])
        }

    def get_user_top_genres(self):
        
        user_genres = {}
        
        top_artist_genres = self.api_client.get_multiple_track_or_artist_info("artists", self.csv_ids['artists'], "genres")

        # print('4324_____________________________________________________-')
        # print(top_artist_genres)

        for artist_genres in top_artist_genres:

            for genre in artist_genres:
                
                if genre in user_genres:
                    user_genres[genre] += 1
                    
                else:
                    user_genres[genre] = 1


        # top_genres = dict(Counter(user_genres).most_common(5)) 
        # return (list(top_genres))
        return user_genres
    


        
    def get_user_top_avg_audio_features(self, columns):

            try:
                features_list = self.api_client.get_audio_features_for_multiple_songs(self.csv_ids['tracks'])
        
            except:
                features_list = retry_call(self.api_client.get_audio_features_for_multiple_songs, fargs=[self.csv_ids['tracks']]) #keeps retrying the request to prevent user from getting 500 errors

            data_table = pd.DataFrame(features_list, columns=columns)
            avg_value_list = [round(data_table[col].mean(), 4) for col in columns]

            return avg_value_list

    def get_spotify_charts_avg_features(self, columns):
            
            avg_value_list = [round(self.spotify_dataset[col.lower()].mean(), 4) for col in columns]

            return avg_value_list


def get_user_top_data(data):

    df = pd.DataFrame(data.values())
    return df.to_dict("list")

    