import pandas as pd
from collections import Counter

class DataClient():

    def __init__(self, api_client, song_ids, artist_ids, time_frame):
        
        self.api_client = api_client
        self.spotify_dataset = pd.read_csv('static/csv/spotifytoptracks.csv')
        self.ids = {
            "artists": (artist_ids),
            "tracks": (song_ids) 
        }
        self.csv_ids = {
            "artists": ','.join(self.ids['artists']),
            "tracks": ','.join(self.ids['tracks'])
        }

    def get_user_top_genres(self):
        
        genres = {}
        
        top_artist_genres = self.api_client.get_multiple_track_or_artist_info("artists", self.csv_ids['artists'], "genres")

        for artist_genres in top_artist_genres:

            for genre in artist_genres:
                
                if genre in genres.keys():
                    genres[genre] += 1
                    
                else:
                    genres[genre] = 1

        top_genres = dict(Counter(genres).most_common(5)) 

        

        return (list(top_genres))


def get_user_top_data(data):

    df = pd.DataFrame(data.values())
    return df.to_dict("list")