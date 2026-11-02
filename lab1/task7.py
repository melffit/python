price = 24.99
extra_minutes = 0
extra_sms = 0
extra_mb = 0
minutes = int(input("введите количество израсходованных минут за месяц: "))
sms = int(input("введите количество отправленных смс-сообщений за месяц: "))
mb = int(input("введите количество израсходованных мб за месяц: "))
if minutes > 60:
    extra_minutes = (minutes - 60) * 0.89
if sms > 30:
    extra_sms = (sms - 30) * 0.59
if mb > 1024:
    extra_mb = (mb - 1024) * 0.79
total_price = price + extra_minutes + extra_sms + extra_mb
tax = total_price * 0.02
total = total_price + tax
print(f"цена тарифа: {price}")
if extra_minutes != 0:
    print(f"дополнительные минуты: {extra_minutes:.2f}")
if extra_sms != 0:
    print(f"дополнительные смс-сообщения: {extra_sms:.2f}")
if extra_mb != 0:
    print(f"дополнительные мб: {extra_mb:.2f}")
print(f"общая сумма: {total_price:.2f}")
print(f"налог: {tax:.2f}")
print(f"итоговая цена к оплате: {total:.2f}")