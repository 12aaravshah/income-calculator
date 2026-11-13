from tax import gross_needed
from cities import get_all_city_totals

YEAR = 2026
SAVINGS_PERCENT = 20

rows = get_all_city_totals()

results = []
for city, state, monthly_total in rows:
    yearly_costs = monthly_total * 12
    take_home_needed = yearly_costs / (1 - SAVINGS_PERCENT / 100)
    gross = gross_needed(take_home_needed, YEAR)
    results.append((city, state, monthly_total, gross))

results.sort(key=lambda r: r[3])

print("Saving", SAVINGS_PERCENT, "percent, default costs, year", YEAR)
print()
print(f"{'Rank':<5} {'City':<18} {'Monthly costs':>13}   {'Gross salary needed':>19}")
for i, (city, state, monthly_total, gross) in enumerate(results, start=1):
    label = city + ", " + state
    print(f"{i:<5} {label:<18} {monthly_total:>13,.0f}   {gross:>19,.2f}")