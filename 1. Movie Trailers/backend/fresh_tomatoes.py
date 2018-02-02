import os
import re
import webbrowser

"""Module to take the movies list and generate html file contain the movies
   (title, poster, youtube_trailer) save it to the main project path and open
   it in the default webbrowser"""

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Movie Trailers</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
	<script src="https://use.fontawesome.com/2dfe59e8c7.js"></script>
    <link   rel="stylesheet" href="styles/style.css">
    <script src="scripts/script.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand">Movie Trailers</a>
          </div>
          <div class="navbar-links">
		  <ul>
		  <li><a href="index.html"><i class="fa fa-star" aria-hidden="true"></i>Top Rated</a></li>
		  <li><a href="popular.html"><i class="fa fa-heart" aria-hidden="true"></i>Popular</a></li>
		  <li><a href="now_playing.html"><i class="fa fa-play" aria-hidden="true"></i>Latest</a></li>
		  <li><a href="upcoming.html"><i class="fa fa-clock-o" aria-hidden="true"></i>Upcoming</a></li>
		  </ul>
		  </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <footer style="text-align:center">
    <img alt="Powerd By The Movie DB" style="width:230px;height:100px;" src="https://www.themoviedb.org/assets/static_cache/bb45549239e25f1770d5f76727bcd7c0/images/v4/logos/408x161-powered-by-rectangle-blue.png">
	</footer>
    </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="250" height="350">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+',
                                     movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                         movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(
            0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies, title):
    # Create or overwrite the output file
    os.chdir("..")
    output_file = open(title + '.html', 'w')

    # Replace the placeholder for the movie tiles with
    # the actual dynamically generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
    os.chdir("backend")
