# Assignment Day 02
# v1.4) Make my_pow custom function instead of ** operator, power function and make it work.

import math

def my_pow(b, e) -> float:
    """
    A user-defined function that receives a base and exponent and returns the power result in the form of a real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    if e < 0:
        b = 1/  b
        e *= -1
    integer_part = int(e)
    fraction_part = e - integer_part

    result = 1
    for _ in range(integer_part):
        result *= b

    if fraction_part > 0:
        result *= math.exp(fraction_part * math.log(b))

    return result



def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while i < (int(my_pow(num, 0.5)) + 1):
            if num % i == 0:
                return False
            i += 1
    else:
        return False
    return True


print(my_pow(2, 9))
numbers = input("Input number : ").split()  # ex) 900 1000
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

j = n1
while j <= n2:
    if is_prime(j):
        print(j, end=' ')
    j += 1