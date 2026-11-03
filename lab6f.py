# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 11/05/2026
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

# TO DO 1: Create function histogram() as instructed in readme.md file. 
# TO DO 2: Create main() function and call histogram(). Call the main() function.

def histogram(string):
    char_count = {}

    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    for char in char_count:
        val = "*" * char_count[char]
        print(f"{char} {val}")


def main():
    string ="hello"
    histogram(string)    



main()

# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.
