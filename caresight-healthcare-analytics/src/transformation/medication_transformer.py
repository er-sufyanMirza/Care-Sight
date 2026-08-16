""" 
Medication Transformer
converts raw medication fhir data into analytics ready pandas dataframe
"""
from __future__ import annotations
from src.transformation.base_transformer import BaseTransformer
from typing import Any
import pandas as pd 

class MedicationTransformer(BaseTransformer):
    
    def transform(
        self,
        resources : list[dict[str, Any]],
    ) -> pd.DataFrame:
        
        rows : list[dict[str,Any]] = []
        
        for medication in resources:
            if medication.get("resourceType") != "MedicationRequest":
                continue
            
            rows.append(
                {
                    "medication_request_id" : medication.get("id"),
                    "patient_id" : self._extract_patient_id(medication),
                    "encounter_id" : self._extract_encounter_id(medication),
                    "code_system" : self._extract_code_system(medication),
                    "medication_code" : self._extract_medication_code(medication),
                    "medication_name" : self._extract_medication_name(medication),
                    "status" : medication.get("status"),
                    "intent" : medication.get("intent"),
                    "authored_date" : medication.get("authoredon"),
                    "dosage_text" : self._extract_dosage_text(medication),
                }
            )
        return pd.DataFrame(rows)
    
        
    def _extract_patient_id(
        self,
        medication: dict[str,Any],
    ) -> str | None:
        
        subject = medication.get("subject", {})
        reference = subject.get("reference")
        
        return self._clean_reference(reference)
    
    def _extract_encounter_id(
        self,
        medication: dict[str, Any],
    ) -> str | None:
        
        encounter = medication.get("encounter", {})
        reference = encounter.get("reference")
        
        return self._clean_reference(reference)
        
        
    def _clean_reference(
        self,
        reference :str | None,
    ) -> str | None:
        
        if not reference:
            return None
        
        if reference.startswith("urn:uuid:"):
            return reference.replace("urn:uuid:", "", 1)
        
        return reference.split("/")[-1]
    
    def _extract_code_system(
        self,
        medication : dict[str, Any],
    ) -> str | None:
        
        concept = medication.get("medicationCodableConcept", {})
    
        coding = concept.get("coding", [])
        
        for item in coding:
            system = item.get("system")
            
            if system:
                return system
            
        return None
    
    def _extract_medication_code(
        self,
        medication: dict[str, Any],
    ) -> str | None:
        
        concept = medication.get("medicationCodableConcept", {})
        
        coding = concept.get("coding", [])
        
        for item in coding:
            code = item.get("code")
            
            if code:
                return code
            
        return None
    
    def _extract_medication_name(
        self,
        medication: dict[str, Any],
    ) -> str | None:
        
        concept = medication.get("medicationCodableConcept", {})
        
        text = concept.get("text")
        if text:
            return text
        coding = concept.get("coding", [])
        
        for item in coding:
            display = item.get("display")
            
            if display:
                return display
        return None
    
    def _extract_dosage_text(
        self,
        medication : dict[str, Any],
    ) -> str | None:
        
        """ Extract Human readable dosage instructions """
        
        dosage = medication.get("dosageInstructions", [])
        
        if not dosage:
            return None
        return dosage[0].get("text")