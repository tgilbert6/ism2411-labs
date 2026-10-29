# inventory.py
# Author: tgilbert
# Module 10 Lab: Inventory List Manager

# Self Reflection ----------
#
# 1) I did not think python would have two types of lists. I figured that you could prevent overwriting by just copying a list as a backup, but tuples do this better.
# Otherwise, they work the same way I would expect but I did not know a step could be specified.
#
# 2) I have not been in a position like this, but an instance this would be better than Excel would be if I was working with a constantly changing dataset. As
# discussed in class, sometimes there are millions of transactions going through at once and there is no way Excel would be able to handle that as fast or as easily. The
# most rows I've ever seen in Excel was around 30,000 and even then I was having some trouble loading it. This would be especially true during high volume days such as before
# a holiday and if I needed to see more than half a second of data.
#
# ---------------------------

print("--- Exercise 1: Build the list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2 # calculate the index of the middle item
print(inventory[middle]) # middle item



print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item

print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope")

print(inventory)
inventory.remove("tape")
print(inventory)
# inventory.append("Zoo")
# inventory.append("zoo")
# inventory.append("Apple")
# inventory.append("1")
# inventory.append("11")
# inventory.append("%")
# inventory.append("4")
# inventory.append("-")
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2))

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: ~{sum(high_sales) / len(high_sales):.2f}")