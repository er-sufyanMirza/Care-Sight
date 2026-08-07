from pathlib import Path
from pprint import pprint

from src.transformation.resource_extractor import ResourceExtractor
from src.ingestion.fhir_file_reader import FhirFileReader

reader = FhirFileReader()

resources = reader.read_folder(Path("synthea", "synthea", "output", "fhir"))

grouped = ResourceExtractor().group_by_type(resources)

encounter = grouped["Encounter"][0]

print(encounter.keys())

print()

print(encounter)