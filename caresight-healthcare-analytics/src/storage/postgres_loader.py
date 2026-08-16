"""
PostgreSQL Loader

Loads transformed CareSight CSV datasets into
the PostgreSQL healthcare analytics warehouse.
"""

from __future__ import annotations
from pathlib import Path
#hi
from uuid import UUID as PythonUUID



from sqlalchemy import create_engine, text, Date
from sqlalchemy.dialects.postgresql import UUID

import pandas as pd 

from src.config import DATABASE_URL, PROCESSED_DATA

from sqlalchemy.engine import Engine, URL

class PostgreSQLLoader:
    """ Loads csv data into Postgresql"""
    TABLE_COLUMNS = {
        "dim_patient": [
            "patient_id",
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "age",
            "age_group",
            "city",
            "state",
            "postal_code",
            "phone",
            "marital_status",
            "race",
            "ethnicity",
            ],
        "fact_encounter" : [
            "encounter_id",
            "patient_id",
            "encounter_class",
            "start_datetime",
            "end_datetime",
            "length_of_stay_days",
            "organization_id"
        ],
        "fact_observation": [
            "observation_id",
            "patient_id",
            "encounter_id",
            "loinc_code",
            "observation_name",
            "value",
            "value_text",
            "unit",
            "status",
            "effective_datetime",
        ],
        "fact_condition": [
            "condition_id",
            "patient_id",
            "encounter_id",
            "code_system",
            "diagnosis_code",
            "condition_name",
            "clinical_status",
            "verification_status",
            "onset_date",
            "recorded_date",
        ],

        "fact_procedure": [
            "procedure_id",
            "patient_id",
            "encounter_id",
            "code_system",
            "procedure_code",
            "procedure_name",
            "status",
            "performed_start",
            "performed_end",
            "location",
        ],
        "fact_medication": [
            "medication_request_id",
            "patient_id",
            "encounter_id",
            "code_system",
            "medication_code",
            "medication_name",
            "status",
            "intent",
            "authored_date",
            "dosage_text",
        ],
        }
    
    LOAD_ORDER = [
        (
            'patient.csv',
            'dim_patient',
         ),
        (
            'encounter.csv',
            'fact_encounter'
        ),
        (
            'observation.csv',
            'fact_observation',
        ),
        (
            'condition.csv',
            'fact_condition',
        ),
        (
            'procedure.csv',
            'fact_procedure',
        ),
        (
            'medication.csv',
            'fact_medication',
        )
    ]
    
    def __init__(
        self,
        database_url :  str |  URL  = DATABASE_URL,
    ) -> None:
        
        if not database_url:
            raise ValueError("DATABASE_URL is not configured")
        
        self.engine : Engine = create_engine(database_url)
        
    def test_connection(self) -> bool:
        """Test PostgreSQL connectivity."""

        with self.engine.connect() as connection:
            result = connection.execute(
                text("SELECT 1")
            )

            value = result.scalar()

            print("SQL result:", value)
            print("SQL result type:", type(value))

            return value == 1
    def load_dataframe(
        self,
        dataframe : pd.DataFrame,
        table_name : str,
    ) -> None:
        """ Load a Dataframe into existing Postgresql table"""
        dataframe = dataframe.copy()
        # ========================================================
        # ENCOUNTER
        # ========================================================
        if table_name == "fact_encounter":
            dataframe = dataframe.rename(columns = 
            {"start_date" : "start_datetime", "end_date" : "end_datetime"})
        
        # ========================================================
        # OBSERVATION
        # ========================================================    
        if table_name == "fact_observation":

            numeric_values = pd.to_numeric(
                dataframe["value"],
                errors="coerce",
            )

            text_values = dataframe["value"].where(
                numeric_values.isna()
            )

            dataframe = dataframe.assign(
                value=numeric_values,
                value_text=text_values,
            )
            
        # ========================================================
        # REQUIRED COLUMNS
        # ========================================================    
        if table_name in self.TABLE_COLUMNS:
            columns = self.TABLE_COLUMNS[table_name]
            
            missing_columns = [
                column
                for column in columns
                    if column not in dataframe.columns
            ]

            if missing_columns:
                raise ValueError(
                    f"Missing columns for {table_name}: "
                    f"{missing_columns}"
                )

            dataframe = dataframe[columns]
            
    # ========================================================
    # UUID CONVERSION
    # ========================================================
        uuid_columns = [
            column
            for column in [
                "patient_id",
                "encounter_id",
                "observation_id",
                "condition_id",
                "procedure_id",
                "medication_request_id",
            ]
            if column in dataframe.columns
        ]

        for column in uuid_columns:
            uuid_values = pd.Series(
                [
                    PythonUUID(str(value))
                    if pd.notna(value)
                    else None
                    for value in dataframe[column]
                ],
                index=dataframe.index,
                dtype="object",
            )

            dataframe = dataframe.assign(
                **{
                    column: uuid_values
                }
                )
        # ========================================================
        # DATE
        # ========================================================
        if "birth_date" in dataframe.columns:
            dataframe["birth_date"] =(
                pd.to_datetime(dataframe["birth_date"], errors="coerce",).dt.date
                ) 
        # ========================================================
        # DATETIME
        # ========================================================     
        datetime_columns = [
            column
            for column in [
                "start_datetime",
                "end_datetime",
                "effective_datetime",
                "onset_date",
                "recorded_date",
                "performed_start",
                "performed_end",
                "authored_date",
            ]
            if column in dataframe.columns
        ]
        for column in datetime_columns:
            datetime_values = pd.to_datetime(
                dataframe[column],
                errors = "coerce",
            )
            dataframe = dataframe.assign(
                **{column : datetime_values}
            )
            
        
        # ========================================================
        # DATABASE LOAD
        # ========================================================    
        with self.engine.begin() as connection:
            dataframe.to_sql(
                name=table_name,
                con=self.engine,
                schema="public",
                if_exists="append",
                index=False,
                method="multi",
                dtype={
                    "patient_id": UUID(as_uuid=True),
                    "encounter_id": UUID(as_uuid=True),
                    "observation_id": UUID(as_uuid=True),
                    "condition_id": UUID(as_uuid=True),
                    "procedure_id": UUID(as_uuid=True),
                    "medication_request_id": UUID(as_uuid=True),
                    "birth_date": Date(),
                },
            )
        
    def load_csv(
        self,
        filename : str,
        table_name : str,
    ) -> int:
        
        """Load one csv into Postgresql"""
        file_path = PROCESSED_DATA / filename
        
        if not file_path.exists():
            raise FileNotFoundError(f"CSV file not found : {file_path}")
        
        dataframe = pd.read_csv(
            file_path
        )
        
        self.load_dataframe(
            dataframe,
            table_name
        )
        
        return len(dataframe)
    
    def load_all(self) -> None:
        """Load all CareSight datasets in dependency order"""
        
        for filename, table_name in self.LOAD_ORDER:
            print(f"Loading {filename} -> {table_name}")
            
            row_count = self.load_csv(
                filename,
                table_name,
            )
            
            print(f"loaded {row_count:,} rows")
            
            print()
            print("All data loaded successfully")
            
if __name__ == '__main__':
    loader  = PostgreSQLLoader()
    print("Testing PostgreSQL connection")
    
    if loader.test_connection:
        print("PostgreSQL connection successful")
        
        print()
        loader.load_all()