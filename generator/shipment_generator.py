from datetime import datetime, timedelta
import random


STATUS_FLOW = {
    "CREATED": "DISPATCHED",
    "DISPATCHED": "IN_TRANSIT",
    "IN_TRANSIT": "DELIVERED"
}


DRUG_TYPES = [
    "DRUG_A",
    "DRUG_B",
    "DRUG_C"
]


def create_new_shipments(state):

    events = []

    current_date = datetime.strptime(
        state["current_date"],
        "%Y-%m-%d"
    )

    new_shipments = random.randint(1, 3)

    for _ in range(new_shipments):

        state["counters"]["shipment"] += 1

        shipment_id = (
            f"SHIP{state['counters']['shipment']:05}"
        )

        site = random.choice(state["sites"])
        depot = random.choice(state["depots"])

        shipment = {

            "shipment_id":
                shipment_id,

            "shipment_event_timestamp":
                f"{state['current_date']}T10:00:00",

            "shipment_date":
                state["current_date"],

            "source_depot_id":
                depot["depot_id"],

            "destination_site_id":
                site["site_id"],

            "study_id":
                site["study_id"],

            "drug_type":
                random.choice(DRUG_TYPES),

            "qty_shipped":
                random.randint(50, 200),

            "shipment_status":
                "CREATED",

            "expected_delivery_date":
                (
                    current_date
                    + timedelta(
                        days=random.randint(2, 7)
                    )
                ).strftime("%Y-%m-%d"),

            "actual_delivery_date":
                None
        }

        state["shipments"].append(
            shipment
        )

        events.append(
            shipment.copy()
        )

    return events


def progress_existing_shipments(state):

    events = []

    open_shipments = [

        shipment

        for shipment in state["shipments"]

        if shipment["shipment_status"] != "DELIVERED"
    ]

    for shipment in open_shipments:

        if random.random() < 0.60:

            current_status = (
                shipment["shipment_status"]
            )

            next_status = (
                STATUS_FLOW.get(current_status)
            )

            if not next_status:
                continue

            shipment["shipment_status"] = (
                next_status
            )

            shipment[
                "shipment_event_timestamp"
            ] = (
                f"{state['current_date']}T10:00:00"
            )

            if next_status == "DELIVERED":

                shipment[
                    "actual_delivery_date"
                ] = (
                    state["current_date"]
                )

            event = shipment.copy()

            # controlled dirty data
            if random.random() < 0.02:

                event["shipment_status"] = (
                    event["shipment_status"].lower()
                )

            events.append(event)

    return events


def generate_shipments(state):

    events = []

    events.extend(
        progress_existing_shipments(state)
    )

    events.extend(
        create_new_shipments(state)
    )

    # occasional duplicate CDC event
    if events and random.random() < 0.02:

        events.append(
            random.choice(events).copy()
        )

    return events