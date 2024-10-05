import pandas as pd
import pickle
movies = pd.read_csv("Book2.csv")
print(movies)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=100, stop_words='english')
vector = cv.fit_transform(movies['tag']).toarray()
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vector)
print(similarity)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    mov_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    for i in mov_list:
        print(movies.iloc[i[0]].title)
print("*************************************")
recommend("KGF: Chapter 1")       
print("*************************************")
recommend("Elemental")
print("*************************************")

pickle.dump(movies, open('mov_dict.pkl','wb'))
pickle.dump(similarity, open('similarity_dict.pkl','wb'))
