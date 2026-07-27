from src.fhir.client import FHIRClient

client = FHIRClient()

print("="* 60)
print("FHIR CONNECTION TEST")
print("=" * 60)

metadata = client.get("metadata")

print("RESOURCE TYPE:", metadata["resourceType"])
print("FHIR VERSION:", metadata["fhirVersion"])
print("status           : success")