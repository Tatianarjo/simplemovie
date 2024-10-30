favorite_movies = []

# Adds a movie
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")

# Removes movie    
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found.")
        
# Displaying all movies
def display_movies():
    print("Movie List:")
    for movie in favorite_movies:
        print(f"- {movie}")
        
# Counts movies on the list
def count_movies():
    count=len(favorite_movies)
    print(f"Total number of movies: {count}")
    
# Find a movie
def find_movie(movie):
    if movie in favorite_movies:
        print(f"Movie '{movie}' is listed.")
    else:
        print(f"Movie '{movie}' is not in the list.")
#adds movies
add_movie("Inception")
add_movie("Bambi")
add_movie("She-Devil")

#Clear the list of movies

def clear_movies():
    favorite_movies.clear()
    print(f"All the movies are cleared from the list.")