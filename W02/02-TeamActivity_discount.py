

from datetime import datetime
print()
subtotal = float(input("Please enter the subtotal: "))
#sales_tax_amount = 0.06 * subtotal 
day_of_week = datetime.now().weekday()
discount = 0
day_of_week = 2

if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50: 
   discount = subtotal * 0.1
   subtotal = subtotal * 0.9
      
sales_tax_amount = subtotal * 0.06
if discount > 0:
    print(f"Discount amount: {discount:.2f}")
print(f"Sales tax amount: {sales_tax_amount:.2f}")

total = subtotal + sales_tax_amount
print(f"Total: {total:.2f}")
print()

