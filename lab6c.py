# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 11/05/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

# TO DO 1: Copy the code from lab6b.py and paste here.
def s3_and_s5_not_s7():
    s3 = buildtheSet(3)
    s5 = buildtheSet(5)
    s7 = buildtheSet(7)
    return (s3.union(s5)) - s7

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

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s3oands5nots7 = s3_and_s5_not_s7()
    print("s3oands5nots7: ", s3oands5nots7)
    print("----------------------------------------")




main()


# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
