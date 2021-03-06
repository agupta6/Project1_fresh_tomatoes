import webbrowser


class Movie():
    """This class creates an object of Movie type."""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """This is a constructor method.It initialize all the Movie
           variables. It takes the following inputs:
           movie_title     [in] the name of movie
           movie_storyline [in] the storyline of movie
           poster_image    [in] the poster image url of movie
           trailer_youtube [in] the movie trailer url"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method opens the movie trailer url."""
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        """This method opens the movie poster url."""
        webbrowser.open(self.poster_image_url)
