# Author:Mahtab Zilaie
# Date: October 29, 2019
# Description: recursive function that finds the multiplication of two integers using addition

def multiply(n, m):
    """multiplies two integers"""
    if (n or m) == 0:
        return 0
    elif n == 1:
         return m
    elif m == 1:
        return n
    return n + multiply(n, m-1)