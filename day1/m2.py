"""
Qisqa Python funksiyasini yozing, is even(k), butun son qiymatini oladi va
k juft bo'lsa True, aks holda False qaytaradi. Biroq, sizning vazifangiz
ko'paytirish, modul yoki bo'lish operatorlaridan foydalana olmaydi.
"""


def is_even(k):
    k = int(str(k)[-1])
    return True if k==0 or k==2 or k==4 or k==6 or k==8 else False


if __name__ in '__main__':
    print(is_even(158960))