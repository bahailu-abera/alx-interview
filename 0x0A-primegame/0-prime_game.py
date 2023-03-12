#!/usr/bin/python3
"""
Module for Prime Game
"""


def isprime(n):
    """
    Determines if the given integer is prime
    """
    if n & 1 == 0 or n % 3 == 0:
        return False
    i = 5
    while i < n:
        if n % i == 0:
            return False
        i += 6

    return True


def primeNumbers(num):
    """
    Determines number of primes in a given range
    """
    primes = [0, 1, 2]
    i = 3

    for n in range(4, num + 1):
        if isprime(n):
            primes.append(primes[i - 1] + 1)
        else:
            primes.append(primes[i - 1])
        i += 1

    return primes


def isWinner(x, nums):
    """
    @x: the number of rounds
    @nums: an array of integers
    Return: name of the player that won the game
    """
    primes = primeNumbers(max(nums))
    p1 = 0
    p2 = 0

    for i in range(x):
        if primes[nums[i] - 1] & 1:
            p1 += 1
        else:
            p2 += 1

    if p1 > p2:
        return "Maria"
    elif p1 < p2:
        return "Ben"
    return None
