import sqlite3
from tax_data import TAX_YEARS
from city_data import CITIES

conn = sqlite3.connect("calculator.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS tax_years")
cur.execute("DROP TABLE IF EXISTS brackets")
cur.execute("DROP TABLE IF EXISTS city_costs")
cur.execute("DROP TABLE IF EXISTS cities")

cur.execute("""
CREATE TABLE tax_years (
    year INTEGER PRIMARY KEY,
    standard_deduction REAL,
    ss_wage_base REAL
)
""")

cur.execute("""
CREATE TABLE brackets (
    year INTEGER,
    upper_limit REAL,
    rate REAL
)
""")

cur.execute("""
CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY,
    city TEXT,
    state TEXT
)
""")

cur.execute("""
CREATE TABLE city_costs (
    city_id INTEGER,
    category TEXT,
    monthly_cost REAL,
    source TEXT
)
""")

for year, data in TAX_YEARS.items():
    cur.execute(
        "INSERT INTO tax_years (year, standard_deduction, ss_wage_base) VALUES (?, ?, ?)",
        (year, data["standard_deduction"], data["ss_wage_base"]),
    )
    for upper, rate in data["brackets"]:
        if upper == float("inf"):
            upper = None
        cur.execute(
            "INSERT INTO brackets (year, upper_limit, rate) VALUES (?, ?, ?)",
            (year, upper, rate),
        )

for city, info in CITIES.items():
    cur.execute(
        "INSERT INTO cities (city, state) VALUES (?, ?)",
        (city, info["state"]),
    )
    city_id = cur.lastrowid
    for category, amount in info["costs"].items():
        cur.execute(
            "INSERT INTO city_costs (city_id, category, monthly_cost, source) VALUES (?, ?, ?, ?)",
            (city_id, category, amount, info["source"]),
        )

conn.commit()

print("cities table:")
for row in cur.execute("SELECT * FROM cities ORDER BY city_id"):
    print(row)

print("Austin costs (using a JOIN):")
for row in cur.execute("""
    SELECT city_costs.category, city_costs.monthly_cost
    FROM city_costs
    JOIN cities ON cities.city_id = city_costs.city_id
    WHERE cities.city = 'Austin'
    ORDER BY city_costs.rowid
"""):
    print(row)

conn.close()