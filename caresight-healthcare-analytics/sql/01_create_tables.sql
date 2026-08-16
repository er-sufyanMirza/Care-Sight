-- ============================================================
-- CareSight Healthcare Analytics
-- PostgreSQL Warehouse
-- 01 - Create Tables
-- ============================================================

-- ============================================================
-- DIMENSION: PATIENT
-- ============================================================

CREATE TABLE IF NOT EXISTS dim_patient(
    patient_id uuid PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),

    gender VARCHAR(50),

    birth_date DATE,

    age INTEGER,
    age_group VARCHAR,

    city VARCHAR(255), 
    state VARCHAR(100),
    postal_code VARCHAR(20),
    phone VARCHAR(50),
    marital_status VARCHAR(100),
    race VARCHAR(255)
    ethnicity VARCHAR(255)

);


-- ============================================================
-- FACT: ENCOUNTER
-- ============================================================

CREATE TABLE IF NOT EXISTS fact_encounter (
    encounter_id UUID PRIMARY KEY,

    patient_id UUID,

    encounter_class VARCHAR(50),

    start_datetime TIMESTAMPTZ,
    end_datetime TIMESTAMPTZ,

    length_of_stay_days NUMERIC(10, 2),

    organization_id VARCHAR(255)
);


-- ============================================================
-- FACT: OBSERVATION
-- ============================================================

CREATE TABLE IF NOT EXISTS fact_observation (
    observation_id UUID PRIMARY KEY,

    patient_id UUID,
    encounter_id UUID,

    loinc_code VARCHAR(100),

    observation_name VARCHAR(500),

    value NUMERIC,

    unit VARCHAR(100),

    status VARCHAR(50),

    effective_datetime TIMESTAMPTZ
);


-- ============================================================
-- FACT: CONDITION
-- ============================================================

CREATE TABLE IF NOT EXISTS fact_condition (
    condition_id UUID PRIMARY KEY,

    patient_id UUID,
    encounter_id UUID,

    code_system VARCHAR(500),

    diagnosis_code VARCHAR(100),

    condition_name VARCHAR(500),

    clinical_status VARCHAR(100),

    verification_status VARCHAR(100),

    onset_date TIMESTAMPTZ,

    recorded_date TIMESTAMPTZ
);


-- ============================================================
-- FACT: PROCEDURE
-- ============================================================

CREATE TABLE IF NOT EXISTS fact_procedure (
    procedure_id UUID PRIMARY KEY,

    patient_id UUID,
    encounter_id UUID,

    code_system VARCHAR(500),

    procedure_code VARCHAR(100),

    procedure_name VARCHAR(500),

    status VARCHAR(50),

    performed_start TIMESTAMPTZ,
    performed_end TIMESTAMPTZ,

    location VARCHAR(500)
);


-- ============================================================
-- FACT: MEDICATION
-- ============================================================

CREATE TABLE IF NOT EXISTS fact_medication (
    medication_request_id UUID PRIMARY KEY,

    patient_id UUID,
    encounter_id UUID,

    code_system VARCHAR(500),

    medication_code VARCHAR(100),

    medication_name VARCHAR(500),

    status VARCHAR(50),

    intent VARCHAR(50),

    authored_date TIMESTAMPTZ,

    dosage_text TEXT
);