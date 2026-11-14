import streamlit as st

from calculator import salary_needed
from cities import (
    list_cities,
    get_city_costs,
    get_city_taxes,
    get_all_city_totals,
    tax_codes,
)

YEAR = 2026

st.set_page_config(page_title="Salary Needed Calculator")

st.title("What salary do you need?")
st.write(
    "Pick a city, adjust your monthly costs, and see the gross salary you "
    "would need. Includes federal income tax, Social Security and Medicare, "
    "and state and city income tax. Tax year "
    + str(YEAR)
    + ", single filer."
)

city = st.selectbox("City", list_cities())
taxes = get_city_taxes(city)
defaults = get_city_costs(city)

st.subheader("Monthly costs")
monthly_costs = {}
for category, default in defaults.items():
    monthly_costs[category] = st.number_input(
        category.replace("_", " ").capitalize(),
        min_value=0,
        value=int(round(default)),
        step=25,
        key=city + "_" + category,
    )

savings_percent = st.slider("Percent of take-home to save", 0, 60, 20)

monthly_total = sum(monthly_costs.values())
take_home_needed, gross_federal, gross_with_taxes = salary_needed(
    monthly_total, savings_percent, taxes, YEAR
)

st.subheader("Result")
col1, col2 = st.columns(2)
col1.metric("Gross salary needed", f"${gross_with_taxes:,.0f}")
col2.metric("Take-home needed", f"${take_home_needed:,.0f}")
st.caption("Taxes included: federal, FICA, " + " + ".join(taxes) + ".")

st.subheader("All cities, default costs")
rows = []
for name, state, local_tax, total in get_all_city_totals():
    _, _, gross = salary_needed(
        total, savings_percent, tax_codes(state, local_tax), YEAR
    )
    rows.append({"city": name + ", " + state, "monthly": total, "gross": gross})
rows.sort(key=lambda r: r["gross"])

lines = [
    "| Rank | City | Monthly costs | Gross salary needed |",
    "|---|---|---|---|",
]
for rank, r in enumerate(rows, start=1):
    lines.append(
        f"| {rank} | {r['city']} | \\${r['monthly']:,.0f} | \\${r['gross']:,.0f} |"
    )
st.markdown("\n".join(lines))

biggest = rows[-1]["gross"]
for r in rows:
    st.progress(r["gross"] / biggest, text=r["city"] + ": " + f"\\${r['gross']:,.0f}")