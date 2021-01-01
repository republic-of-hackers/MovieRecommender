import pickle
import numpy as np
import pandas as pd

def get_recommended_movies_for_user(liked_movies_id):
    movies = []
    movies_df = pickle.load(open('./recommender/datafiles/movies.dat', 'rb'))
    M = pickle.load(open("./recommender/datafiles/movie_features.dat", "rb"))
    M = np.transpose(M)
    movies_df = pd.DataFrame(movies_df[:9066])

    id = liked_movies_id
    current_movie_features = M[id - 1]
    difference = M - current_movie_features
    absolute_difference = np.abs(difference)
    total_difference = np.sum(absolute_difference, axis=1)
    movies_df['difference_score'] = total_difference
    sorted_movie_list = movies_df.sort_values('difference_score')

    similer_movies_df = pd.DataFrame(sorted_movie_list[['title','genres']][1:11])

    titles = list(similer_movies_df.title)
    genres = list(similer_movies_df.genres)

    for i in range(10):
        movie_info = str('Title: ' + titles[i] + '      Genres: ' + genres[i])
        movies.append(movie_info)

    return movies