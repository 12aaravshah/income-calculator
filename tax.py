TAX_YEARS = {
    2025: {
        "brackets": [
            (11_925, 0.10),
            (48_475, 0.12),
            (103_350, 0.22),
            (197_300, 0.24),
            (250_525, 0.32),
            (626_350, 0.35),
            (float("inf"), 0.37),
        ],
        "standard_deduction": 15_750,
        "ss_wage_base": 176_100,
    },
    2026: {
        "brackets": [
            (12_400, 0.10),
            (50_400, 0.12),
            (105_700, 0.22),
            (201_775, 0.24),
            (256_225, 0.32),
            (640_600, 0.35),
            (float("inf"), 0.37),
        ],
        "standard_deduction": 16_100,
        "ss_wage_base": 184_500,
    },
}
SS_RATE = 0.062
MEDICARE_RATE = 0.0145


def tax_owed(taxable_income, brackets):
    tax = 0
    lower = 0
    for upper, rate in brackets:
        if taxable_income > lower:
            amount_in_bracket = min(taxable_income, upper) - lower
            tax += amount_in_bracket * rate
        lower = upper
    return tax


def income_tax(gross, year):
    data = TAX_YEARS[year]
    taxable = max(gross - data["standard_deduction"], 0)
    return tax_owed(taxable, data["brackets"])


def fica_tax(gross, year):
    wage_base = TAX_YEARS[year]["ss_wage_base"]
    social_security = min(gross, wage_base) * SS_RATE
    medicare = gross * MEDICARE_RATE
    return social_security + medicare


def take_home(gross, year):
    return gross - income_tax(gross, year) - fica_tax(gross, year)


def gross_needed(target_take_home, year):
    low = target_take_home
    high = target_take_home * 2

    while take_home(high, year) < target_take_home:
        high = high * 2

    for _ in range(100):
        mid = (low + high) / 2
        if take_home(mid, year) < target_take_home:
            low = mid
        else:
            high = mid
    return round(high, 2)


print(round(take_home(50_000, 2026), 2))
print(round(take_home(100_000, 2026), 2))
print(round(take_home(50_000, 2025), 2))
print(gross_needed(42_355, 2026))
print(round(take_home(200_000, 2026), 2))