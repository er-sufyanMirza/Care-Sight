""" FHIR DOWNLOADER

Responsible for downloading fhir resources
"""

from __future__ import annotations
from src.fhir.client import FHIRClient
from src.utils.file_manager import FileManager

class FHIRDownloader:
    def __init__(
        self,
        client: FHIRClient
    ):
        self.client = client
        
    def download_resource(
        self,
        resource: str,
        count: int = 100,
    ) -> list[dict]:

        bundle = self.client.get_bundle(
            resource,
            count=count,
        )

        timestamp = FileManager.create_timestamp()

        filename = f"{resource}_{timestamp}.json"

        path = FileManager.save_json(
            data=bundle,
            folder=resource,
            filename=filename,
        )

        print(f"Saved raw Bundle -> {path}")

        entries = bundle.get("entry")

        if entries is None:
            raise ValueError(
                "FHIR Bundle does not contain an 'entry' field. "
                "Check the API response or the data source."
            )

        resources = [
            entry["resource"]
            for entry in entries
        ]

        return resources