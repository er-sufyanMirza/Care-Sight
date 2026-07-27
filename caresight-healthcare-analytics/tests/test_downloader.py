from pprint import pprint

from src.fhir.client import FHIRClient
from src.fhir.downloader import FHIRDownloader

client = FHIRClient()
downloader = FHIRDownloader(client)

patients = downloader.download_resource(
    resource="Patient",
    count=5,
)

print(f"Type of patients: {type(patients)}")
print(f"Number of patients: {len(patients)}")

if len(patients) > 0:
    print("\nFirst resource:")
    pprint(patients[0])
else:
    print("No patients returned.")