from tax import gross_needed


def salary_needed(monthly_total, savings_percent, taxes, year):
    yearly_costs = monthly_total * 12
    take_home_needed = yearly_costs / (1 - savings_percent / 100)
    gross_federal = gross_needed(take_home_needed, year)
    gross_with_taxes = gross_needed(take_home_needed, year, taxes)
    return take_home_needed, gross_federal, gross_with_taxes