from src.config import (
    FHIR_BASE_URL,
    PROJECT_ROOT,
    RAW_DATA,
    PROCESSED_DATA,
    REFERENCE_DATA,
)

print("=" * 60)
print("CONFIGURATION TEST")
print("=" * 60)

print(f"FHIR Base URL : {FHIR_BASE_URL}")
print(f"Project Root  : {PROJECT_ROOT}")
print(f"Raw Data      : {RAW_DATA}")
print(f"Processed Data: {PROCESSED_DATA}")
print(f"Reference Data: {REFERENCE_DATA}")

print("\nConfiguration loaded successfully.")
