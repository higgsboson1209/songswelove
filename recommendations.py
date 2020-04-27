import pandas as pd
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
path=#use the location to upload the dataset
finaldf = pd.read_csv(path)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
x = list(zip(finaldf.Negative.tolist(),finaldf.Neutral.tolist(),finaldf.Positive.tolist()))
y=finaldf.Song.tolist()
def closedouput(n,usersentimentvalues):
  recommend = KNeighborsClassifier(n_neighbors = n, p = 1)
  recommend.fit(x,y)
  predict=recommend.kneighbors([usersentimentvalues])
  return predict
def scores(inp):
    score = analyser.polarity_scores(inp)
    m=[]
    for i in score:
      m.append(int(score[i]))
    print(score)
    return m
print("Welcome to the song recommender system \n")
inp=input("Please enter how you feel today \n")
usersentimentvalues=scores(inp)
answer=closedouput(10,[usersentimentvalues[0],usersentimentvalues[1],usersentimentvalues[2]])
#10 because i find the 10 nearest neighbours
for x in np.nditer(answer[1]):
  print(y[x])
