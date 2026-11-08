age = int(input("сколько вам лет? "))
credit = float(input("запрашиваемый кредит? "))
months = int(input("на сколько месяцев вы планируете брать кредит? "))
income = float(input("сколько вы зарабатываете в месяц? "))
history = input("какая у вас кредитная история (отличная, хорошая, удовлетворительная, плохая)? ").strip().lower()
has_guarantor = input("есть ли у вас поручитель? (да/нет) ") == "да"
has_collateral = input("есть ли у вас залог? (да/нет) ") == "да"
ratio = credit / (income * months)
risk = "низкий"
if (age < 18) or (age > 63):
    risk = "критический"
elif ratio > 0.5:
    risk = "критический"
elif history == "плохая":
    risk = "высокий"
elif history == "удовлетворительная":
    risk = "средний"
elif ratio > 0.3:
    risk = "средний"
if (risk == "высокий") and (has_guarantor or has_collateral):
    risk = "средний"
elif (risk == "средний") and (has_guarantor and has_collateral):
    risk = "низкий"
if risk == "низкий":
    rate = 12.0
    decision = "одобрить"
elif risk == "средний":
    rate = 18.0
    decision = "одобрить"
elif risk == "высокий":
    rate = 24.0
    decision = "одобрить с ограничениями"
else:
    rate = None
    decision = "отклонить"
print(f"соотношение кредита к доходу: {ratio:.2f}")
print(f"категория риска: {risk}")
if rate is not None:
    print(f"процентная ставка: {rate:.1f}%")
print(f"рекомендация: {decision}")