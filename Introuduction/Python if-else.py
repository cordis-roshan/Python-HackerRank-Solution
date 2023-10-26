#!/bin/python3

import math
import os
import random
import re
import sys



def odd_even(n):
    if n % 2 ==0:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

n=int(input())
odd_even(n)
