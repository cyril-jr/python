def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
price = float(input("Enter the pric: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print(f"The final price is : {final_price}")