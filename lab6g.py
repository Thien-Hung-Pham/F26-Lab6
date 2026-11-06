# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 11/05/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

# TO DO 1: Create function add_movie(). 


def add_movie(database, name = "Unknown Movie", director = "Unknown Director", year = 0, runtime = 0):
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }

    database.append(movie)


def main():
    database = []
    # TO DO 2: Call the function 4 times.
    add_movie(database, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(database, "Interstellar", "Christopher Nolan", 2014, 169)
    add_movie(database, "The Matrix", "Lana Wachowski", 1999, 136)
    add_movie(database, "Parasite", "Bong Joon-ho", 2019, 132)

    # TO DO 3: Print the database as instructed in readme.md file.
    for movie in database:
        print(f"{movie['name']} | {movie['director']} | {movie['year']} | {movie['runtime']} minutes")


main()    

# TO DO 4: Run the script. Take screenshot of code and script.
