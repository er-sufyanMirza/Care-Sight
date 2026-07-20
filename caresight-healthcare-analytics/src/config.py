from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

FILE_BASE_URL = os.getenv("FILE_BASE_URL")

project_root = Path(__file__).resolve().parent.parent
RAW_DATA = project_root/"data"/"raw"
PROCDSSED_DATA = project_root/"data"/"processed"
REFERENCE_DATA = project_root/"data"/"reference"

