def mandelbrot_c(z, maxiter, bailout, bailout_est):  # Iterate $f_c(0)$ until it escapes.
    c = z
    for n in range(maxiter):
        absz = abs(z)
        if absz > bailout:  # If $\abs{z}> 2$, orbit escapes to $\infty$
            # return continuous estimate of escape iterate $n-\frac{\log\log\abs{z_n}}{\log 2}+b_{est}$.
            return n - np.log(np.log(absz))/np.log(2) + bailout_est
        z = z*z + c
    return 0


def mandelbrot_c_set(xmin, xmax, ymin, ymax, width, height, maxiter):

    bailout = 2**30
    bailout_est = np.log(np.log(bailout))/np.log(2)  # $b_{est}= \frac{\log\log b}{\log 2}$

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    escape = np.empty((width, height))

    for i in range(width):  # Loop over each $c=x+yi$.
        for j in range(height):
            escape[i, j] = mandelbrot_c(x[i] + 1j*y[j], maxiter, bailout, bailout_est)
    return (x, y, escape)
