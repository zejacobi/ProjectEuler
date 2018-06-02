"""
# Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

# I distinctly recall hating factorization problems, although I can't remember why. Um. Let's
# go check through the other problems for other factorization problems?

# (At least python doesn't hate the unicode ² in the problem; it's previously thrown a fit about
# unicode characters and proper encodings)


# Okay I think I just have to bite the bullet and implement a factoring algorithm from Wikipedia.
# I'm going to use the "Rational sieve"; it's apparently a bit slower than the "General Field
# Sieve", but simpler, which is good, because implementing algorithms from Wikipedia is always such
# an absolute shit-show. I don't know how they make them so difficult to understand, but they do.

# (I could find some better explanation, but if I don't suffer while solving these, it feels like I
# cheated and takes away half the fun. From that lens, Wikipedia's terrible pseudocode and
# annoyingly minimalistic conventions are a blessing in disguise.)
