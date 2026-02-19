print("Trend Growth Analyzer")

months = int(input("Enter months: "))
i = 0
previous = 0
growth = 0

while i < months:
value = int(input("Enter monthly value: "))  
# Mistake 1: Indentation Error (value should be inside while loop)

if value > previous:
    growth = growth + 1

previous = value
i = i + 1

print("Growth months:", growth)

ratio = growth / months

print("Growth ratio:", ratio  
# Mistake 2: Missing closing bracket ) → Syntax Error

if ratio > 1:
    print("Impossible ratio")
    # Mistake 3: Logical mistake (ratio cannot be greater than 1)

if months < 0:
    print("Invalid months")
    # Mistake 4: Wrong place for validation (should check before loop)
