print("Trend Growth Analyzer")

months = int(input("Enter months: "))

if months <= 0:
    print("Invalid months")
else:
    i = 0
    previous = 0
    growth = 0

    while i < months:
        value = int(input("Enter monthly value: "))

        if value > previous:
            growth = growth + 1

        previous = value
        i = i + 1

    print("Growth months:", growth)

    ratio = growth / months
    print("Growth ratio:", ratio)

    if ratio > 1:
        print("Impossible ratio")
