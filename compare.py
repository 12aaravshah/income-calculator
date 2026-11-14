from tax import gross_needed
from cities import get_all_city_totals, tax_codes

YEAR = 2026
SAVINGS_PERCENT = 20

rows = get_all_city_totals()

results = []
for city, state, local_tax, monthly_total in rows:
    taxes = tax_codes(state, local_tax)
    yearly_costs = monthly_total * 12
    take_home_needed = yearly_costs / (1 - SAVINGS_PERCENT / 100)
    gross_federal = gross_needed(take_home_needed, YEAR)
    gross_with_taxes = gross_needed(take_home_needed, YEAR, taxes)
    results.append((city, state, monthly_total, gross_federal, gross_with_taxes))

results.sort(key=lambda r: r[4])

print("Saving", SAVINGS_PERCENT, "percent, default costs, year", YEAR)
print()
print(f"{'Rank':<5} {'City':<18} {'Monthly costs':>13} {'Federal only':>13} {'State/city tax':>14} {'Gross needed':>13}")
for i, (city, state, monthly_total, gross_federal, gross_with_taxes) in enumerate(results, start=1):
    label = city + ", " + state
    extra = gross_with_taxes - gross_federal
    print(f"{i:<5} {label:<18} {monthly_total:>13,.0f} {gross_federal:>13,.2f} {extra:>14,.2f} {gross_with_taxes:>13,.2f}")