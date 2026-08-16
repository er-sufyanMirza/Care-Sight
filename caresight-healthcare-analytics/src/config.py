from pathlib import Path
import os
from sqlalchemy.engine import URL

from dotenv import load_dotenv

load_dotenv()

# ============================================================
# FHIR
# ============================================================
FHIR_BASE_URL = os.getenv("FHIR_BASE_URL")

# ============================================================
# PROJECT PATHS
# ============================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA =      PROJECT_ROOT/"data"/"raw"
PROCESSED_DATA = PROJECT_ROOT/"data"/"processed"
REFERENCE_DATA = PROJECT_ROOT/"data"/"reference"

# ============================================================
# POSTGRESQL
# ============================================================
POSTGRES_HOST = os.getenv(
    "POSTGRES_HOST",
    "localhost"
) 

POSTGRES_PORT = os.getenv(
    "POSTGRES_PORT",
    "5432"
)

POSTGRES_DB = os.getenv(
    "POSTGRES_DB",
    "caresight"
)

POSTGRES_USER = os.getenv(
    "POSTGRES_USER",
    "postgres"
)

POSTGRES_PASSWORD = os.getenv(
    "POSTGRES_PASSWORD"
)

# ============================================================
# DATABASE URL
# ============================================================



DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=int(POSTGRES_PORT),
    database=POSTGRES_DB,
)



