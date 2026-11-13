from tax import gross_needed

YEAR = 2026

monthly_costs = {
    "rent": 2500,
    "groceries": 400,
    "transport": 150,
    "phone_internet": 100,
    "shopping": 200,
    "other": 150,
}

yearly_costs = 0
for item, amount in monthly_costs.items():
    yearly_costs = yearly_costs + amount * 12

print("Yearly costs:", yearly_costs)
print("Gross salary needed:", gross_needed(yearly_costs, YEAR))