# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.

database = []

def add_movie(name, director, year, runtime):
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }

    database.append(movie)
    
def find_movie(search):
    results = []

    for movie in database:
        if search.lower() in movie["name"].lower():
            results.append(movie)

    return results


def main():
    add_movie("Inception", "Christopher Nolan", 2010, 148)
    add_movie("Interstellar", "Christopher Nolan", 2014, 169)
    add_movie("The Matrix", "Lana Wachowski", 1999, 136)
    add_movie("Parasite", "Bong Joon-ho", 2019, 132)

    print("Search: gone")
    for movie in find_movie("gone"):
        print(movie)

    print("\nSearch: inception")
    for movie in find_movie("inception"):
        print(movie)


main()    


# TO DO 2: Create function find_movie().
# TO DO 3: Call the function as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.

