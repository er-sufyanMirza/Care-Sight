from src.fhir.client import FHIRClient

print("=" * 60)
print("fhir client test")
print("=" * 60)

client = FHIRClient()

print(f"Base url: {client.base_url}")
print(f"Timeout: { client.timeout}")

print("\nHeader:")
for key, value in client.session.headers.items():
    print(f"{key} : {value}")