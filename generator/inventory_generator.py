from datetime import date
import random


DRUG_TYPES = [
    "DRUG_A",
    "DRUG_B",
    "DRUG_C"
]


def initialize_inventory(state):

    for site in state["sites"]:

        for drug in DRUG_TYPES:

            key = f"{site['site_id']}_{drug}"

            if key not in state["inventory"]:

                state["inventory"][key] = {
                    "qty_on_hand": random.randint(50, 100)
                }


def apply_delivered_shipments(
    state,
    shipment_events
):

    for shipment in shipment_events:

        if shipment["shipment_status"] != "DELIVERED":
            continue

        key = (
            f"{shipment['destination_site_id']}"
            f"_{shipment['drug_type']}"
        )

        state["inventory"][key]["qty_on_hand"] += (
            shipment["qty_shipped"]
        )


def apply_dispensing(
    state,
    dispensing_events
):

    for dispense in dispensing_events:

        key = (
            f"{dispense['site_id']}"
            f"_{dispense['drug_type']}"
        )

        if key not in state["inventory"]:
            continue

        state["inventory"][key]["qty_on_hand"] -= (
            dispense["quantity_dispensed"]
        )


def generate_inventory(
    state,
    shipment_events,
    dispensing_events
):

    initialize_inventory(state)

    apply_delivered_shipments(
        state,
        shipment_events
    )

    apply_dispensing(
        state,
        dispensing_events
    )

    snapshots = []

    snapshot_id = (
        f"INV{state['run_number'] + 1:05}"
    )

    for site in state["sites"]:

        for drug in DRUG_TYPES:

            key = f"{site['site_id']}_{drug}"

            qty = state["inventory"][key]["qty_on_hand"]

            expired_qty = 0
            adjustment_qty = 0

            if random.random() < 0.05:

                expired_qty = random.randint(
                    1,
                    5
                )

                qty -= expired_qty

                qty = max(0, qty)

            if random.random() < 0.03:

                adjustment_qty = random.randint(
                    -3,
                    3
                )

                qty = max(
                    0,
                    qty + adjustment_qty
                )

            state["inventory"][key][
                "qty_on_hand"
            ] = qty

            record = {

                "inventory_snapshot_id":
                    snapshot_id,

                "snapshot_date":
                    state["current_date"],
                    
                "site_id":
                    site["site_id"],

                "study_id":
                    site["study_id"],

                "drug_type":
                    drug,

                "qty_on_hand":
                    qty,

                "qty_reserved":
                    random.randint(
                        0,
                        10
                    ),

                "qty_expired":
                    expired_qty,

                "inventory_adjustment":
                    adjustment_qty
            }

            # controlled dirty data
            if (
                state["run_number"] > 5
                and random.random() < 0.01
            ):
                record["qty_on_hand"] = -1

            snapshots.append(record)

    return snapshots