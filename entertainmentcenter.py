import media
import codehawk

# 6 objects has been defined from the class Movie.

tomb_raider = media.Movie(
    "Tomb Raider", "The fate of humanity rests in her hands.",
    "https://upload.wikimedia.org/wikipedia/en"
    "/b/bd/Tomb_Raider_%282018_film%29.png",
    "https://youtu.be/8ndhidEmUbI"
)
jwfk = media.Movie(
    "Jurassic World: Fallen Kingdom",
    "It’s been four years since theme park and luxury resort Jurassic World"
    " was destroyed by dinosaurs out of containment."
    "Isla Nublar now sits abandoned by humans"
    " while the surviving dinosaurs fend for themselves in the jungles",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/Jurassic_World_Fallen"
    "_Kingdom.png",
    "https://youtu.be/vn9mMeWcgoM"
)
avengers = media.Movie(
    "Avengers: Infinity War",
    " Avengers unite to battle their most powerful enemy yet Thanos.",
    "https://upload.wikimedia.org/wikipedia/en"
    "/4/4d/Avengers_Infinity_War_poster.jpg",
    "https://youtu.be/6ZfuNTqbHE8"
)
venom = media.Movie(
    "Venom", "One of Spider-Man's greatest villains receives his"
    " own origin movie in VENOM starringTom Hardy.",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Venom_poster.jpg",
    "https://youtu.be/zX81KEqzy_M"
)
dp2 = media.Movie(
    "Deadpool: 2",
    "Wisecracking mercenary Deadpool meets Russell, an angry"
    " teenage mutant who lives at an orphanage.",
    "https://upload.wikimedia.org/wikipedia/en/c/cf/"
    "Deadpool_2_poster.jpg",
    "https://youtu.be/wLeGWcVeIZ4"
)
the_nun = media.Movie(
    "The Nun",
    "In 1952 Romania, a nun,"
    " a Catholic priest and a novice, sent by the Vatican,"
    " investigate the mysterious suicidal"
    " death of a nun at the Cârța Monastery.",
    "https://upload.wikimedia.org/wikipedia/en/3/34/TheNunPoster.jpg",
    "https://youtu.be/pzD9zGcUNrw"
)
movies = [the_nun, venom, jwfk, avengers, tomb_raider, dp2]

# Function open_movies_page is being called from fresh_tomatoes module
# which takes movies, a list as an argument
codehawk.open_movies_page(movies)
