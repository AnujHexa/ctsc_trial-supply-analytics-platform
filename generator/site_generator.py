from datetime import datetime
import random


SITE_MANAGERS = [
    "Rahul Sharma",
    "Priya Mehta",
    "Vikas Gupta",
    "Anita Rao",
    "Neha Singh",
    "John Miller",
    "Thomas Weber"
]


SITE_STATUS = [
    "ACTIVE",
    "SUSPENDED",
    "CLOSED"
]


INITIAL_SITES = [
    ("Mumbai Oncology Site", "IN", "APAC"),
    ("Delhi Clinical Center", "IN", "APAC"),
    ("Singapore Research Hub", "SG", "APAC"),
    ("Frankfurt Trial Center", "DE", "EMEA"),
    ("Boston Medical Site", "US", "NA")
]

STUDY_MAPPING = {
    "SITE001": "STUDY001",
    "SITE002": "STUDY001",
    "SITE003": "STUDY002",
    "SITE004": "STUDY003",
    "SITE005": "STUDY003"
}


def create_initial_sites(state):

    records = []

    for idx, site_info in enumerate(INITIAL_SITES, start=1):

        site_id = f"SITE{idx:03}"

        site = {
            "site_id": site_id,
            "site_name": site_info[0],
            "study_id": STUDY_MAPPING[site_id],
            "country_code": site_info[1],
            "region": site_info[2],
            "site_status": "ACTIVE",
            "activation_date": "2025-01-01",
            "site_manager": random.choice(SITE_MANAGERS),
            "last_updated_timestamp":
                f"{state['current_date']}T09:00:00"
        }

        state["sites"].append(site)
        records.append(site)

    state["counters"]["site"] = len(records)

    return records


def apply_site_changes(state):

    for site in state["sites"]:

        if random.random() < 0.05:

            site["site_manager"] = random.choice(SITE_MANAGERS)
            site["last_updated_timestamp"] = (
                f"{state['current_date']}T09:00:00"
            )

        if random.random() < 0.02:

            site["site_status"] = random.choice(SITE_STATUS)
            site["last_updated_timestamp"] = (
                f"{state['current_date']}T09:00:00"
            )
        # Controlled dirty data
        if random.random() < 0.02:
            site["country_code"] = site["country_code"] + " "

    return state["sites"]


def generate_sites(state):

    if not state["sites"]:
        return create_initial_sites(state)

    return apply_site_changes(state)