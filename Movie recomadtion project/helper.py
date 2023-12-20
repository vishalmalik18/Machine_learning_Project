from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import difflib


def Movies(movie_name):
    df1 = pd.read_csv("Movies.csv")
    selected_features = ['genres','tagline','keywords','cast','director']
    for feature in selected_features:
        df1[feature] = df1[feature].fillna('')

    combinded_features = df1['genres']+' '+df1['keywords']+' '+df1['tagline']+' '+df1['cast']+' '+df1['director']
    
    vectorizer = TfidfVectorizer()

    feature_vectors = vectorizer.fit_transform(combinded_features)

    similarity = cosine_similarity(feature_vectors)

    list_of_all_titles = df1['title'].tolist()

    find_the_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)

    close_match = find_the_close_match[0]

    find_the_index_of_the_movie = df1[df1.title==close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[find_the_index_of_the_movie]))

    sorted_similar_movies = sorted(similarity_score,key=lambda x:x[1],reverse=True)
    
    result = []

    i = 1

    for movie in sorted_similar_movies:
        index = movie[0]

        title_from_index = df1[df1.index==index]['title'].values[0]
        if (i<=20):
            result.append((i,title_from_index))
            i+=1
        
    return result

if __name__ == '__main__':
    Movies(movie_name='Avtar')
































