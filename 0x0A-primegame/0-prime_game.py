#!/usr/bin/python3
""" Defines isWinner function the solution of prime game problem"""


def isWinner(x, nums):
    """Determine the winner between Maria and Ben"""
    Maria = 0
    Ben = 0

    # Find the maximum number in nums to optimize prime sieving
    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to the maximum number in nums
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    # Count the number of primes up to each number in nums
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            Maria += 1
        else:
            Ben += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
