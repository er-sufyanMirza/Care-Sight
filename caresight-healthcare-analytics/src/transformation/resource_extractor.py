""" Resource Extraction utilities
Seperates FHIR resources by resource type
"""

from __future__ import annotations
from typing import Any
from collections import defaultdict

class ResourceExtractor:
    """ 
    Group FHIR resources by resource type
    """
    
    def group_by_type(
        self,
        resources: list[dict[str, Any]]
    ) ->dict[str, list[dict[str, Any]]]:
        
        grouped = defaultdict(list)
        
        for resource in resources:
            resource_type = resource["resourceType"]
            grouped[resource_type].append(resource)
            
        return dict(grouped)
    
