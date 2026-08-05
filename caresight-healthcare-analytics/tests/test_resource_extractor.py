from pathlib import Path

from src.ingestion.fhir_file_reader import FhirFileReader
from src.transformation.resource_extractor import ResourceExtractor

reader = FhirFileReader()

folder = Path(
    "synthea",
    "synthea",
    "output",
    "fhir",
)

resources = reader.read_folder(folder)

exractor = ResourceExtractor()

grouped = exractor.group_by_type(resources)

print(grouped.keys())

print("Patients", len(grouped["Patient"]))

print("Encounters", len(grouped["Encounter"]))

print("Observations", len(grouped["Observation"]))