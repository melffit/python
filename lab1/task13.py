raw = input("введите числа: ").split()
numbers = []
for item in raw:
    if '.' in item:
        numbers.append(float(item))
    else:
        numbers.append(int(item))
count = {}
for x in numbers:
    count[x] = count.get(x, 0) + 1
unique = [x for x in numbers if count[x] == 1]
print(f"уникальные числа: {unique}")
repeated = set(x for x in numbers if count[x] > 1)
print(f"повторяющиеся числа: {repeated}")
even = [x for x in numbers if isinstance(x, int) and x % 2 == 0]
print(f"четные числа: {even}")
odds = [x for x in numbers if isinstance(x, int) and  x % 2 != 0]
print(f"нечетные числа: {odds}")
negative = [x for x in numbers if x < 0]
print(f"отрицательные числа: {negative}")
floats = [x for x in numbers if isinstance(x, float)]
print(f"числа с плавающей точкой: {floats}")
sum5 = sum(x for x in numbers if isinstance(x, int) and x % 5 == 0)
print(f"сумма чисел, кратных 5: {sum5}")
print(f"максимальное число: {max(numbers)}")
print(f"минимальное число: {min(numbers)}")