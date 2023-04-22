import random

# Define the parameters for the proof
p = 23  # Prime number used for modular arithmetic
g = 5  # Base of the discrete logarithm
x = 6  # Secret value of the discrete logarithm
h = pow(g, x, p)  # Public value of the discrete logarithm

# Define the functions used for the proof
def prove():
    # Generate a random value r and compute the commitment
    r = random.randint(1, p-1)
    R = pow(g, r, p)
    # Generate a random challenge value e and compute the response
    e = random.randint(0, 1)
    if e == 0:
        s = r
    else:
        s = (r*x) % (p-1)
    # Return the proof (R, s, e)
    return R, s, e

def verify(h, proof):
    # Extract the proof components (R, s, e)
    R, s, e = proof
    # Verify the commitment value R
    if R < 1 or R >= p:
        return False
    # Verify the response value s
    if s < 1 or s >= p-1:
        return False
    # Verify the equation h^s = R * g^e * x^e
    if pow(h, s, p) != (R * pow(g, e, p) * pow(x, e, p)) % p:
        return False
    # If all checks pass, the proof is valid
    return True

# Generate a proof and verify it
proof = prove()
print(verify(h, proof))

# Generate a fake proof and verify it (should fail)
fake_proof = (proof[0], proof[1]+1, proof[2])
print(verify(h, fake_proof))
