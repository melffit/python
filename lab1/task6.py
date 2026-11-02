day = int(input("введите день вашего рождения: "))
month = int(input("введите месяц вашего рождения: "))
if (month == 1 and day >=20) or (month == 2 and day <=18):
    sign = "водолей"
if (month == 2 and day >=19) or (month == 3 and day <=20):
    sign = "рыбы"
if (month == 3 and day >=22) or (month == 4 and day <=19):
    sign = "овен"
if (month == 4 and day >=20) or (month == 5 and day <=20):
    sign = "телец"
if (month == 5 and day >=21) or (month == 6 and day <=20):
    sign = "телец"
if (month == 6 and day >=21) or (month == 7 and day <=22):
    sign = "рак"
if (month == 7 and day >=23) or (month == 8 and day <=22):
    sign = "лев"
if (month == 8 and day >=23) or (month == 9 and day <=22):
    sign = "дева"
if (month == 9 and day >=23) or (month == 10 and day <=22):
    sign = "весы"
if (month == 10 and day >=23) or (month == 11 and day <=21):
    sign = "скорпион"
if (month == 11 and day >=22) or (month == 12 and day <=21):
    sign = "стрелец"
if (month == 12 and day >=22) or (month == 1 and day <=19):
    sign = "козерог"
print(f"ваш знак зодиака: {sign}")