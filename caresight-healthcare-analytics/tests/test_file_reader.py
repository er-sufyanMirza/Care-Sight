from collections import Counter
from pathlib import Path

from src.ingestion.fhir_file_reader import FhirFileReader

reader = FhirFileReader()

folder = Path(
    "synthea",
    "synthea",
    "output",
    "fhir",
)

resources = reader.read_folder(folder)

print(f"Total resources: {len(resources)}")

counter = Counter(
    resource["resourceType"]
    for resource in resources
)

print("\nResource Counts")
print("=" * 40)

for resource_type, count in sorted(counter.items()):
    print(f"{resource_type:<25} {count}")