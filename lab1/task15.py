sales = []
while True:
    product = input("введите название товара(или 'стоп', если хотите остановть запись): ")
    if product == "стоп":
        break
    price = float(input("цена: "))
    quantity = int(input("количество: "))
    sales.append({"product": product, "price": price, "quantity": quantity})
revenue = {}
for item in sales:
    product = item["product"]
    item_revenue = item["price"] * item["quantity"]
    revenue[product] = revenue.get(product, 0) + item_revenue
print("выручка:")
for product, rev in revenue.items():
    print(f"  {product}: {rev}")
most_profitable = max(revenue, key=revenue.get)
print(f"самый прибыльный товар: {most_profitable}")
unique_count = len(revenue)
print(f"количество уникальных товаров: {unique_count}")