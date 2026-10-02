import json
import pandas as pd
from pathlib import Path
import xml.etree.ElementTree as ET

from site_generator import generate_sites
from shipment_generator import generate_shipments
from enrollment_generator import generate_enrollments
from dispensing_generator import generate_dispensing
from inventory_generator import generate_inventory


# ==================================================
# PATHS
# ==================================================

BASE_PATH = Path("../landing")

SITE_PATH = BASE_PATH / "site_master"
SHIPMENT_PATH = BASE_PATH / "shipment_events"
INVENTORY_PATH = BASE_PATH / "inventory"
ENROLLMENT_PATH = BASE_PATH / "enrollment"
DISPENSING_PATH = BASE_PATH / "dispensing"

for path in [
    SITE_PATH,
    SHIPMENT_PATH,
    INVENTORY_PATH,
    ENROLLMENT_PATH,
    DISPENSING_PATH
]:
    path.mkdir(parents=True, exist_ok=True)


STATE_FILE = "generator_state.json"


# ==================================================
# STATE
# ==================================================

def load_state():

    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):

    with open(STATE_FILE, "w") as f:
        json.dump(
            state,
            f,
            indent=2
        )


# ==================================================
# WRITERS
# ==================================================

def write_csv(records, path):

    if not records:
        return

    pd.DataFrame(records).to_csv(
        path,
        index=False
    )


def write_parquet(records, path):

    if not records:
        return

    pd.DataFrame(records).to_parquet(
        path,
        index=False
    )


def write_json(records, path):

    if not records:
        return

    with open(path, "w") as f:
        json.dump(
            records,
            f,
            indent=2
        )


def write_xml(records, path):

    if not records:
        return

    root = ET.Element(
        "dispensing_records"
    )

    for row in records:

        record = ET.SubElement(
            root,
            "dispense"
        )

        for key, value in row.items():

            child = ET.SubElement(
                record,
                key
            )

            child.text = str(value)

    tree = ET.ElementTree(root)

    tree.write(
        path,
        encoding="utf-8",
        xml_declaration=True
    )


# ==================================================
# FILE NAMING
# ==================================================

def get_run_file_name(
    prefix,
    run_number,
    extension
):

    return (
        f"{prefix}_run_"
        f"{run_number:03}."
        f"{extension}"
    )


# ==================================================
# MAIN
# ==================================================

def main():

    state = load_state()

    run_number = state["run_number"] + 1

    print(
        f"\nStarting Run {run_number}"
    )

    # --------------------------------------
    # Site Master Snapshot
    # --------------------------------------

    sites = generate_sites(state)

    # --------------------------------------
    # Shipment CDC Events
    # --------------------------------------

    shipments = generate_shipments(state)

    # --------------------------------------
    # Enrollment Events
    # --------------------------------------

    enrollments = generate_enrollments(state)

    # --------------------------------------
    # Dispensing Events
    # --------------------------------------

    dispensings = generate_dispensing(state)

    # --------------------------------------
    # Inventory Snapshot
    # --------------------------------------

    inventory = generate_inventory(
        state,
        shipments,
        dispensings
    )

    # ==================================================
    # WRITE FILES
    # ==================================================

    write_csv(
        sites,
        SITE_PATH /
        get_run_file_name(
            "site_master",
            run_number,
            "csv"
        )
    )

    write_json(
        shipments,
        SHIPMENT_PATH /
        get_run_file_name(
            "shipment_events",
            run_number,
            "json"
        )
    )

    write_csv(
        inventory,
        INVENTORY_PATH /
        get_run_file_name(
            "inventory_snapshot",
            run_number,
            "csv"
        )
    )

    write_parquet(
        enrollments,
        ENROLLMENT_PATH /
        get_run_file_name(
            "enrollment",
            run_number,
            "parquet"
        )
    )

    write_xml(
        dispensings,
        DISPENSING_PATH /
        get_run_file_name(
            "dispensing",
            run_number,
            "xml"
        )
    )

    # ==================================================
    # UPDATE STATE
    # ==================================================

    from datetime import datetime, timedelta

    current_date = datetime.strptime(
        state["current_date"],
        "%Y-%m-%d"
    )

    state["current_date"] = (
        current_date + timedelta(days=1)
    ).strftime("%Y-%m-%d")

    state["run_number"] = run_number

    save_state(state)

    print(
        f"Run {run_number} completed"
    )

    print(
        f"Sites Snapshot: {len(sites)}"
    )

    print(
        f"Shipment Events: {len(shipments)}"
    )

    print(
        f"Enrollments: {len(enrollments)}"
    )

    print(
        f"Dispensing Events: {len(dispensings)}"
    )

    print(
        f"Inventory Rows: {len(inventory)}"
    )


if __name__ == "__main__":
    main()