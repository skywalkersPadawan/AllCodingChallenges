#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    # capitalize the first word in every string
    s = [word[0].upper() + word[1:] for word in s.split()]
    s = " ".join(s)
    return s


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = solve(s)
    fptr.write(result + "\n")
    fptr.close()
