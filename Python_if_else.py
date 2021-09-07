import math
import os
import random
import re
import sys

def numbers(n):
    # when the number is odd print weird
    if(n % 2 !=0):
        return "Weird"
    # when number is even and in between 2 and 5 both inclusive
    elif((n % 2 ==0) and ((n <= 5)and(n >= 2))):
        return "Not Weird"
    # when number is even and in between 6 and 20 both inclusive
    elif((n % 2 == 0) and ((n<=20)and(n>=6))):
        return "Weird"
    else:
        return "Not Weird"
        
if __name__ == '__main__':
    n = int(input().strip())
    print(numbers(n))