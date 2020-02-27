def julia_set(f, width=10, height=10, maxiter=200, xmin=-2, xmax=2, ymin=-1, ymax=1):

    x = np.linspace(xmin, xmax, width)   # Generate $x$ values
    y = np.linspace(ymin, ymax, height)  # Generate $y$ values
    escape = np.empty((width, height))

    for i in range(width):  # Loop over each $z=x+yi\in\bbC$.
        for j in range(height):
            escape[i, j] = julia(f, z=x[i] + 1j*y[j], maxiter)
    return (x, y, escape)
