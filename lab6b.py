# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 11/05/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py


def s3_or_s5():
    s3 = buildtheSet(3)
    s5 = buildtheSet(5)

    # Other method: I can use XOR (return s3 ^ s5) to achieve the same thing  


    just_s3 = s3 - s5
    just_s5 = s5 - s3


    return just_s3.union(just_s5) 

# TO DO 1: Copy the code from lab6a.py and paste here.
def buildtheSet(divisor):
    set = {0}
    # Complete this function
    for num in range(101):
        if num % divisor == 0:
            set.add(num)
    return set


def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s3ors5 = s3_or_s5()
    print("s3ors5: ", s3ors5)
    print("----------------------------------------")




main()

# TO DO 2: Create the function s3ors5().

    


# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
