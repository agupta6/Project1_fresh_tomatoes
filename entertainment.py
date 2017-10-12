import media
import fresh_tomatoes

# This file define the objects of six movies which trailer is going to be 
# displayed on website.Each object conatins following details:
# Movie name
# Brief about story
# Poster URL
# Trailer URL
mountain_man = media.Movie("The Mountain Man",
                           """A story of a man who cut the mountain in the
                              memory of his beloved wife.""",
                           "https://upload.wikimedia.org/wikipedia/en/4/4f/Manjhi_The_Mountain_Man_-_Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=I9KAoTQlEWs"
                           )

avatar = media.Movie("Avatar",
                     "The man entered into an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

SpiderMan = media.Movie("SpiderMan",
                        """A story of a boy who becomes spiderman and got
                         supernatural power.""",
                        "https://upload.wikimedia.org/wikipedia/en/2/21/Web_of_Spider-Man_Vol_1_129-1.png",  # noqa
                        "https://www.youtube.com/watch?v=U0D3AOldjMU")


X_Men = media.Movie("X-Men",
                    "A group of people who has unique powers.",
                    "https://upload.wikimedia.org/wikipedia/en/8/81/X-MenfilmPoster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=nbNcULQFojc")

Harry_Porter = media.Movie("Harry-Porter",
                           "The story of a boy who do magic.",
                           "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",  # noqa
                           "https://www.youtube.com/watch?v=PbdM1db3JbY")

The_Core = media.Movie("The Core",
                       "The story of a crew who to the core of Earth.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f4/The_Core_poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=_K19aN953Hg")

movies = [mountain_man, avatar, SpiderMan, X_Men, Harry_Porter, The_Core]
fresh_tomatoes.open_movies_page(movies)

