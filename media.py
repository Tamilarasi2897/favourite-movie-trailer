import webbrowser
class Movie( ):
    ''' The variables below is now called from the entertainment file so it can be initialised.
        Al the arguments for the movie fragments to load is called then read into memory. Self below gets called
        which is a instance being created to run which is toy story. All the instances below gets called  and is
        populated with information from the entertainment file.''' 
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):'''When __init__ is called all arguments in
                                                                                       parenthese ( ) gets called and populated with appropriate values.'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
