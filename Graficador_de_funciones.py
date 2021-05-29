import matplotlib.pyplot as plt
import numpy as np

def funcion(t):
    ans = 0.5
    omega = 1
    for n in range(1, 5000, 2):
        ans += np.e**(-n/24) * 1/(2*np.pi) * (-1)**((n-1)/2)*np.cos(n*np.pi*t)/n
    return ans

c = np.linspace(0, 4, 100000)
d = funcion(c)
print(d)
print(c)
plt.plot(c, d, 'ko', markersize=0.2)
plt.show()
