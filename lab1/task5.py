a = float(input("введите а: "))
b = float(input("введите b: "))
print(f"сумма: {a+b}")
print(f"разность: {a-b}")
print(f"произведение: {a*b}")
print(f"возведение в степень: {a**b}")
if b==0:
    print("деление на 0 невозможно")
else:
    print(f"деление: {a/b}")
    print(f"остаток: {a%b}")