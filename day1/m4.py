"""
n musbat butun sonni oladigan va qaytaruvchi qisqa Python funksiyasini yozing
n dan kichik barcha musbat sonlarning kvadratlari yig'indisi.
M:
1**2+2**2+3**3+...+(n-1)**2=n(n+1)(2n+1)/6
1+2+3+...+n=n(n+1)/2
"""


def k(n):
    return sum(data**2 for data in range(1, n))

# or math

def k(n):
    n=n-1
    return n*(n+1)*(2*n+1)/6

if __name__ in "__main__":
    print(k(4))