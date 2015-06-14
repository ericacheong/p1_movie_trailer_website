# media.py
# Date: 14 Jun 2014
# Created by: Erica Cheong

class Movie():
    """This class stores movie related information"""

# TODO: add quotes
    def __init__(self, title, storyline, poster_img, trailer, year):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer
        self.year = year
