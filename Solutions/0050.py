"""
# Problem 50: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms,
and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from Lib.Helpers import list_primes

# Ah, I love clear bounds

upper_bound = 1000000
all_primes = list_primes(upper_bound)
# ^ I may have said this before, but I don't need to worry here if this gives primes below
# 1,000,000 only or would include 1,000,000, because 1,000,000 obviously isn't prime.

# So this has some combinatorial explosion, eh?
# I'll just have to be clever in my limits

prime = 953
num_consec = 21


def find_index_for_cutoff(primes, max_number, current_consec):
    max_number = max_number / current_consec
    for cutoff_index, current_prime in enumerate(primes):
        if current_prime > max_number:
            return cutoff_index + current_consec


max_index = find_index_for_cutoff(all_primes, upper_bound, num_consec)
next_start = None
num_consec_when_next_set = None
next_iter_num_consec = None
next_start_used = False

for index, p_sum in enumerate(all_primes):
    if index > max_index:
        break

    iter_set = all_primes[index + 1:]

    if next_start:
        # copy over all the math we've already done
        p_sum = next_start
        iter_set = all_primes[index + num_consec_when_next_set - 1:]
        next_start = None
        next_start_used = True
    for count, next_prime in enumerate(iter_set):
        p_sum += next_prime
        if next_start_used:
            # since we've skipped things, we need to fix the count
            count = count + num_consec_when_next_set - 2
        if p_sum > upper_bound or (count + index) > max_index:
            break
        if count + 2 > num_consec:  # +1 for original, +1 for 0 indexing
            if p_sum in all_primes:
                prime = p_sum
                num_consec = count + 2
                max_index = find_index_for_cutoff(all_primes, upper_bound, num_consec)
        elif count + 2 == num_consec:
            # we've done the count now for the next n consecutive numbers, which is where we always
            # start our investigation. The next loop will re-use all but one of these numbers,
            # so let's save that sum for it. The one number it isn't using is the initial one.
            # subtract that out!
            next_iter_num_consec = num_consec
            next_start = p_sum - all_primes[index]

    # This complicated dance took forever to debug. Basically, we need to be really careful not to
    # make two easy mistakes:
    #  1: If we just use num_consec, our index will get thrown off every time we find a new number
    #  2: If we update num_consec_when_next_set directly, we'll throw off the index for all future
    #     iterations with this number.

    # Doing it this way successfully gets the right answer and has my answer taking ~2s to generate,
    # down from 20-30 seconds when my limits weren't that good.
    next_start_used = False
    num_consec_when_next_set = next_iter_num_consec
    next_iter_num_consec = None


print(num_consec, prime)
