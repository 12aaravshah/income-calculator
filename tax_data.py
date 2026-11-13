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