""" 
FHIR client

can connect to all the client FHIR R4
"""

from __future__ import annotations
import requests
from typing import Any
from src.config import FHIR_BASE_URL

class FHIRClient:
    
    """ simple reusable FHIR base client"""
    def __init__(
        self,
        base_url : str | None = None,
        timeout : int = 30
    ):
        
        base_url_value = base_url if base_url is not None else FHIR_BASE_URL
        if base_url_value is None:
            raise ValueError("FHIR base URL must be provided")

        self.base_url = base_url_value.rstrip("/")
        self.timeout = timeout
        self.session = requests.session()
        self.session.headers.update(
            {
                "Accept": "application/fhir+json",
                "Content-Type": "application/fhir+json",
            }
        )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict:
        url = f"{self.base_url}/{endpoint}"

        response = self.session.get(
            url,
            params=params,
            timeout=self.timeout,
        )

        response.raise_for_status()
        return response.json()
    
    def get_bundle(
        self,
        resource: str,
        count: int = 100,
    ) -> dict:
        """ fetch one bundle page of the fhir resource"""
        
        return self.get(
            endpoint = resource,
            params = {
                "_count": count
            },
        )