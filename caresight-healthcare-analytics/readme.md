# CareSight Healthcare Analytics

An end-to-end healthcare data analytics platform that transforms FHIR healthcare resources into a structured PostgreSQL data warehouse and delivers interactive healthcare analytics dashboards using Power BI.

## 📌 Project Overview

CareSight Healthcare Analytics is a data engineering and analytics project built around healthcare data represented using the FHIR (Fast Healthcare Interoperability Resources) standard.

The project implements an end-to-end pipeline that extracts healthcare resources, transforms them into analytics-ready datasets, loads them into a PostgreSQL data warehouse, creates SQL-based analytical views, and visualizes healthcare metrics through an interactive Power BI dashboard.

The platform currently processes:

- 10 patients
- 382 encounters
- 269 conditions
- 1,751 observations
- 1,086 procedures
- 119 medication requests

## 🎯 Objectives

The main objectives of the project are to:

- Transform FHIR healthcare resources into structured analytical datasets.
- Build a relational healthcare data warehouse using PostgreSQL.
- Implement reusable Python ETL components.
- Maintain referential integrity between healthcare entities.
- Create SQL analytical views for reporting and BI consumption.
- Develop an interactive Power BI healthcare analytics dashboard.
- Provide patient, demographic, encounter, and clinical activity insights.

## 🏗️ System Architecture

```text
FHIR Healthcare Data
        │
        ▼
Python ETL Pipeline
        │
        ├── Patient Transformer
        ├── Encounter Transformer
        ├── Observation Transformer
        ├── Condition Transformer
        ├── Procedure Transformer
        └── Medication Transformer
        │
        ▼
Processed CSV Files
        │
        ▼
PostgreSQL Data Warehouse
        │
        ├── dim_patient
        ├── fact_encounter
        ├── fact_observation
        ├── fact_condition
        ├── fact_procedure
        └── fact_medication
        │
        ▼
SQL Analytics Views
        │
        ├── Patient 360
        ├── Encounter Analytics
        ├── Condition Analytics
        ├── Observation Analytics
        ├── Procedure Analytics
        └── Medication Analytics
        │
        ▼
Power BI
        │
        ├── Executive Overview
        ├── Patient & Demographics
        └── Clinical Analytics



---

## Next section: SQL Analytics

Add this immediately after the above:

```markdown
## 📈 SQL Analytics Layer

After loading the warehouse tables, analytical SQL views were created to provide clean datasets for reporting and business intelligence.

### Patient Analytics

`vw_patient_360`

Provides a patient-level summary combining demographic information with aggregated healthcare activity.

Metrics include:

- Encounter count
- Condition count
- Observation count
- Procedure count
- Medication count

### Encounter Analytics

`vw_encounter_analytics`

Combines encounter information with patient demographic attributes for utilization analysis.

### Condition Analytics

`vw_condition_analytics`

Provides condition-level analysis including:

- Diagnosis code
- Condition name
- Clinical status
- Verification status
- Patient demographics
- Onset date

### Observation Analytics

`vw_observation_analytics`

Provides clinical observation data including numeric and text-based observations, units, status, and effective timestamps.

### Procedure Analytics

`vw_procedure_analytics`

Provides procedure-level information along with patient demographics and procedure timing.

### Medication Analytics

`vw_medication_analytics`

Provides medication-level information including medication name, status, intent, dosage information, and patient demographics.

## 📊 Dashboard Analytics Views

Additional dashboard-specific views were created for Power BI:

- `vw_dashboard_kpis`
- `vw_patient_demographics`
- `vw_encounter_trends`
- `vw_top_conditions`
- `vw_top_procedures`
- `vw_top_medications`


## 📊 Power BI Dashboard

The Power BI dashboard provides three analytical pages.

### 1. Executive Overview

Provides a high-level view of healthcare activity through:

- Total patients
- Total encounters
- Total conditions
- Total procedures
- Total medications
- Average length of stay
- Encounter trends
- Top conditions
- Top procedures

### 2. Patient & Demographics

Provides patient-level and demographic analysis including:

- Patient population
- Patients with encounters
- Average age
- Encounters per patient
- Age-group distribution
- Gender distribution
- Race distribution
- Patient healthcare utilization

### 3. Clinical Analytics

Provides clinical activity analysis including:

- Total conditions
- Total observations
- Total procedures
- Total medications
- Top conditions
- Top procedures
- Top medications
- Condition status distribution



## ✅ Data Quality & Validation

The pipeline includes validation at multiple stages.

### CSV Validation

Each transformed dataset was inspected for:

- Expected row counts
- Column names
- Missing values
- Data types
- Resource-specific fields

### PostgreSQL Validation

Database tables were validated using:

- Primary key constraints
- Foreign key constraints
- Indexes
- Data type validation
- Row-count checks

### Referential Integrity

Relationships between fact and dimension tables were tested for orphan records.

The final validation confirmed zero orphan records for the patient and encounter relationships across:

- Conditions
- Observations
- Procedures
- Medications

### Final Warehouse Counts

| Table | Records |
|---|---:|
| `dim_patient` | 10 |
| `fact_encounter` | 382 |
| `fact_condition` | 269 |
| `fact_observation` | 1,751 |
| `fact_procedure` | 1,086 |
| `fact_medication` | 119 |


## 🛠️ Technology Stack

### Data Engineering
- Python
- Pandas
- SQLAlchemy
- FHIR data

### Database
- PostgreSQL
- SQL

### Business Intelligence
- Microsoft Power BI

### Development
- VS Code
- PowerShell
- Git
- GitHub

## 📁 Project Structure

```text
caresight-healthcare-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── transformation/
│   ├── storage/
│   └── analytics/
│
├── tests/
│
├── sql/
│
├── dashboard/
│
├── README.md
├── requirements.txt
└── .gitignore






```markdown
## 🚀 Future Improvements

Potential future improvements include:

- Increasing the dataset size for more robust analytics.
- Adding automated ETL scheduling.
- Adding incremental data loading.
- Implementing automated data-quality monitoring.
- Adding more advanced patient-risk analytics.
- Developing predictive models for healthcare utilization.
- Adding role-based dashboard views.
- Deploying the analytics platform to a cloud environment.

## 👨‍💻 Author

**Sufyan Mirza**

B.Tech — Computer Science & Engineering (AI/ML)

---

## ⭐ Project Highlights

This project demonstrates an end-to-end workflow covering:

**FHIR → Python ETL → PostgreSQL Data Warehouse → SQL Analytics → Power BI**

It combines data engineering, database design, SQL analytics, and business intelligence into a single healthcare analytics platform.