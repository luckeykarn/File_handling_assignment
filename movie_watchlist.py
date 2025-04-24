import json
import os

filename = "movie_list.json"

# Load movies from JSON file
def load_movies():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []


def save_movies():
    with open(filename, "w") as file:
        json.dump(movies, file, indent=4)

movies = load_movies()

# Add a new movie
def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")

    movie = {
        "title": title,
        "genre": genre,
        "status": "pending"
    }

    movies.append(movie)
    save_movies()
    print("Movie added successfully!")

# Mark a movie as watched
def mark_watched():
    title = input("Enter movie title to mark as watched: ")

    found = False
    for movie in movies:
        if movie["title"].lower() == title.lower():
            movie["status"] = "watched"
            found = True
            break

    if found:
        save_movies()
        print("Movie marked as watched.")
    else:
        print("Movie not found.")

# Search moviees by genere
def search_genre():
    genre = input("Enter genre to search: ").lower()
    found = False
    print(f"\n--- Movies in genre: {genre} ---")
    for movie in movies:
        if movie["genre"].lower() == genre:
            print(f"{movie['title']} | Status: {movie['status']}")
            found = True
    if not found:
        print("No movies found in this genre.")

# List all unwatched movies
def list_unwatched():
    found = False
    print("\n--- Unwatched Movies ---")
    for movie in movies:
        if movie["status"].lower() == "pending":
            print(f"{movie['title']} | Genre: {movie['genre']}")
            found = True
    if not found:
        print("No unwatched movies found.")

# Main loop
while True:
    print("\n--- Movie Watchlist Tracker ---")
    print("Commands: add | watch | search | unwatched | exit")
    command = input("Enter command: ").lower()

    if command == "add":
        add_movie()
    elif command == "watch":
        mark_watched()
    elif command == "search":
        search_genre()
    elif command == "unwatched":
        list_unwatched()
    elif command == "exit":
        print("Exiting Movie tracking system...")
        break
    else:
        print("Invalid command. Try again.")
