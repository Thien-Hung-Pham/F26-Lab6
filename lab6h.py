# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 11/05/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.


def add_movie(database, name = "Unknown Movie", director = "Unknown Director", year = 0, runtime = 0):
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }

    database.append(movie)

# TO DO 2: Create function find_movie().    
def find_movie(database, search):
    results = []

    for movie in database:
        if search.lower() in movie["name"].lower():
            results.append(movie)

    return results


def main():
    database = []
    add_movie(database, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(database, "Interstellar", "Christopher Nolan", 2014, 169)
    add_movie(database, "The Matrix", "Lana Wachowski", 1999, 136)
    add_movie(database, "Parasite", "Bong Joon-ho", 2019, 132)
    add_movie(database, "Gone with the Wind", "Victor Fleming", 1939, 238)
    add_movie(database, "Forever Gone", "John Doe", 2020, 120)

    # TO DO 3: Call the function as instructed in readme.md file.
    print("Search: gone")
    for movie in find_movie(database, "gone"):
        print(movie)

    print("\nSearch: inception")
    for movie in find_movie(database, "inception"):
        print(movie)


if __name__ == "__main__":
    main()    


# TO DO 4: Run the script. Take screenshot of code and script.

