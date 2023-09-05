#!/usr/bin/python3
"""
Module for Prime Game
"""


def prime_numbers(n):
    """
    Determines number of primes in a given range
    """
    mark = [True for _ in range(n + 1)]
    primes = [0 for _ in range(n + 1)]
    count = 0

    i = 2

    while i * i <= n:
        if mark[i]:
            for j in range(i * i, n + 1, i):
                mark[j] = False

        i += 1

    for i in range(2, n + 1):
        if mark[i]:
            count += 1

        primes[i] = count

    return primes


def isWinner(x, nums):
    """
    @x: the number of rounds
    @nums: an array of integers
    Return: name of the player that won the game
    """
    ben = maria = 0
    primes = prime_numbers(max(nums))

    for n in nums:
        maria += primes[n] & 1
        ben += (primes[n] & 1) ^ 1

    if maria > ben:
        return 'maria'

    if ben > maria:
        return 'ben'

    return None
