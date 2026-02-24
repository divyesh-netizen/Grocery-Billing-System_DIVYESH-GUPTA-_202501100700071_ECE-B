prices = []
quantities = []
total = 0

print("Enter price of 5 items:")
for j in range(5):
    p = float(input(f"Prices :{j+1}: "))
    prices.append(p)

for i in range(0,5):
    q = int(input(f"unit[{i}] quantity: "))
    quantities.append(q)


for i in range(5):
    total += prices[i] * quantities[i]


discount = 0
if total > 100:
    discount = total * 0.10

final_amount = total - discount

print("Total amount =", total)
print("Discount =", discount)
print("Final Payable Amount =", final_amount)