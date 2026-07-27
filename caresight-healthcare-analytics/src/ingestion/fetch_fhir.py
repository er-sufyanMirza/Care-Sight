import os
import requests
from dotenv import load_dotenv

load_dotenv()

FHIR_BASE_URL = os.getenv("FHIR_BASE_URL")

def test_fhir_connection() -> None:
    "test the fhir connection to the server"
    metadata_url = f"{FHIR_BASE_URL}/metadata"
    
    response = requests.get(
        metadata_url,
        headers = {
            "Accept" : "application/fhir+json"
        },
        timeout = 30
    )
    
    response.raise_for_status()
    
    capability_statement = response.json()
    
    print("fhir connection successful")
    
    print(
        "resourcetype:",
        capability_statement.get("resourceType")
    )
    
    print(
        "FHIR_version: ",
        capability_statement.get(
            "fhirVersion",
            "not provided"
        )
    )
    
if __name__ == '__main__':
    test_fhir_connection()