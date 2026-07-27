""" FHIR DOWNLOADER

Responsible for downloading fhir resources
"""

from __future__ import annotations
from src.fhir.client import FHIRClient

class FHIRDownloader:
    def __init__(
        self,
        client: FHIRClient
    ):
        self.client = client
        
    def download_resource(
        self,
        resource: str,
        count: int = 100
    ):
        
        bundle = self.client.get_bundle(
            resource,
            count = count
        )
        
        entries = bundle.get("entry", [])
        print(f"entries: {len(entries)}")
        
        return entries