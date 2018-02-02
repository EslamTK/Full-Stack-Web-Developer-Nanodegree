import json
import urllib

import media

"""Module that manage the requests and responses to the TheMovieDB Api"""

# Developer Api key to use the TheMovieDB api
API_KEY = "04ee1d6a7cbff40bd4568b0b617c70d3"


def get_movies_list(list_id):
    """Method that receive a list id and create a request to TheMovieDB Api
       with this id to receive the movies in this list and return a list
       contain Movie type objects that store the movies info"""

    # Create the request url with the api key and the list id
    list_url = "https://api.themoviedb.org/3/movie/" + list_id + "?api_key=" \
               + API_KEY + "&language=en-US&page=1"

    list_response = urllib.urlopen(list_url)

    # Convert the api response to json obj to extract the list movies form it
    list_content = json.loads(list_response.read())

    # Store the result movies list in array
    list_results = list_content['results']

    # Create empty array to store the Movie type objects
    movies_list = []

    for list_item in list_results:
        # Check if the movie is not for adults only or ignore it
        if not list_item['adult']:
            movie_title = list_item['title']
            movie_story_line = list_item['overview']

            # Get the poster image with quality 342 url by concatenate
            # the movie image poster key with the TheMovieDB images database
            movie_poster_image_url = 'https://image.tmdb.org/t/p/w342' \
                                     + list_item['poster_path']

            # Get the trailer youtube from the TheMovieDB Api by the movie id
            movie_trailer_youtube_url = get_movie_trailer(list_item['id'])

            # Check if the movie has a youtube trailer or ignore it
            if movie_trailer_youtube_url:
                # Create a movie type object with the movie info
                movie_details = media.Movie(movie_title, movie_story_line,
                                            movie_poster_image_url,
                                            movie_trailer_youtube_url)
                # Store the movie object in the movies list
                movies_list.append(movie_details)

    # Return the movies list
    return movies_list


def get_movie_trailer(movie_id):
    """Method to get the movie trailers from the TheMovieDB Api by
       the movie id and return the youtube url of the trailer"""

    # Create the request url with the api key and the movie id
    video_url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) \
                + '/videos?api_key=' + str(API_KEY) + '&language=en-US'

    video_response = urllib.urlopen(video_url)

    # Convert the api response to json obj to extract the list movies form it
    video_content = json.loads(video_response.read())

    # Check if the movie hasn't any trailers return False
    if len(video_content['results']) < 1:
        return False

    # Otherwise if the movie has a trailer concatenate the youtube video key to
    # the youtube website and return it
    trailer_youtube_url = 'https://www.youtube.com/watch?v=' + \
                          video_content['results'][0]['key']
    return trailer_youtube_url
