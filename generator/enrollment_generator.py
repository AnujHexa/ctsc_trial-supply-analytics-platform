from datetime import date
import random


PATIENT_STATUSES = [
    "ACTIVE",
    "COMPLETED",
    "WITHDRAWN",
    "SCREEN_FAILED"
]


STUDY_ARMS = [
    "ARM_A",
    "ARM_B",
    "ARM_C"
]


def update_existing_patients(state):

    for patient in state["patients"]:

        if patient["patient_status"] != "ACTIVE":
            continue

        if random.random() < 0.03:
            patient["patient_status"] = "COMPLETED"

        elif random.random() < 0.02:
            patient["patient_status"] = "WITHDRAWN"


def generate_enrollments(state):

    update_existing_patients(state)

    records = []

    new_patients = random.randint(2, 5)

    for _ in range(new_patients):

        state["counters"]["patient"] += 1

        site = random.choice(state["sites"])

        patient = {

            "patient_id":
                f"PAT{state['counters']['patient']:06}",

            "study_id":
                site["study_id"],

            "site_id":
                site["site_id"],

            "country_code":
                site["country_code"].strip(),

            "randomization_date":
                state["current_date"],

            "study_arm":
                random.choice(STUDY_ARMS),

            "patient_status":
                "ACTIVE"
        }

        # controlled dirty data
        if (
            state["run_number"] > 5
            and random.random() < 0.02
        ):
            patient["study_arm"] = None

        state["patients"].append(patient)

        records.append(patient)

    return records