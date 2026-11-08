amount = int(input("введите сумму(целое число): "))
count100 = amount // 100
rest = amount % 100
count50 = rest // 50
rest = rest % 50
count10 = rest // 10
rest = rest % 10
count5 = rest // 5
rest = rest % 5
count2= rest // 2
rest = rest % 2
count1 = rest // 1
rest = rest % 1
print(f"купюр по 100: {count100}")
print(f"купюр по 50: {count50}")
print(f"купюр по 10: {count10}")
print(f"купюр по 5: {count5}")
print(f"монет по 2: {count2}")
print(f"монет по 1: {count1}")