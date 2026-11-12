# Each bracket is (upper_limit, rate).
# These are TEST numbers, not real IRS brackets. We'll swap in real ones later.
TEST_BRACKETS = [
    (10_000, 0.10),
    (40_000, 0.20),
    (float("inf"), 0.30),
]

def tax_owed(taxable_income, brackets):
    tax = 0
    lower = 0
    for upper, rate in brackets:
        if taxable_income > lower:
            amount_in_bracket = min(taxable_income, upper) - lower
            tax += amount_in_bracket * rate
        lower = upper
    return tax

print(tax_owed(50_000, TEST_BRACKETS))