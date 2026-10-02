-- 1. dim_site_scd2
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.dim_site_scd2
(
    site_sk BIGINT GENERATED ALWAYS AS IDENTITY,

    site_id STRING,
    site_name STRING,
    study_id STRING,
    country_code STRING,
    region STRING,

    site_status STRING,
    site_manager STRING,

    effective_start_date TIMESTAMP,
    effective_end_date TIMESTAMP,

    is_current BOOLEAN
)
USING DELTA;

-- 2. dim_country
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.dim_country
(
    country_sk BIGINT GENERATED ALWAYS AS IDENTITY,

    country_code STRING,
    country_name STRING,
    region STRING
)
USING DELTA;

-- 3. dim_depot
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.dim_depot
(
    depot_sk BIGINT GENERATED ALWAYS AS IDENTITY,

    depot_id STRING,
    depot_name STRING,
    country_code STRING,
    region STRING
)
USING DELTA;

-- 4. dim_drug
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.dim_drug
(
    drug_sk BIGINT GENERATED ALWAYS AS IDENTITY,

    drug_type STRING,
    drug_name STRING,
    shelf_life_days INT,
    reorder_threshold INT,
    unit_of_measure STRING
)
USING DELTA;

-- 5. dim_patient
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.dim_patient
(
    patient_sk BIGINT GENERATED ALWAYS AS IDENTITY,

    patient_id STRING,
    study_id STRING,
    site_id STRING,
    country_code STRING,

    randomization_date DATE,

    study_arm STRING,
    patient_status STRING
)
USING DELTA;

-- 6. fact_shipment_events
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.fact_shipment_events
(
    shipment_id STRING,

    shipment_event_timestamp TIMESTAMP,

    source_depot_id STRING,
    destination_site_id STRING,

    study_id STRING,
    drug_type STRING,

    qty_shipped INT,

    shipment_status STRING,

    expected_delivery_date DATE,
    actual_delivery_date DATE
)
USING DELTA;

-- 7. fact_shipment_current
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.fact_shipment_current
(
    shipment_id STRING,

    shipment_date DATE,

    source_depot_id STRING,
    destination_site_id STRING,

    study_id STRING,
    drug_type STRING,

    qty_shipped INT,

    current_status STRING,

    expected_delivery_date DATE,
    actual_delivery_date DATE,

    shipment_lead_time_days INT,
    delivery_delay_days INT
)
USING DELTA;

-- 8. fact_inventory
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.fact_inventory
(
    snapshot_date DATE,

    site_id STRING,
    study_id STRING,

    drug_type STRING,

    qty_on_hand INT,
    qty_reserved INT,
    qty_expired INT,

    available_stock INT,

    inventory_adjustment INT
)
USING DELTA;

-- 9. fact_dispensing
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.fact_dispensing
(
    dispense_id STRING,

    patient_id STRING,
    site_id STRING,
    study_id STRING,

    drug_type STRING,

    kit_id STRING,

    visit_number INT,

    dispense_date DATE,

    quantity_dispensed INT
)
USING DELTA;

-- 10. fact_daily_consumption
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.silver.fact_daily_consumption
(
    consumption_date DATE,

    site_id STRING,
    study_id STRING,

    drug_type STRING,

    total_kits_dispensed BIGINT,

    total_quantity_dispensed BIGINT
)
USING DELTA;


-- Truncate 

TRUNCATE TABLE clinical_trial_supply_chain.silver.dim_site_scd2;

TRUNCATE TABLE clinical_trial_supply_chain.silver.dim_country;

TRUNCATE TABLE clinical_trial_supply_chain.silver.dim_depot;

TRUNCATE TABLE clinical_trial_supply_chain.silver.dim_drug;

TRUNCATE TABLE clinical_trial_supply_chain.silver.dim_patient;

TRUNCATE TABLE clinical_trial_supply_chain.silver.fact_shipment_events;

TRUNCATE TABLE clinical_trial_supply_chain.silver.fact_shipment_current;

TRUNCATE TABLE clinical_trial_supply_chain.silver.fact_inventory;

TRUNCATE TABLE clinical_trial_supply_chain.silver.fact_dispensing;

TRUNCATE TABLE clinical_trial_supply_chain.silver.fact_daily_consumption;