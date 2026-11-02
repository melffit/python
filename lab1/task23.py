incomes = {}
expenses = {}
while True:
    print("\n1-доход, 2-расход, 3-анализ, 4-рекомендации, 5-цель, 0-выход")
    choice = input("выбор: ")
    if choice == "1":
        name = input("источник: ")
        amount = float(input("сумма: "))
        incomes[name] = incomes.get(name, 0) + amount
    elif choice == "2":
        category = input("категория: ")
        amount = float(input("сумма: "))
        expenses[category] = expenses.get(category, 0) + amount
    elif choice == "3":
        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        print(f"\nдоходы: {total_income}")
        print(f"расходы: {total_expense}")
        print(f"баланс: {total_income - total_expense}")
        for cat, amount in expenses.items():
            percent = amount / total_expense * 100 if total_expense > 0 else 0
            print(f"  {category}: {amount} ₽ ({percent:.1f}%)")
    elif choice == "4":
        if expenses:
            max_cat = max(expenses, key=expenses.get)
            print(f"\nсамая большая статья: {max_cat} ({expenses[max_cat]})")
            print(f"попробуйте сократить на {expenses[max_cat] * 0.1:.0f}")
    elif choice == "5":
        goal = input("цель: ")
        target = float(input("сколько нужно: "))
        saving = sum(incomes.values()) - sum(expenses.values())
        if saving > 0:
            months = target / saving
            print(f"накопите за {months:.1f} месяцев")
        else:
            print("нет свободных денег!")
    elif choice == "0":
        break