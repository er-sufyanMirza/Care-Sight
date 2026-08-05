from pathlib import Path
from src.ingestion.fhir_file_reader import FhirFileReader
from src.transformation.resource_extractor import ResourceExtractor
from src.transformation.patient_transformer import PatientTransformer

reader = FhirFileReader()

resources = reader.read_folder(Path("synthea", "synthea", "output", "fhir"))

extractor = ResourceExtractor()

grouped = extractor.group_by_type(resources)

patients = grouped["Patient"]

print(f"patients found: {len(patients)}")

transformer = PatientTransformer()

df = transformer.transform(patients)

print()
print(df.head())

print()
print(df.columns.to_list())

print()
print(df.shape)