import fresh_tomatoes
import movies_list

"""Module to get the movies list from module movies_list and send it to module fresh_tomatoes"""

# get the movies list from module movies_list by calling get_movies_list()
# method with the list_id which will return an array of the movies
# Note: the list_id is given from the TheMovieDB Api

top_rated_movies = movies_list.get_movies_list('top_rated')
popular_movies = movies_list.get_movies_list('popular')
latest_movies = movies_list.get_movies_list('now_playing')
upcoming_movies = movies_list.get_movies_list('upcoming')

# After get the list of movies from the movies_list module send it to
# open_movies_page() method from module fresh_tomatoes with the list and
# the name for the required output html file

fresh_tomatoes.open_movies_page(top_rated_movies, 'index')
fresh_tomatoes.open_movies_page(popular_movies, 'popular')
fresh_tomatoes.open_movies_page(latest_movies, 'now_playing')
fresh_tomatoes.open_movies_page(upcoming_movies, 'upcoming')
