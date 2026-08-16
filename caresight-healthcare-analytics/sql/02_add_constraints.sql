-- ============================================================
-- CareSight Healthcare Analytics
-- PostgreSQL Warehouse
-- 02 - Constraints and Indexes
-- ============================================================


-- ============================================================
-- FOREIGN KEYS
-- ============================================================


ALTER TABLE fact_encounter
ADD CONSTRAINT fk_encounter_patient
FOREIGN KEY (patient_id)
REFERENCES dim_patient(patient_id);

-- Observation → Patient
ALTER TABLE fact_observation
ADD CONSTRAINT fk_observation_patient
FOREIGN KEY (patient_id)
REFERENCES dim_patient(patient_id);

-- Observation → encounter
ALTER TABLE fact_observation
ADD CONSTRAINT fk_observation_encounter
FOREIGN KEY (encounter_id)
REFERENCES fact_encounter(encounter_id);

-- condition → patient
ALTER TABLE fact_condition
ADD CONSTRAINT fk_condition_patient
FOREIGN KEY (condition_id)
REFERENCES dim_patient(patient_id);

-- condition → encounter
ALTER TABLE fact_condition
ADD CONSTRAINT fk_condition_encounter
FOREIGN KEY (encounter_id)
REFERENCES fact_encounter(encounter_id);


-- Procedure → Patient
ALTER TABLE fact_procedure
ADD CONSTRAINT fk_procedure_patient
FOREIGN KEY (patient_id)
REFERENCES dim_patient(patient_id);


-- Procedure → Encounter
ALTER TABLE fact_procedure
ADD CONSTRAINT fk_procedure_encounter
FOREIGN KEY (encounter_id)
REFERENCES fact_encounter(encounter_id);


-- Medication → Patient
ALTER TABLE fact_medication
ADD CONSTRAINT fk_medication_patient
FOREIGN KEY (patient_id)
REFERENCES dim_patient(patient_id);


-- Medication → Encounter
ALTER TABLE fact_medication
ADD CONSTRAINT fk_medication_encounter
FOREIGN KEY (encounter_id)
REFERENCES fact_encounter(encounter_id);

-- ============================================================
-- INDEXES
-- ============================================================

-- Patient lookup indexes
CREATE INDEX idx_encounter_patient
ON fact_encounter(patient_id);

CREATE INDEX idx_observation_patient
ON fact_observation(patient_id);

CREATE INDEX idx_condition_patient
ON fact_condition(patient_id);

CREATE INDEX idx_medication_patient
ON fact_medication(patient_id);

-- Encounter lookup indexes
CREATE INDEX idx_observation_encounter
ON fact_observation(encounter_id);

CREATE INDEX idx_condition_encounter
ON fact_condition(encounter_id);

CREATE INDEX idx_procedure_encounter
ON fact_procedure(encounter_id);

CREATE INDEX idx_medication_encounter
ON fact_medication(encounter_id);

-- Clinical terminology indexes
CREATE INDEX idx_observation_loinc
ON fact_observation(loinc_code);

CREATE INDEX idx_condition_code
ON fact_condition(diagnosis_code);

CREATE INDEX idx_procedure_code
ON fact_procedure(procedure_code);

CREATE INDEX idx_medication_code
ON fact_medication(medication_code);

-- Time based analytical indexes

CREATE INDEX idx_encounter_start
ON fact_encounter(start_datetime);

CREATE INDEX idx_observation_effective
ON fact_observation(effective_datetime);

CREATE INDEX idx_condition_onset
ON fact_condition(onset_date);

CREATE INDEX idx_procedure_start
ON fact_procedure(performed_start);

CREATE INDEX idx_medication_authored
ON fact_medication(authored_date);