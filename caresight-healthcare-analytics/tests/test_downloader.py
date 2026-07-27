from pprint import pprint

from src.fhir.client import FHIRClient

client = FHIRClient()

bundle = client.get_bundle("Patient", count=3)

print(type(bundle))
print(bundle.keys())

pprint(bundle)