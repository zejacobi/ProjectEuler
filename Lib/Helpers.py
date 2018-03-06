def list_primes(limit):
    """Finds a list of all primes below the input limit"""
    bits = [0] + [1 for _ in range(limit)]  # we filter out 0
    bits[1] = 0  # and also one.
    primes = []

    for num, prime in enumerate(bits):
        if not prime:
            continue
        primes.append(num)
        index = num ** 2
        while index <= limit:
            bits[index] = 0
            index += num

    return primes


def all_rotations(number):
    """Finds all rotations of a number (e.g. 123 => 123, 231, 312"""
    out = [number]
    str_num = str(number)
    current = str_num[-1] + str_num[:-1]
    while int(current) not in out:
        out.append(int(current))
        current = current[-1] + current[:-1]

    return out


def is_palindrome(num):
    """Checks if a number is a palindrome. Does return True for single digit numbers"""
    str_num = str(num)
    for idx in range(len(str_num) // 2 + 1):
        if not str_num[idx] == str_num[-idx - 1]:
            return False
    return True
