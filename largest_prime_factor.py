# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    return num
            

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True





