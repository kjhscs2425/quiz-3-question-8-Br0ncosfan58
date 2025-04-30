import json

# read `expenses.json`
with open("expenses.json", "r") as f:
    data = json.load(f)
# get and print total "price" for all expenses at the "pet store"
def total():
    for expense in data:
        if "price" in "pet store":
            total == expense("price")

print(total)