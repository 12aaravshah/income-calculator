import sqlite3

DB_FILE = "calculator.db"


def list_cities():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT city FROM cities ORDER BY city")
    names = []
    for row in cur.fetchall():
        names.append(row[0])
    conn.close()
    return names


def get_city_costs(city):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT city_costs.category, city_costs.monthly_cost
        FROM city_costs
        JOIN cities ON cities.city_id = city_costs.city_id
        WHERE cities.city = ?
        ORDER BY city_costs.rowid
        """,
        (city,),
    )
    costs = {}
    for category, amount in cur.fetchall():
        costs[category] = amount
    conn.close()
    return costs



def get_all_city_totals():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT cities.city, cities.state, SUM(city_costs.monthly_cost) AS monthly_total
        FROM cities
        JOIN city_costs ON city_costs.city_id = cities.city_id
        GROUP BY cities.city_id
        ORDER BY monthly_total
        """
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def get_city_state(city):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT state FROM cities WHERE city = ?", (city,))
    state = cur.fetchone()[0]
    conn.close()
    return state