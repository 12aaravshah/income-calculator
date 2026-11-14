import sqlite3

SS_RATE = 0.062
MEDICARE_RATE = 0.0145
DB_FILE = "calculator.db"

_cache = {}


def load_tax_data(year):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(
        "SELECT standard_deduction, ss_wage_base FROM tax_years WHERE year = ?",
        (year,),
    )
    row = cur.fetchone()
    if row is None:
        conn.close()
        raise ValueError("No tax data for year " + str(year))
    standard_deduction, ss_wage_base = row

    brackets = []
    for upper, rate in cur.execute(
        "SELECT upper_limit, rate FROM brackets WHERE year = ? ORDER BY rate",
        (year,),
    ):
        if upper is None:
            upper = float("inf")
        brackets.append((upper, rate))

    conn.close()
    return {
        "standard_deduction": standard_deduction,
        "ss_wage_base": ss_wage_base,
        "brackets": brackets,
    }


def get_tax_data(year):
    if year not in _cache:
        _cache[year] = load_tax_data(year)
    return _cache[year]


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
    data = get_tax_data(year)
    taxable = max(gross - data["standard_deduction"], 0)
    return tax_owed(taxable, data["brackets"])


def fica_tax(gross, year):
    wage_base = get_tax_data(year)["ss_wage_base"]
    social_security = min(gross, wage_base) * SS_RATE
    medicare = gross * MEDICARE_RATE
    return social_security + medicare

_rules_cache = {}


def load_tax_rules(code, year):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(
        "SELECT deduction, credit FROM tax_rules WHERE code = ? AND year = ?",
        (code, year),
    )
    row = cur.fetchone()
    if row is None:
        conn.close()
        raise ValueError("No tax data for " + code + " in " + str(year))
    deduction, credit = row

    brackets = []
    for upper, rate in cur.execute(
        "SELECT upper_limit, rate FROM tax_brackets WHERE code = ? AND year = ? ORDER BY rate",
        (code, year),
    ):
        if upper is None:
            upper = float("inf")
        brackets.append((upper, rate))

    conn.close()
    return {"deduction": deduction, "credit": credit, "brackets": brackets}


def get_tax_rules(code, year):
    key = (code, year)
    if key not in _rules_cache:
        _rules_cache[key] = load_tax_rules(code, year)
    return _rules_cache[key]


def local_income_tax(gross, code, year):
    rules = get_tax_rules(code, year)
    taxable = max(gross - rules["deduction"], 0)
    tax = tax_owed(taxable, rules["brackets"]) - rules["credit"]
    return max(tax, 0)


def take_home(gross, year, places=()):
    result = gross - income_tax(gross, year) - fica_tax(gross, year)
    for code in places:
        result = result - local_income_tax(gross, code, year)
    return result


def gross_needed(target_take_home, year, places=()):
    low = target_take_home
    high = target_take_home * 2

    while take_home(high, year, places) < target_take_home:
        high = high * 2

    for _ in range(100):
        mid = (low + high) / 2
        if take_home(mid, year, places) < target_take_home:
            low = mid
        else:
            high = mid
    return round(high, 2)


if __name__ == "__main__":
    print(round(take_home(50_000, 2026), 2))
    print(round(take_home(100_000, 2026), 2))
    print(round(take_home(50_000, 2025), 2))
    print(gross_needed(42_355, 2026))
    print(round(take_home(200_000, 2026), 2))
    print(round(local_income_tax(100_000, "TX", 2026), 2))
    print(round(local_income_tax(100_000, "IL", 2026), 2))
    print(round(local_income_tax(100_000, "NY", 2026), 2))
    print(round(local_income_tax(100_000, "CA", 2026), 2))
    print(round(local_income_tax(100_000, "NYC", 2026), 2))