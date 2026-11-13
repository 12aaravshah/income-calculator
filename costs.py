from tax import gross_needed
from cities import list_cities, get_city_costs

YEAR = 2026


def ask_number(question, default=None):
    while True:
        answer = input(question)
        if answer == "" and default is not None:
            return default
        try:
            number = float(answer)
        except ValueError:
            print("Please enter a number, like 1500.")
            continue
        if number < 0:
            print("Please enter 0 or more.")
            continue
        return number


def ask_city():
    cities = list_cities()
    print("Cities available:", ", ".join(cities))
    while True:
        name = input("Pick a city: ").strip()
        for city in cities:
            if city.lower() == name.lower():
                return city
        print("City not found. Try again.")


city = ask_city()
defaults = get_city_costs(city)

print("Press Enter to keep the default, or type your own MONTHLY cost.")
monthly_costs = {}
for category, default in defaults.items():
    monthly_costs[category] = ask_number(
        category + " [" + str(round(default)) + "]: ", default
    )

while True:
    savings_percent = ask_number("Percent of take-home to save (0 for none): ")
    if savings_percent < 100:
        break
    print("Savings percent must be below 100.")

yearly_costs = sum(monthly_costs.values()) * 12
take_home_needed = yearly_costs / (1 - savings_percent / 100)

print("City:", city)
print("Yearly costs:", round(yearly_costs, 2))
print("Take-home needed:", round(take_home_needed, 2))
print("Gross salary needed:", gross_needed(take_home_needed, YEAR))