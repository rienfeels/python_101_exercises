total_bill = float(input("Total bill amount? $"))

service_level = input("Level of service? (good/fair/bad) ").lower()

tip_percentages = {'good': 0.20, 'fair': 0.15, 'bad': 0.10}

if service_level in tip_percentages:
    tip_amount = total_bill * tip_percentages[service_level]
    total_amount = total_bill + tip_amount

    num_people = int(input("Split how many ways? "))

    if num_people > 0:
        amount_per_person = total_amount / num_people

        print("Tip amount: ${:.2f}".format(tip_amount))
        print("Total amount: ${:.2f}".format(total_amount))
        print("Amount per person: ${:.2f}".format(amount_per_person))
    else:
        print("Invalid number of people. Please enter a positive integer.")
else:
    print("Invalid service level. Please enter 'good', 'fair', or 'bad'.")
