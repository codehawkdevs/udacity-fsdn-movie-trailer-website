import webbrowser


class Movie():
    """This class can be used for defining new objects which has several fields
like title, storyline, movie poster and the movie trailer youtube link."""
    def __init__(
        self, movie_title, movie_storyline, poster_image, trailer_youtube
    ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# A function in a class is called instance method.

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
