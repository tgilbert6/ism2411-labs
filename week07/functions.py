# Self Assessment-----------
#
# 1. The first bug I spotted was the missing ":" in the first defined function. I found it from vscode pointing it out, but I also saw it in the traceback when I ran the function
# for the first time. I would have found it anyway. I think it tells me my debugging skills are fine at the moment, but maybe once it gets more complicated my ability
# to debug will crumble.
#
# 2. apply_discount(price, tier) uses the price and provided membership tier arguments to apply a membership discount. I think a colleague
# would be able to use it without reading the body because it is fairly straightforward.
#
# 3. The only AI usage was to check the Exercise 5 broken_sales.py after I had fixed it. No AI assisted/generated code is present in any material I am submitting. The
# AI usage did not shortcut anything, nor did it build my understanding. However, I do think it made me more confident in my debugging skills. Because of this, I think
# the AI usage was positive.
#
#----------------------------

# --- Exercise 1 ---
# Define a calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# -- Exercise 3 ---

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold") # used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price,tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# -- Exericse 6 ---

x = 100 # global

def double_it():
    x = 999 # local variable
    return x * 2

print(x) # 100
print(double_it()) # 1998
print(x) # 100

# Explanation: The output is what it is because the first time print(x) is ran, double_it() has not yet been called. So it would just return 100 because x = 100 and
# there were no other changes to it. The double_it() print does run the double_it() function, so the x variable changes to 999, as x was redefined in the function. Then it would
# multiply by two because of the return x * 2. The second print(x) still returns 100 because the previous variable redefining only applies within the bounds of the
# function, because defined variables within functions and such are local and not global. So it basically just reverts back to the global x value of 100.
# Because of this, the final output would be:
# 100
# 1998
# 100




###### Exercise 5 ---- broken_sales.py ---------

# broken_sales.py - trace and diagnose before fixing anything.
# comments are the original lines of code
# ai usage: only to check the code after I had completed it. no AI-generated code is present
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = total + sale # total = sale
print(f"Total: ${total}")

count = 0
for sale in sales: # for sale in sales
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #while i <= len(sales):
    print(sales[i])
    i += 1