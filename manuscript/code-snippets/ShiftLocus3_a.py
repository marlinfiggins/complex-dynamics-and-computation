def Shift_Locus_3_a_Set(b=0, xmin=-2, xmax=2, ymin=-2, ymax=2, width=10, height=10, maxiter=50):
    # Compute $a$-space given a specific $b\in\bbC$.

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    escape = np.empty((width, height))

    for i in range(width):  # Loop over $a=x+iy$.
        for j in range(height):
            escape[i, j] = Shift_Locus_3(a=x[i] + 1j*y[j], b=b, maxiter=maxiter)
    return (x, y, escape)
