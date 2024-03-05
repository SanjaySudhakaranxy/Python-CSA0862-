purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount > 2000:
    discount_amount = 500
else:
    discount_amount = 0
final_price = purchase_amount - discount_amount
print("Final price:", final_price)
