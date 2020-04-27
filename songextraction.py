#This is how we have created the dataset that finds all the top billboard songs 
pip install lyricsgenius
pip install textblob
import lyricsgenius as lg
import pandas as pd
import numpy as np
genius = lg.Genius('#generate your token on the genius website ')
hot100_df = pd.read_csv('https://query.data.world/s/qf6et5c7dh23kglnvjcoztlmom62it')
#get top songs only from the last 10 years
hot101=hot100_df[hot100_df["WeekID"].str.contains("201")]
#sort them
hot101.sort_values(["WeekID","Week Position"],inplace=True)
#drop things we wont use
hot101.drop(["url","WeekID","SongID","Instance","Previous Week Position","Peak Position","Weeks on Chart","Week Position"],inplace=True,axis=1)
#removing the duplicate songs since lot of songs retain their positions in subsequent weeks
hot101.drop_duplicates(inplace=True)
#extracting the lyrics of each song for which the lyrics can be found
def get_lyrics(title,artist):
  try:
    return genius.search_song(title, artist).lyrics
  except:
    return 0
lyrics=hot101.apply(lambda row: get_lyrics(row['Song'], row['Performer']), axis =1)
hot101["Lyrics"]=lyrics
#in case you plan to do this on google colab here are the additional steps to stor this dataset in your drive
from google.colab import drive
drive.mount('drive')
hot101.to_csv('data.csv')
!cp data.csv "drive/My Drive/"
