from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

FHIR_BASE_URL = os.getenv("FHIR_BASE_URL")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA =      PROJECT_ROOT/"data"/"raw"
PROCESSED_DATA = PROJECT_ROOT/"data"/"processed"
REFERENCE_DATA = PROJECT_ROOT/"data"/"reference"

