-- 1.gold_stockout_risk

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.gold.gold_stockout_risk
(
    site_id STRING,
    site_name STRING,

    drug_type STRING,

    available_stock INT,

    avg_daily_consumption DOUBLE,

    days_of_supply_remaining DOUBLE,

    reorder_threshold INT,

    stockout_risk_flag STRING
)
USING DELTA;

--2. gold_replenishment_recommendation

CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.gold.gold_replenishment_recommendation
(
    site_id STRING,

    drug_type STRING,

    available_stock INT,

    reorder_threshold INT,

    recommended_replenishment_qty INT,

    recommendation_status STRING
)
USING DELTA;

-- 3. gold_country_inventory
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.gold.gold_country_inventory
(
    country_code STRING,
    country_name STRING,
    region STRING,

    drug_type STRING,

    total_on_hand BIGINT,

    total_available_stock BIGINT,

    total_reserved_stock BIGINT,

    total_expired_stock BIGINT
)
USING DELTA;

-- 4. gold_shipment_delay_monitoring
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.gold.gold_shipment_delay_monitoring
(
    shipment_id STRING,

    source_depot_id STRING,

    destination_site_id STRING,

    drug_type STRING,

    current_status STRING,

    expected_delivery_date DATE,

    actual_delivery_date DATE,

    delivery_delay_days INT,

    delay_flag STRING
)
USING DELTA;

-- 5. gold_depot_performance
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.gold.gold_depot_performance
(
    depot_id STRING,
    depot_name STRING,

    total_shipments BIGINT,

    delivered_shipments BIGINT,

    delayed_shipments BIGINT,

    avg_lead_time_days DOUBLE,

    on_time_delivery_pct DOUBLE
)
USING DELTA;

-- 6. gold_supply_chain_kpi
CREATE TABLE IF NOT EXISTS clinical_trial_supply_chain.gold.gold_supply_chain_kpi
(
    reporting_date DATE,

    active_sites BIGINT,

    active_patients BIGINT,

    total_inventory BIGINT,

    total_dispensed_quantity BIGINT,

    total_shipments BIGINT,

    delayed_shipments BIGINT,

    stockout_risk_sites BIGINT
)
USING DELTA;