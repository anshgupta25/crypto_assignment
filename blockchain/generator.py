import random
import largeprime
def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, p):
    """Returns True if g is a primitive root modulo p, False otherwise."""
    phi = p-1
    factors = []
    d = 2
    while d*d <= phi:
        if phi % d == 0:
            factors.append(d)
            while phi % d == 0:
                phi //= d
        d += 1
    if phi > 1:
        factors.append(phi)
    for factor in factors:
        if pow(g, (p-1)//factor, p) == 1:
            return False
    return True

def find_generator(p):
    """Finds a generator of the prime number p."""
    while True:
        g = random.randint(2, p-1)
        if gcd(g, p) == 1 and is_primitive_root(g, p):
            return g

if __name__ == '__main__':
    print(find_generator(7))
    