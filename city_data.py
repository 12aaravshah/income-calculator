# Yearly costs for one adult with no children, copied from the MIT Living Wage
# Calculator (livingwage.mit.edu), metro area pages, data updated Feb 15, 2026.
# The yearly amounts are divided by 12 when the database is built.
# MIT categories -> ours: Housing = rent, Food = groceries,
# Transportation = transport, Internet & Mobile = phone_internet,
# Medical = health_care, Civic = civic_entertainment, Other = other.
# Child care is $0 for one adult, so it is left out.

SOURCE = (
    "MIT Living Wage Calculator (livingwage.mit.edu), 1 adult 0 children, "
    "metro area, data updated Feb 15 2026, yearly amount divided by 12"
)

CITIES = {
    "Austin": {
        "state": "TX",
        "source": SOURCE,
        "costs": {
            "rent": 17779,
            "groceries": 4047,
            "transport": 9016,
            "phone_internet": 1509,
            "health_care": 3075,
            "civic_entertainment": 2583,
            "other": 4067,
        },
    },
    "Houston": {
        "state": "TX",
        "source": SOURCE,
        "costs": {
            "rent": 15276,
            "groceries": 3895,
            "transport": 8856,
            "phone_internet": 1652,
            "health_care": 3240,
            "civic_entertainment": 2583,
            "other": 4067,
        },
    },
    "Dallas": {
        "state": "TX",
        "source": SOURCE,
        "costs": {
            "rent": 18416,
            "groceries": 4131,
            "transport": 9103,
            "phone_internet": 1442,
            "health_care": 3038,
            "civic_entertainment": 2583,
            "other": 4067,
        },
    },
    "New York": {
        "state": "NY",
        "local_tax": "NYC",
        "source": SOURCE,
        "costs": {
            "rent": 26341,
            "groceries": 4965,
            "transport": 7254,
            "phone_internet": 1510,
            "health_care": 4375,
            "civic_entertainment": 3456,
            "other": 4715,
        },
    },
    "Chicago": {
        "state": "IL",
        "source": SOURCE,
        "costs": {
            "rent": 17251,
            "groceries": 4627,
            "transport": 8162,
            "phone_internet": 1747,
            "health_care": 3595,
            "civic_entertainment": 3347,
            "other": 4549,
        },
    },
    "San Francisco": {
        "state": "CA",
        "source": SOURCE,
        "costs": {
            "rent": 27462,
            "groceries": 5313,
            "transport": 8939,
            "phone_internet": 1947,
            "health_care": 3798,
            "civic_entertainment": 3876,
            "other": 4992,
        },
    },
    "Los Angeles": {
        "state": "CA",
        "source": SOURCE,
        "costs": {
            "rent": 24894,
            "groceries": 4503,
            "transport": 8809,
            "phone_internet": 1513,
            "health_care": 3251,
            "civic_entertainment": 3876,
            "other": 4992,
        },
    },
    "Miami": {
        "state": "FL",
        "source": SOURCE,
        "costs": {
            "rent": 21584,
            "groceries": 4832,
            "transport": 7706,
            "phone_internet": 2068,
            "health_care": 2770,
            "civic_entertainment": 2583,
            "other": 4067,
        },
    },
    "Seattle": {
        "state": "WA",
        "source": SOURCE,
        "costs": {
            "rent": 23247,
            "groceries": 5012,
            "transport": 8850,
            "phone_internet": 2225,
            "health_care": 3049,
            "civic_entertainment": 3876,
            "other": 4992,
        },
    },
    "Atlanta": {
        "state": "GA",
        "source": SOURCE,
        "costs": {
            "rent": 18958,
            "groceries": 4581,
            "transport": 9350,
            "phone_internet": 1686,
            "health_care": 3104,
            "civic_entertainment": 2583,
            "other": 4067,
        },
    },
    "Denver": {
        "state": "CO",
        "source": SOURCE,
        "costs": {
            "rent": 19817,
            "groceries": 4666,
            "transport": 8188,
            "phone_internet": 2032,
            "health_care": 3199,
            "civic_entertainment": 3876,
            "other": 4992,
        },
    },
    "Phoenix": {
        "state": "AZ",
        "source": SOURCE,
        "costs": {
            "rent": 17574,
            "groceries": 4167,
            "transport": 8633,
            "phone_internet": 1817,
            "health_care": 3008,
            "civic_entertainment": 3876,
            "other": 4992,
        },
    },
    "Boston": {
        "state": "MA",
        "source": SOURCE,
        "costs": {
            "rent": 26094,
            "groceries": 5016,
            "transport": 8165,
            "phone_internet": 2199,
            "health_care": 4125,
            "civic_entertainment": 3456,
            "other": 4715,
        },
    },
    "Minneapolis": {
        "state": "MN",
        "source": SOURCE,
        "costs": {
            "rent": 14906,
            "groceries": 4913,
            "transport": 8763,
            "phone_internet": 1592,
            "health_care": 3468,
            "civic_entertainment": 3347,
            "other": 4549,
        },
    },
    "Washington": {
        "state": "DC",
        "source": SOURCE,
        "costs": {
            "rent": 23266,
            "groceries": 4998,
            "transport": 8201,
            "phone_internet": 1934,
            "health_care": 3500,
            "civic_entertainment": 2583,
            "other": 4067,
        },
    },
    "Charlotte": {
        "state": "NC",
        "source": SOURCE,
        "costs": {
            "rent": 16473,
            "groceries": 4478,
            "transport": 8895,
            "phone_internet": 1514,
            "health_care": 3465,
            "civic_entertainment": 2583,
            "other": 4067,
        },
    },
}