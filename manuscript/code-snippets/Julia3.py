def julia(a, b, z, maxiter):  # Iterate $f_{a,b}(z)=z^3-a^2z+b$ until it escapes
    Threea2 = 3*a**2  # Pre-allocate $3a^2$.
    for n in range(maxiter):
        if abs(z) > 4:  # If $f_{a,b}(z)$ escapes, return $n$.
            return n
        z = z**3 - Threea2*z + b
    return 0
