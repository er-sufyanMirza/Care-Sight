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

