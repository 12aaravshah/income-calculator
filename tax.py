# TEST numbers, not real IRS numbers. We'll swap in real ones later.
TEST_BRACKETS = [
    (10_000, 0.10),
    (40_000, 0.20),
    (float("inf"), 0.30),
]
STANDARD_DEDUCTION = 10_000
SS_RATE = 0.062
MEDICARE_RATE = 0.0145
SS_WAGE_BASE = 100_000


def tax_owed(taxable_income, brackets):
    tax = 0
    lower = 0
    for upper, rate in brackets:
        if taxable_income > lower:
            amount_in_bracket = min(taxable_income, upper) - lower
            tax += amount_in_bracket * rate
        lower = upper
    return tax


def income_tax(gross, brackets):
    taxable = max(gross - STANDARD_DEDUCTION, 0)
    return tax_owed(taxable, brackets)


def fica_tax(gross):
    social_security = min(gross, SS_WAGE_BASE) * SS_RATE
    medicare = gross * MEDICARE_RATE
    return social_security + medicare


def take_home(gross, brackets):
    return gross - income_tax(gross, brackets) - fica_tax(gross)


def gross_needed(target_take_home, brackets):
    low = target_take_home
    high = target_take_home * 2

    while take_home(high, brackets) < target_take_home:
        high = high * 2

    for _ in range(100):
        mid = (low + high) / 2
        if take_home(mid, brackets) < target_take_home:
            low = mid
        else:
            high = mid
    return round(high, 2)


print(round(take_home(50_000, TEST_BRACKETS), 2))
print(round(take_home(10_000, TEST_BRACKETS), 2))
print(gross_needed(39_175, TEST_BRACKETS))