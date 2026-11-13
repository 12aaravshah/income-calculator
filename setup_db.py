import sqlite3
from tax_data import TAX_YEARS

conn = sqlite3.connect("calculator.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS tax_years")
cur.execute("DROP TABLE IF EXISTS brackets")

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

conn.commit()

print("tax_years table:")
for row in cur.execute("SELECT * FROM tax_years"):
    print(row)

print("2026 brackets:")
for row in cur.execute("SELECT upper_limit, rate FROM brackets WHERE year = 2026 ORDER BY rate"):
    print(row)

conn.close()