total_bill_amount = float(input("Total bill amount? $"))
service_level = input("Leve of service? (good/fair/bad)").lower()
tip_percentages = { 'good': 0.20, 'fair': 0.15, 'bad': .10}
if service_level in tip_percentages:
    tip_amount = total_bill_amount * tip_percentages[service_level]
    total_bill_amount = total_bill_amount + tip_amount
    print("Tip amount: ${:.2f}".format(tip_amount))
    print("Total amount: ${:.2f}".format(total_bill_amount))
else:
    print("invalid service level. Please enter 'good', 'fair', or 'bad'.")