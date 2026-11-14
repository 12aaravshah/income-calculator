from tax import local_income_tax

for code in ["FL", "WA", "GA", "NC", "AZ", "CO", "MA", "MN", "DC"]:
    print(code, round(local_income_tax(100_000, code, 2026), 2))