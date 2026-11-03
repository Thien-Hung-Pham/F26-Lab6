# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 11/05/2026
# Purpose: Traverse dictionary.
# Usage: ./lab6e.py

# TO DO 1: Create a for in loop as instructed in readme.md file. 

def main():
    my_dict = {"switzerland" : "Alps", "United States" : "Alska Range", "Armenia" : "Caucasus", "Argentina" : "Andes", "Karakoram" : "Pakistan"}

    for key in my_dict:
        print(f"{key} : {my_dict[key]}")

main()


# TO DO 2: Run the script, and take the screenshot of code and output.
