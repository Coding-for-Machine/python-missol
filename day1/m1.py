"""
Qisqa Python funksiyasini yozing, is_multiple(n, m), u ikkita butun sonni oladi
qiymatlar va rost qaytaradi, agar n m ning karrali bo'lsa, ya'ni ba'zilari uchun n = mi
integer i, aks holda False.
"""

def is_multiple(n, m):
    return True if m%n==0 or n%m==0 else False


if __name__ in '__main__':
    print(is_multiple(15, 85))
    

