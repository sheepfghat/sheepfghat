#4 лекция
#Functions 2 - squaring an argument
def square(n):
    return n * n
#Beginner Series #2 Clock
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000
#Grasshopper - Array Mean
def find_average(nums):
    return sum(nums) / len(nums)
#You're a square!
from math import sqrt

def is_square(n):
    if n < 0:
        return False
    return sqrt(n) == int(sqrt(n))
#Opposite number
def opposite(number):
    return -number