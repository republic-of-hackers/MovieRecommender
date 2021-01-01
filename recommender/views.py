from django.shortcuts import render
import pickle
from .recommender import get_recommended_movies_for_user

movies_df = pickle.load(open('./recommender/datafiles/movies.dat', 'rb'))

def index(request):
	movies_df1 = movies_df[:9066]
	movies_title = list(movies_df1['title'])
	context = {
		'title' : movies_title
	}
	return render(request, 'recommmender/index.html', context)

def recommend(request):
	movies1 = request.POST['movie1']
	liked_movieId = get_movieId(movies1)
	predicted_movies = get_recommended_movies_for_user(liked_movies_id=liked_movieId)
	context = {
		'movies' : predicted_movies
	}
	return render(request, 'recommmender/recommend.html', context)

def get_movieId(movie):
	df = movies_df[movies_df['title'] == movie]
	id = int(df['movieId'])
	return id