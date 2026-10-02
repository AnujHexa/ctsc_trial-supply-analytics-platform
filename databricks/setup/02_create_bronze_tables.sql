-- bronze_site_master

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_site_master
(
    site_id STRING,
    site_name STRING,
    study_id STRING,
    country_code STRING,
    region STRING,
    site_status STRING,
    activation_date DATE,
    site_manager STRING,
    last_updated_timestamp TIMESTAMP,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;


-- bronze_shipment_events

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_shipment_events
(
    shipment_id STRING,
    shipment_event_timestamp TIMESTAMP,
    shipment_date DATE,

    source_depot_id STRING,
    destination_site_id STRING,

    study_id STRING,
    drug_type STRING,

    qty_shipped INT,
    shipment_status STRING,

    expected_delivery_date DATE,
    actual_delivery_date DATE,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;

-- bronze_inventory_snapshot

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_inventory_snapshot
(
    inventory_snapshot_id STRING,
    snapshot_date DATE,

    site_id STRING,
    study_id STRING,

    drug_type STRING,

    qty_on_hand INT,
    qty_reserved INT,
    qty_expired INT,

    inventory_adjustment INT,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;

-- bronze_enrollment

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_enrollment
(
    patient_id STRING,
    study_id STRING,
    site_id STRING,
    country_code STRING,

    randomization_date DATE,

    study_arm STRING,
    patient_status STRING,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;

-- bronze_dispensing

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_dispensing
(
    dispense_id STRING,

    patient_id STRING,
    study_id STRING,
    site_id STRING,

    drug_type STRING,

    kit_id STRING,

    visit_number INT,

    dispense_date DATE,

    quantity_dispensed INT,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;

-- bronze_drug_master

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_drug_master
(
    drug_type STRING,
    drug_name STRING,
    shelf_life_days INT,
    reorder_threshold INT,
    unit_of_measure STRING,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;

-- bronze_country_master

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_country_master
(
    country_code STRING,
    country_name STRING,
    region STRING,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;

-- bronze_depot_master

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_depot_master
(
    depot_id STRING,
    depot_name STRING,
    country_code STRING,
    region STRING,

    source_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    load_id STRING
)
USING DELTA;

-- bronze_processed_files

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_processed_files
(
    file_name STRING,
    source_system STRING,
    file_size_bytes BIGINT,

    load_id STRING,

    processed_timestamp TIMESTAMP
)
USING DELTA;

-- bronze_load_audit

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.bronze.bronze_load_audit
(
    load_id STRING,

    table_name STRING,

    source_file_name STRING,

    records_loaded BIGINT,

    load_start_timestamp TIMESTAMP,
    load_end_timestamp TIMESTAMP,

    load_status STRING
)
USING DELTA;

-- Truncate 

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_site_master;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_shipment_events;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_inventory_snapshot;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_enrollment;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_dispensing;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_drug_master;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_country_master;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_depot_master;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_processed_files;

TRUNCATE TABLE clinical_trial_supply_chain.bronze.bronze_load_audit;
