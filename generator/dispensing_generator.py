from datetime import date
import random


DRUG_TYPES = [
    "DRUG_A",
    "DRUG_B",
    "DRUG_C"
]


def generate_dispensing(state):

    active_patients = [

        p for p in state["patients"]

        if p["patient_status"] == "ACTIVE"
    ]

    if not active_patients:
        return []

    events = []

    dispense_count = min(
        len(active_patients),
        random.randint(1, 5)
    )

    selected_patients = random.sample(
        active_patients,
        dispense_count
    )

    for patient in selected_patients:

        state["counters"]["dispense"] += 1

        qty = random.choice([
            5,
            10,
            15
        ])

        record = {

            "dispense_id":
                f"DSP{state['counters']['dispense']:06}",

            "patient_id":
                patient["patient_id"],

            "study_id":
                patient["study_id"],

            "site_id":
                patient["site_id"],

            "drug_type":
                random.choice(DRUG_TYPES),

            "kit_id":
                f"KIT{state['counters']['dispense']:06}",

            "visit_number":
                random.randint(1, 8),

            "dispense_date":
                state["current_date"],

            "quantity_dispensed":
                qty
        }

        events.append(record)

    return events