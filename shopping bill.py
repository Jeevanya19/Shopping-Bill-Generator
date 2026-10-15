
def calculate_discount(subtotal):
    if subtotal >= 1000:
        return subtotal * 0.10
    return 0


def calculate_tax(amount):
    return amount * 0.05


products = []

print("===== SHOPPING BILL GENERATOR =====")

while True:
    name = input("\nEnter product name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))

        if quantity <= 0 or price < 0:
            print("Invalid quantity or price. Try again.")
            continue

        total = quantity * price

        product = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": total
        }

        products.append(product)

    except ValueError:
        print("Please enter a valid quantity and price.")

if len(products) == 0:
    print("\nNo products added.")
else:
    subtotal = sum(product["total"] for product in products)
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount)
    final_amount = taxable_amount + tax

    print("\n========== SHOPPING BILL ==========")
    print(f"{'Product':<15}{'Qty':<6}{'Price':<10}{'Total':<10}")
    print("-----------------------------------")

    for product in products:
        print(
            f"{product['name']:<15}"
            f"{product['quantity']:<6}"
            f"{product['price']:<10.2f}"
            f"{product['total']:<10.2f}"
        )

    print("-----------------------------------")
    print(f"Subtotal:         Rs. {subtotal:.2f}")
    print(f"Discount:         Rs. {discount:.2f}")
    print(f"Tax (5%):         Rs. {tax:.2f}")
    print(f"Final Amount:     Rs. {final_amount:.2f}")
    print("===================================")
