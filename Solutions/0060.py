"""
# PROBLEM 60: Prime pair sets


The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them
in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are
prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with
this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another
prime.
"""

from Lib.Helpers import list_big_primes, efficient_is_prime

prime_list_max = 100000
prime_list = list_big_primes(prime_list_max)

set_list = []

global_variables = {
    "current_number": None,
    "forbidden_numbers": None
}


def check_list_combinations(set_of_primes, glob=None):
    if len(set_of_primes) < 2:
        return True
    if glob and glob['forbidden_numbers']:
        for n in glob['forbidden_numbers']:
            if n in set_of_primes:
                return False
    for ind, prime in enumerate(set_of_primes[:-1]):
        for prime2 in set_of_primes[ind+1:]:
            if not (efficient_is_prime(int(str(prime) + str(prime2)), prime_list_max, prime_list)
                    and efficient_is_prime(int(str(prime2) + str(prime)), prime_list_max, prime_list)):
                if glob and glob['current_number'] and prime == glob['current_number']:
                    glob['forbidden_numbers'].append(prime2)
                return False
    return True


for prime_number in prime_list:
    global_variables["current_number"] = prime_number
    global_variables["forbidden_numbers"] = []
    for prime_set in set_list:
        temp_set = [prime_number] + prime_set
        all_combos_prime = check_list_combinations(temp_set, global_variables)
        n_in_temp_set = len(temp_set)
        if all_combos_prime and n_in_temp_set < 5:
            set_list.append(temp_set)
        elif all_combos_prime and n_in_temp_set == 5:
            print(sum(temp_set))
            exit()

    if prime_number != 2 and prime_number != 5:
        # set can never have 2 or 5
        set_list.append([prime_number])