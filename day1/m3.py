"""
ning ketma-ketligini oladigan qisqa Python funksiyasini yozing, minmax(data).
bir yoki bir nechta raqamni kiritadi va eng kichik va eng katta raqamlarni qaytaradi
uzunligi ikki bo'lgan kortejning shakli. Min yoki o'rnatilgan funktsiyalardan foydalanmang
yechimingizni amalga oshirishda.
"""

def minmax(data):
    max = data[0]
    min = data[0]
    for i in range(len(data)):
        if min >= data[i]:
            min = data[i]
        if max <= data[i]:
            max = data[i]
    return max, min


if __name__ in '__main__':
    print(minmax([15, 25, 8, 5, 3, 86, 55, 48]))

