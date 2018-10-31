from math import floor, sqrt


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


def list_big_primes(limit):
    """Finds an list of all primes below input limit without melting your RAM. Use when
        limit is large! This is O(sqrt(n)) in space and O(nlog(n)) in time."""
    delta = int(floor(sqrt(limit)))
    primes = list_primes(delta)
    usable_primes = [prime for prime in primes if prime <= sqrt(delta * 2)]
    higher_primes = [prime for prime in primes if prime >= sqrt(delta * 2)]

    for i in range(delta):
        ix = i + 1  # 0 is our standard sieve, already called above
        highest_this_sieve = (ix + 1) * delta
        prime_limit = sqrt(highest_this_sieve)
        bits = [0] + [1 for _ in range(delta - 1)]

        # efficiently maintain a list of what primes we're checking
        highest_ix = -1
        for list_ix, prime in enumerate(higher_primes):
            if prime <= prime_limit:
                usable_primes.append(prime)
                highest_ix = list_ix
        highest_ix += 1
        higher_primes = higher_primes[highest_ix:]

        # at this point, usable primes has all primes less than sqrt(highest_this_sieve)
        starting_val_this_iteration = ix * delta

        # now we go through our bits for this part of the sieve and mark off all the non prime
        # numbers
        for existing_prime in usable_primes:
            prime_index = existing_prime * (1 + starting_val_this_iteration // existing_prime) - \
                          starting_val_this_iteration
            bits[prime_index] = 0
            prime_index += existing_prime
            while prime_index < delta:
                bits[prime_index] = 0
                prime_index += existing_prime

        # we don't want to always check if the prime is below the limit; just check when we get
        # close to the limit.
        if ix < delta:
            for final_ix, bit in enumerate(bits):
                if bit:
                    prime = final_ix + starting_val_this_iteration
                    primes.append(prime)
                    higher_primes.append(prime)
        else:
            for final_ix, bit in enumerate(bits):
                if bit:
                    prime = final_ix + starting_val_this_iteration
                    if prime < limit:
                        primes.append(prime)
    return primes


def efficient_is_prime(number, regime_change, primes_below_regime_change):
    """A quick check for prime that can be well calibrated to the size of the problem and
       is designed to allow all big computations to be done beforehand. Regime change is the
       number that the list of primes goes up. This should be the square root of the largest
       number you expect to see"""
    if number < regime_change:
        if not primes_below_regime_change or not len(primes_below_regime_change):
            return number in list_primes(regime_change)
        else:
            return number in primes_below_regime_change
    elif number <= (regime_change ** 2):
        for prime in primes_below_regime_change:
            if not number % prime:
                return False
        return True
    else:
        raise(NotImplementedError('Give a bigger pre-computed list!'))


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


def contains_all_numbers(num, set_of_nums):
    """Returns true if the num contains all numbers in the set once and only once"""
    str_num = str(num)
    if len(str_num) != len(set_of_nums):
        return False
    return all([True if str(n) in str_num else False for n in set_of_nums])


def greatest_common_divisor(a, b, prime_list=None):
    """Returns the greatest common divisor of a and b"""
    # https://en.wikipedia.org/wiki/Euclidean_algorithm

    # get our numbers in a predictable format
    if b > a:
        b, a = a, b

    # deal with co-prime cases efficiently if given the tools to do so
    if prime_list:
        if a in prime_list:
            return 1
        elif b in prime_list:
            if a % b == 0:
                return b
            else:
                return 1

    while b != 0:
        new_a = b
        b = a % b
        a = new_a
    return a
