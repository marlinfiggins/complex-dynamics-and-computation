def Shift_Locus_3(a, b, maxiter=500, bailout=4):  # Shift Locus in case $d=3$

    Twoa3 = 2*a**3  # $2a^3$
    Threea2 = 3*a**2  # $3a^2$

    z1 = Twoa3+b  # first iterate starting from $a$
    z2 = -1*Twoa3 + b  # first iterate starting from $-a$

    for n in range(maxiter):
        absz1 = abs(z1)
        absz2 = abs(z2)

        if min(absz1, absz2) > bailout:  # If both $z_1,z_2$ escape bailout radius
            return n
        # Otherwise, iterate again using $f(z)=z^3-3a^2z+b$.
        z1 = z1**3-z1*Threea2 + b
        z2 = z2**3-3*z2*Threea2 + b

    return 0
