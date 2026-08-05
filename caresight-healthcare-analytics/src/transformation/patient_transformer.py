from __future__ import annotations
from typing import Any
from src.transformation.base_transformer import BaseTransformer
from src.utils.date_utils import DateUtils
import pandas as pd

class PatientTransformer:
    
    """ Transform FHIR resources into pandas resources"""
    
    def transform(
        self,
        resources : list[dict[str, Any]],
    ) -> pd.DataFrame:
        
        
        rows = []
        
        for patient in resources:
            
            if patient.get("resourceType") != "Patient":
                continue
            
            birth_date = patient.get("birthDate")
            age = DateUtils.calculate_age(birth_date)
            name = patient.get("name", [{}])[0]
            address = patient.get("address", [{}])[0]
            telecom = patient.get("telecom", [])
            
            rows.append(
                {
                    "patient_id" : patient.get("id"),
                    "first_name" : patient.get("name"),
                    "last_name" : patient.get("family"),
                    "gender" : patient.get("gender"),
                    "birth_date" : patient.get("birthDate"),
                    "age" : age,
                    "age_group" : DateUtils.age_group(age),
                    "city" : patient.get("city"),
                    "state" : patient.get("state"),
                    "postal_code" : patient.get("postalCode"),
                    "phone" : self._extract_phone(telecom),
                    "marital_status" : self._extract_marital_status(patient),
                    "race" : self._extract_race(patient),
                    "ethnicity" : self._extract_ethnicity(patient)
                }
            )
            
        return pd.DataFrame(rows)
    
    def _extract_phone(
        self,
        telecom : list[dict[str, Any]]
    ) -> str | None:
                    
        """ Extract Patient's phone number"""
        
        for contact in telecom:
            if contact.get("system") == "phone":
                return contact.get("value")
        
        return None
    
    def _extract_marital_status(
        self,
        patient : dict[str, Any]
    ) -> str | None:
        
        marital = patient.get("maritalStatus")
        
        if marital:
            return marital.get("text")
        
        
        return None
    
    def _extract_race(
        self,
        patient : dict[str,Any],
    ) -> str | None:
        
        for extension in patient.get("extension", []):
            if "us-core-race" in extension.get("url", ""):
                for item in extension.get("extension",[]):
                    if item.get("url") == "text":
                        return item.get("valueString")
        return None
    
    def _extract_ethnicity(
        self,
        patient : dict[str, Any]
    ) -> str | None:
        
        for extension in patient.get("extension", []):
            if "us-core-ethnicity" in extension.get("url", ""):
                for item in extension.get("extension", []):
                    if item.get("url") == "text":
                        return item.get("valueString")
                    
        return None
    
    