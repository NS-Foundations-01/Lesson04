products = ['olma', 'madarin', 'kivi', 'annjir', 'banan']
               # 0.      1        2         3       4
               #-5     -4       -3        -2      -1
print(products[-5])

meva = str(input("Mevani kiriting -> "))

products.append(meva)

print(f"{meva} ro'yxatga qo'shildi")
print(products)


products.remove(meva)
print(f"{meva} o'chirildi")
print(products)

products.insert(0, meva)

print(products)


products.pop(2)
print(products)