""" 
Encounter transformer
Transforms fhir resources into analytics ready dataframe
"""

from __future__ import annotations

from typing import Any
import pandas as pd
from src.transformation.base_transformer import BaseTransformer
from src.utils.encounter_utils import EncounterUtils

class EncounterTransformer(BaseTransformer):
    def transform(
        self,
        resources : list[dict[str, Any]],
    ) -> pd.DataFrame:
        
        rows = []
        
        for encounter in resources:
            
            if encounter.get("resourceType") != "Encounter":
                continue
            
            period = encounter.get("period", {})
            start = period.get("start")
            end = period.get("end")
            
            rows.append(
                {
                    "encounter_id" : encounter.get("id"),
                    "patient_id" : self._extract_patient_id(encounter),
                    "encounter_class" : self._extract_class(encounter),
                    "start_date" : start,
                    "end_date" : end,
                    "length_of_stay_days" : EncounterUtils.calculate_length_of_stay(
                        start,
                        end
                    ),
                    "organization_id": self._extract_organization(encounter),
                }
            )
            
        return pd.DataFrame(rows)
    
    def _extract_patient_id(
        self,
        encounter : dict[str, Any],
    ) -> str | None:
        
        subject = encounter.get("subject", {})
        reference = subject.get("reference")
        
        if reference.startswith("urn:uuid:"):
            return reference.replace("urn:uuid:", "")
        
        return reference.split("/")[-1]
    
    def _extract_class(
        self,
        encounter : dict[str, Any],
    ) -> str | None:
        
        encounter_class = encounter.get("class", {})
        
        return(
            encounter_class.get("display")
            or encounter_class.get("code")
        )        
        
    def _extract_organization(
        self,
        encounter : dict[str, Any],
    ) -> str | None:
        
        provider = encounter.get("service_provider", {})
        reference = provider.get("reference")
        
        if reference:
            return reference.split("/")[-1]
        return None
    
            