def julia(f, z, maxiter):  # Iterate $f(z)$ until it escapes
    for n in range(maxiter):
        if abs(z) > 4:  # If $f^n(z)$ escapes, return $n$.
            return n
        z = f(z)
    return 0
