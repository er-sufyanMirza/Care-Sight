""" FHIR DOWNLOADER

Responsible for downloading fhir resources
"""

from __future__ import annotations
from src.fhir.client import FHIRClient
from utils.file_manager import FileManager

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
        
        timestamp = FileManager.create_timestamp()
        filename = f"{resource}_{timestamp}.json"
        
        path = FileManager.save_json(
            data =  bundle,
            folder =  resource,
            filename= filename,
        )
        print(f"saved raw bundle ->{path}")
        
        entries = bundle.get("entry", [])
        
        resources = [
            entry[resource]
            for entry in entries
        ]
        
        
        
        
        
        return resource