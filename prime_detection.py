"""
    Prime Detector
    This program uses lambda functions to detect prime numbers from a list
    of numbers:
    5, 36, 123, 47, 8, 143
"""
import math


def isPrime(n):
    if n <=1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    begin = [5, 36, 123, 47, 7, 8, 143]

    print(list(filter(lambda x : isPrime(x), begin)))


if __name__=='__main__':
    main()