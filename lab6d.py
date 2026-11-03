# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 11/05/2026
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# TO DO 1: Create function times_ten as instructed in readme.md file. 
def multiplyByTen(start,end):
    set = {}
    for num in range(start , end +1):
        set[num] = num*10

    return set

def main():
    my_dictionary = multiplyByTen(2,6)
    print(my_dictionary)

main()
    

# TO DO 2: Run the script.
