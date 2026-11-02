raw1 = input("введите первый список чисел: ").split()
numbers1 = []
for item in raw1:
    if '.' in item:
        numbers1.append(float(item))
    else:
        numbers1.append(int(item))
raw2 = input("введите второй список чисел: ").split()
numbers2 = []
for item in raw2:
    if '.' in item:
        numbers2.append(float(item))
    else:
        numbers2.append(int(item))
set1 = set(numbers1)
set2 = set(numbers2)
common = set1 & set2
print(f"общие числа: {common}")
in_only_first = set1 - set2
in_only_second = set2 - set1
print(f"только в первом: {in_only_first}")
print(f"только во втором: {in_only_second}")
symmetric = set1 ^ set2
print(f"симметрическая разность: {symmetric}")