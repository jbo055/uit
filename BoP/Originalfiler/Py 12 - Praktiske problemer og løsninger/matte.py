import scipy.integrate as spi
import numpy as np

# Definer funksjonen
def integrand(x):
    return (x + 1) / np.sqrt(x**2 + 2*x + 3)

# Beregn det bestemte integralet mellom 0 og 1
result, error = spi.quad(integrand, 0, 1)

# Skriv ut resultatet
print(result)
