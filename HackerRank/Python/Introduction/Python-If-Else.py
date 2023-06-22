#!/bin/python3

import math
import os
import random
import re
import sys

# Simplified solution to 4 lines

if __name__ == '__main__':
    n = int(input().strip()) # Honestly don't know what the strip function does, will have to research!
    
    if n % 2 == 0 and ((n >= 2 and n <= 5) or n > 20):
        print("Not Weird")
    else:
        print("Weird")
