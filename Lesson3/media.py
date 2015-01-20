# !usr/bin/env python

# add webbrowser library
import webbrowser

# class to create a movie information template
# the use of """ in the first part of a class is used to write documentation
# about that class. we can acces with __doc__ function

class Movie():

	""" This class provides a way to store movie related information """

	# class variables
	# google code standard suggest to use only uppercase letters when
	# we work with constants values
	VALID_RATINGS = ["G" , "PG" , "PG-13" , "R"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)