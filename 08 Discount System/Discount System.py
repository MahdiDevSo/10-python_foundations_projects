# 8. Discount System
# Idea: Price discount rule

price = float(input("Price : "))

if price >= 100:
    print("Total Price : $", price - price * 0.2)
else:
    print("Total Price : $", price)
