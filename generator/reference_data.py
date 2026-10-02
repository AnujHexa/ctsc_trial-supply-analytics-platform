from pathlib import Path
import pandas as pd


# ==================================================
# PATHS
# ==================================================

BASE_PATH = Path("../reference_data")

BASE_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# ==================================================
# DRUG MASTER
# ==================================================

drug_master = [
    {
        "drug_type": "DRUG_A",
        "drug_name": "Oncology Drug A",
        "shelf_life_days": 365,
        "reorder_threshold": 50,
        "unit_of_measure": "KITS"
    },
    {
        "drug_type": "DRUG_B",
        "drug_name": "Oncology Drug B",
        "shelf_life_days": 180,
        "reorder_threshold": 40,
        "unit_of_measure": "KITS"
    },
    {
        "drug_type": "DRUG_C",
        "drug_name": "Oncology Drug C",
        "shelf_life_days": 270,
        "reorder_threshold": 60,
        "unit_of_measure": "KITS"
    }
]


# ==================================================
# COUNTRY MASTER
# ==================================================

country_master = [
    {
        "country_code": "IN",
        "country_name": "India",
        "region": "APAC"
    },
    {
        "country_code": "SG",
        "country_name": "Singapore",
        "region": "APAC"
    },
    {
        "country_code": "DE",
        "country_name": "Germany",
        "region": "EMEA"
    },
    {
        "country_code": "US",
        "country_name": "United States",
        "region": "NA"
    }
]


# ==================================================
# DEPOT MASTER
# ==================================================

depot_master = [
    {
        "depot_id": "DEPOT001",
        "depot_name": "Mumbai Depot",
        "country_code": "IN",
        "region": "APAC"
    },
    {
        "depot_id": "DEPOT002",
        "depot_name": "Singapore Depot",
        "country_code": "SG",
        "region": "APAC"
    },
    {
        "depot_id": "DEPOT003",
        "depot_name": "Frankfurt Depot",
        "country_code": "DE",
        "region": "EMEA"
    }
]


# ==================================================
# WRITE FILES
# ==================================================

pd.DataFrame(drug_master).to_csv(
    BASE_PATH / "drug_master.csv",
    index=False
)

pd.DataFrame(country_master).to_csv(
    BASE_PATH / "country_master.csv",
    index=False
)

pd.DataFrame(depot_master).to_csv(
    BASE_PATH / "depot_master.csv",
    index=False
)

print("Reference data files created successfully.")