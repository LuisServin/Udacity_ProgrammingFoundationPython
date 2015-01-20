# !usr/bin/env python

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						 "A story of a boy and his toys that come to life",
						 "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
						 "https://www.youtube.com/watch?v=KYz2wyBy3kc") # youtube trailer

# print toy_story.storyline
avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://www.writingfordesigners.com/wp-content/uploads/2014/09/Avatar-Poster-blue-people.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print avatar.storyline
# avatar.show_trailer()

movies = [toy_story, avatar]
# fresh_tomatoes.open_movies_page(movies)
# print media.Movie.VALID_RATINGS
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__