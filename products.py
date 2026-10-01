total = 0
products = []

while True:
    name = input("Enter product name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    price = float(input("Enter product price: "))
    products.append({"name": name, "price": price})
    total += price 
    print("Product added successfully!\n")
for p in products:
    print(f"Product: {p['name']}, Price: ${p['price']:.2f}")
print(f"Total: ${total:.2f}")