initials = input("введите ФИО: ")
parts = initials.split()
surname = parts[0]
name = parts[1]
patronymic = parts[2]
name_initial = name[0].upper()
patronymic_initial = patronymic[0].upper()
result = surname.capitalize() + " " + name_initial + "." + patronymic_initial + "."
print(result)