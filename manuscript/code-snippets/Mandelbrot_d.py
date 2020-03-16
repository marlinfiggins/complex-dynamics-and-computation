def mandelbrot_d(z, maxiter):  # Iterate $f_c(0)$ until it escapes.
    c = z
    for n in range(maxiter):
        if abs(z) > 2:  # If $\abs{z}> 2$, orbit eventually escapes to $\infty$.
            return n
        z = z*z + c
    return 0


def mandelbrot_dset(xmin, xmax, ymin, ymax, width, height, maxiter):

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    escape = np.empty((width, height))

    for i in range(width):  # Loop over each $c=x+yi$.
        for j in range(height):
            escape[i, j] = mandelbrot_d(x[i] + 1j*y[j], maxiter)
    return (x, y, escape)
