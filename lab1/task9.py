print("типы измерений: 1-длина, 2-вес, 3-температура")
type_meas = int(input("выберите тип измерения: "))
if type_meas == 1:
    units = {1: "метр", 2: "километр", 3: "сантиметр", 4: "миля"}
    to_meters = {1: 1, 2: 1000, 3: 0.01, 4: 1609.34}
    print("единицы: 1-метр, 2-километр, 3-сантиметр, 4-миля")
    from_unit = int(input("исходная единица: "))
    to_unit = int(input("целевая единица: "))
    value = float(input("значение: "))
    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    print(f"Результат: {value} {units[from_unit]} = {result:.2f} {units[to_unit]}")
elif type_meas == 2:
    units = {1: "килограмм", 2: "грамм", 3: "тонна", 4: "фунт"}
    to_kg = {1: 1, 2: 0.001, 3: 1000, 4: 0.453592}
    print("единицы: 1-килограмм, 2-грамм, 3-тонна, 4-фунт")
    from_unit = int(input("исходная единица: "))
    to_unit = int(input("целевая единица: "))
    value = float(input("значение: "))
    kg = value * to_kg[from_unit]
    result = kg / to_kg[to_unit]
    print(f"результат: {value} {units[from_unit]} = {result:.2f} {units[to_unit]}")
elif type_meas == 3:
    units = {1: "цельсий", 2: "фаренгейт", 3: "кельвин"}
    print("единицы: 1-цельсий, 2-фаренгейт, 3-кельвин")
    from_unit = int(input("исходная единица: "))
    to_unit = int(input("целевая единица: "))
    value = float(input("значение: "))
    if from_unit == 1:
        celsius = value
    elif from_unit == 2:
        celsius = (value - 32) * 5/9
    elif from_unit == 3:
        celsius = value - 273.15
    if to_unit == 1:
        result = celsius
    elif to_unit == 2:
        result = celsius * 9/5 + 32
    elif to_unit == 3:
        result = celsius + 273.15
    print(f"результат: {value} {units[from_unit]} = {result:.2f} {units[to_unit]}")
else:
    print("неверный тип измерения")