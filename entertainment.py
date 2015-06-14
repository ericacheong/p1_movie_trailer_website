import media
import fresh_tomatoes
from operator import attrgetter

avengers = media.Movie("Avengers: Age of Ultron",
                       "Heroes teamed up to fight a bigger villain",
                       "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                       "https://www.youtube.com/watch?v=JAUoeqvedMo",
                       2015)

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more.",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         1999)

inception = media.Movie("Inception",
                        "A story about a thief stealing secret by planting an idea into the mind of a CEO",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        2010)

dark_knight = media.Movie("The Dark Knight",
                          "Batman faces the manic, the Joker who wreaks havoc and chaos on the people of Gotham. He has to face the fear of his ability to fight justice.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          2008)

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                     1999)

memento = media.Movie("Memento",                        
                      "A man creates a strange system to help him remember things; so he can hunt for the murderer of his wife without his short-term memory loss being an obstacle.",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0",
                      2000)

seven = media.Movie("Se7en",
                     "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi.",
                     "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
                     "https://www.youtube.com/watch?v=J4YV2_TcCoE",
                     1995)

dogville = media.Movie("Dogville",
                        "A woman on the run from the mob is reluctantly accepted in a small Colorado town. In exchange, she agrees to work for them. As a search visits town, she finds out that their support has a price.",
                        "https://upload.wikimedia.org/wikipedia/en/1/10/Dogville_poster.jpg",
                        "https://www.youtube.com/watch?v=XFocbsVe_Ao",
                        2003)


movies = [avengers,fight_club, inception, dark_knight, matrix, memento, seven, dogville] 
# sort by title in ascending order
s = sorted(movies, key=attrgetter('title'))
# sort by year in descending order 
fresh_tomatoes.open_movies_page(sorted(s, key=attrgetter('year'), reverse=True))

