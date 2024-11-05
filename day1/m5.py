"""
n musbat butun sonni oladigan va qaytaruvchi qisqa Python funksiyasini yozing
n dan kichik barcha toq musbat sonlarning kvadratlari yig'indisi.
M:
1**2+3**2+5**2+7**2+...+(2n+1)=(n+1)(2n+1)(2n+3)/3
"""

def toq_son(n: int):
    return sum( i**2 for i in range(n) if i%2!=0)

# or math 


if __name__ in "__main__":
    print(toq_son(5))