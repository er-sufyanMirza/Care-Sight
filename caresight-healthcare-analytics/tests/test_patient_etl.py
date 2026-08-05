from pathlib import Path 
from src.ingestion.fhir_file_reader import FhirFileReader
from src.storage.csv_writer import CSVWriter
from src.transformation.patient_transformer import PatientTransformer
from src.transformation.resource_extractor import ResourceExtractor

reader = FhirFileReader()

resources = reader.read_folder(Path("synthea", "synthea", "output", "fhir"))

grouped = ResourceExtractor().group_by_type(resources)

patients = grouped["Patient"]

df = PatientTransformer().transform(patients)

CSVWriter.write(
    df,
    "patient.csv"
)

print(df.head())
