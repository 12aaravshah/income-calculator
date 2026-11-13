from tax import gross_needed

YEAR = 2026

categories = ["rent", "groceries", "transport", "phone_internet", "shopping", "other"]


def ask_number(question):
    while True:
        answer = input(question)
        try:
            number = float(answer)
        except ValueError:
            print("Please enter a number, like 1500.")
            continue
        if number < 0:
            print("Please enter 0 or more.")
            continue
        return number


print("Enter your MONTHLY costs in dollars.")

monthly_costs = {}
for category in categories:
    monthly_costs[category] = ask_number(category + ": ")

while True:
    savings_percent = ask_number("Percent of take-home to save (0 for none): ")
    if savings_percent < 100:
        break
    print("Savings percent must be below 100.")

yearly_costs = sum(monthly_costs.values()) * 12
take_home_needed = yearly_costs / (1 - savings_percent / 100)

print("Yearly costs:", round(yearly_costs, 2))
print("Take-home needed:", round(take_home_needed, 2))
print("Gross salary needed:", gross_needed(take_home_needed, YEAR))