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

def take_home(gross, brackets):
    return gross - tax_owed(gross, brackets)

def gross_needed(target_take_home, brackets):
    low = target_take_home        # you can't need less gross than your take-home
    high = target_take_home * 2   # a first upper guess

    # If the upper guess is still too low, keep doubling it
    while take_home(high, brackets) < target_take_home:
        high = high * 2

    # Repeatedly guess the middle and shrink the range
    for _ in range(100):
        mid = (low + high) / 2
        if take_home(mid, brackets) < target_take_home:
            low = mid     # take-home too low, so the answer is higher
        else:
            high = mid    # take-home high enough, so the answer is lower or equal
    return round(high, 2)

print(gross_needed(33_000, TEST_BRACKETS))