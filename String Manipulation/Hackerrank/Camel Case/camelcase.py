#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def camelcase(s):
    word_count = 0
    for letter in s:
        if letter.upper():
            loc = s.index(letter)
            word = s[:loc]
            word_count += 1
    return word_count

s = 'oneTwoThree'
result = camelcase(s)
print(result)
