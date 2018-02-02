import webbrowser

"""Module contain the movie class that store the movie details"""


class Movie:
    """Class used to store the movie details (title, story_line,
       poster_image_url, trailer_youtube_url)"""
    def __init__(self, title, story_line,
                 poster_image_url, trailer_youtube_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def play_trailer(self):
        """Method to open the movie youtube trailer in the default browser"""
        webbrowser.open(self.trailer_youtube_url)
