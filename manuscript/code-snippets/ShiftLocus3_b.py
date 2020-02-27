def Shift_Locus_3_b_Set(a=0, xmin=-2, xmax=2, ymin=-2, ymax=2, width=10, height=10, maxiter=50):
        # Compute $b$-space given a specific $a\in\bbC$.

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    escape = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            escape[i, j] = Shift_Locus_3(a=a, b=x[i] + 1j*y[j], maxiter=maxiter)
    return (x, y, escape)
