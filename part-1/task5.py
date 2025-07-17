# List of purchase records: each is (customer name, amount spent)
purchases = [
    ("Alice", 120),
    ("Bob", 80),
    ("Alice", 50),
    ("Bob", 20),
    ("Clara", 200)
]

# Empty dictionary to accumulate totals per customer
totals = {}

# Go through each purchase record
for name, amount in purchases:
    # If this customer is already in our totals dict, add to their sum
    if name in totals:
        totals[name] += amount
    # If not, start their total with this amount
    else:
        totals[name] = amount

# Finally, print out how much each customer spent in total
for name, total in totals.items():
    print(f"{name} spent ${total}")