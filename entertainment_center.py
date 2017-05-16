import media
import fresh_tomatoes

#create movie instances
toy_story = media.Movie("Toy Story",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=5PSNL1qE6VY")


movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
