summa = float(input("введите сумму покупки: "))
age = int(input("введите возраст покупателя: "))
birthday = input("у вас егодня день рождения? (да/нет): ")
vip = input("вы являетесь VIP клиентом? (да/нет): ")
discount = 0
if summa > 1000:
    discount += 10
if age >= 63:
    discount += 5
if birthday.lower() == "да":
    discount += 5
if vip.lower() == "да":
    if 15 > discount:
        discount = 15
if discount > 25:
    discount = 25
final_summa = summa * (100 - discount) / 100
print(f"скидка: {discount}%")
print(f"итого к оплате: {final_summa:.2f} рублей")