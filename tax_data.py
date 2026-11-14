# Source data used to fill the database.
# Federal brackets and standard deduction: irs.gov. Social Security wage base: ssa.gov.
TAX_YEARS = {
    2025: {
        "brackets": [
            (11_925, 0.10),
            (48_475, 0.12),
            (103_350, 0.22),
            (197_300, 0.24),
            (250_525, 0.32),
            (626_350, 0.35),
            (float("inf"), 0.37),
        ],
        "standard_deduction": 15_750,
        "ss_wage_base": 176_100,
    },
    2026: {
        "brackets": [
            (12_400, 0.10),
            (50_400, 0.12),
            (105_700, 0.22),
            (201_775, 0.24),
            (256_225, 0.32),
            (640_600, 0.35),
            (float("inf"), 0.37),
        ],
        "standard_deduction": 16_100,
        "ss_wage_base": 184_500,
    },
}


# Income tax for states and cities, single filer, wages only.
# Each place has a short code: a state's postal code, or "NYC".
# Sources: CA - Franchise Tax Board, Tax News October 2026 (2026 Schedule X).
#          NY and NYC - NYS Dept. of Taxation and Finance, Form IT-2105-I (2026).
#          IL - Illinois Dept. of Revenue (4.95% flat; 2026 exemption $2,925).
#          TX - no state income tax.
# "deduction" is subtracted from income before the brackets apply.
# "credit" is subtracted from the tax after the brackets apply.
INCOME_TAX = {
    2026: {
        "TX": {"brackets": [(float("inf"), 0.0)], "deduction": 0, "credit": 0},
        "IL": {"brackets": [(float("inf"), 0.0495)], "deduction": 2_925, "credit": 0},
        "NY": {
            "brackets": [
                (8_500, 0.039),
                (11_700, 0.044),
                (13_900, 0.0515),
                (80_650, 0.054),
                (215_400, 0.059),
                (1_077_550, 0.0685),
                (5_000_000, 0.0965),
                (25_000_000, 0.103),
                (float("inf"), 0.109),
            ],
            "deduction": 8_000,
            "credit": 0,
        },
        "NYC": {
            "brackets": [
                (12_000, 0.03078),
                (25_000, 0.03762),
                (50_000, 0.03819),
                (float("inf"), 0.03876),
            ],
            "deduction": 8_000,
            "credit": 0,
        },
        "CA": {
            "brackets": [
                (11_456, 0.01),
                (27_157, 0.02),
                (42_861, 0.04),
                (59_498, 0.06),
                (75_197, 0.08),
                (384_109, 0.093),
                (460_927, 0.103),
                (768_213, 0.113),
                (float("inf"), 0.123),
            ],
            "deduction": 5_900,
            "credit": 158,
        },
    },
}