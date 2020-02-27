def julia(c, z, maxiter):  # Iterate $f_c(z)$ until it escapes
    for n in range(maxiter):
        if abs(z) > 4:  # If $f_c^n(z)$ escapes, return $n$.
            return n
        z = z*z + c
    return 0
