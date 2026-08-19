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