 # CareSight Healthcare Analytics

*FHIR → Python ETL → PostgreSQL Data Warehouse → SQL Analytics → Power BI*

An end-to-end healthcare data analytics platform that transforms FHIR healthcare resources into a structured PostgreSQL data warehouse and delivers interactive analytics through Power BI.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-4169E1?logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![FHIR](https://img.shields.io/badge/Standard-FHIR-00758F)

---
  
## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Dataset Snapshot](#dataset-snapshot)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [SQL Analytics Layer](#sql-analytics-layer)
- [Power BI Dashboard](#power-bi-dashboard)
- [Data Quality & Validation](#data-quality--validation)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

## Overview

CareSight Healthcare Analytics is a data engineering and analytics project built around healthcare data represented in the FHIR (Fast Healthcare Interoperability Resources) standard.

The project implements a complete pipeline: it extracts healthcare resources, transforms them into analytics-ready datasets, loads them into a PostgreSQL data warehouse, builds SQL-based analytical views on top of the warehouse, and visualizes the resulting metrics through an interactive Power BI dashboard.

## Key Features

- Transforms raw FHIR healthcare resources into structured, analytics-ready datasets
- Implements a relational healthcare data warehouse in PostgreSQL with dimension and fact tables
- Ships reusable Python ETL components for each FHIR resource type
- Maintains referential integrity across patients, encounters, and clinical events
- Provides SQL analytical views purpose-built for reporting and BI consumption
- Delivers a three-page interactive Power BI dashboard covering executive, demographic, and clinical views
- Surfaces patient, demographic, encounter, and clinical activity insights across the platform
- Includes multi-stage data validation across CSV, database, and referential-integrity checks

## Dataset Snapshot

| Resource | Records |
|---|---:|
| Patients | 10 |
| Encounters | 382 |
| Conditions | 269 |
| Observations | 1,751 |
| Procedures | 1,086 |
| Medication Requests | 119 |

## System Architecture

```
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
```

## Tech Stack

| Category | Tools |
|---|---|
| Data Engineering | Python, Pandas, SQLAlchemy, FHIR |
| Database | PostgreSQL, SQL |
| Business Intelligence | Microsoft Power BI |
| Development | VS Code, PowerShell, Git, GitHub |

## SQL Analytics Layer

After the warehouse tables are loaded, a set of SQL views turns raw fact and dimension data into clean, reporting-ready datasets.

**Patient Analytics** — `vw_patient_360`
A patient-level summary combining demographic information with aggregated healthcare activity: encounter count, condition count, observation count, procedure count, and medication count.

**Encounter Analytics** — `vw_encounter_analytics`
Combines encounter information with patient demographic attributes for utilization analysis.

**Condition Analytics** — `vw_condition_analytics`
Condition-level detail including diagnosis code, condition name, clinical status, verification status, patient demographics, and onset date.

**Observation Analytics** — `vw_observation_analytics`
Clinical observation data including numeric and text-based results, units, status, and effective timestamps.

**Procedure Analytics** — `vw_procedure_analytics`
Procedure-level detail with patient demographics and procedure timing.

**Medication Analytics** — `vw_medication_analytics`
Medication-level detail including medication name, status, intent, dosage information, and patient demographics.

**Dashboard Views**

Additional views were built specifically to power the Power BI dashboard:

- `vw_dashboard_kpis`
- `vw_patient_demographics`
- `vw_encounter_trends`
- `vw_top_conditions`
- `vw_top_procedures`
- `vw_top_medications`

## Power BI Dashboard

The `.pbix` report is organized into three pages.

**1. Executive Overview**
KPI cards including average length of stay, an encounters-over-time trend line, and top-5 breakdowns for conditions and procedures.

**2. Patients & Demographics**
KPI cards for total patients, patients with visits, average age, and encounters per patient; a patients-by-age-group column chart; a patients-by-gender donut chart; a patients-by-race bar chart; and a patient utilization table.

**3. Clinical Analysis**
KPI cards for conditions, observations, medications, and procedures; top-10 breakdowns for conditions, procedures, and medications; and a condition status donut chart.

### Dashboard Preview

![Executive Overview](docs/images/executive-overview.png)
![Patients & Demographics](docs/images/patients-demographics.png)
![Clinical Analysis](docs/images/clinical-analysis.png)

> Export each page from Power BI Desktop (**File → Export → Export to PDF**, then convert pages to PNG, or a straight screenshot works too) and save them into a `docs/images/` folder in the repo using the filenames above.

## Data Quality & Validation

Validation was performed at multiple stages of the pipeline.

- **CSV Validation** — each transformed dataset was checked for expected row counts, column names, missing values, data types, and resource-specific fields.
- **PostgreSQL Validation** — database tables were validated using primary key constraints, foreign key constraints, indexes, data type checks, and row-count checks.
- **Referential Integrity** — relationships between fact and dimension tables were tested for orphan records. Final validation confirmed zero orphan records across conditions, observations, procedures, and medications for both patient and encounter relationships.

**Final Warehouse Counts**

| Table | Records |
|---|---:|
| `dim_patient` | 10 |
| `fact_encounter` | 382 |
| `fact_condition` | 269 |
| `fact_observation` | 1,751 |
| `fact_procedure` | 1,086 |
| `fact_medication` | 119 |

## Project Structure

```
caresight-healthcare-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── ingestion/
│   ├── transformation/
│   ├── storage/
│   └── analytics/
├── tests/
├── sql/
├── dashboard/
├── README.md
├── requirements.txt
└── .gitignore
```

## Getting Started

**Prerequisites**

- Python 3.x
- PostgreSQL
- Power BI Desktop (to open and explore the dashboard)

**Setup**

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/caresight-healthcare-analytics.git
   cd caresight-healthcare-analytics
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your PostgreSQL connection details.
4. Run the ETL pipeline to transform and load the FHIR data into the warehouse.
5. Execute the scripts in `sql/` to create the analytical views.
6. Open the Power BI file in `dashboard/` and connect it to your warehouse.

## Future Improvements

- Increase dataset size for more robust analytics
- Add automated ETL scheduling
- Support incremental data loading
- Implement automated data-quality monitoring
- Add advanced patient-risk analytics
- Develop predictive models for healthcare utilization
- Add role-based dashboard views
- Deploy the analytics platform to a cloud environment

## Author

**Sufyan Mirza**
B.Tech, Computer Science & Engineering (AI/ML)

## License

This project is shared for portfolio and educational purposes.
