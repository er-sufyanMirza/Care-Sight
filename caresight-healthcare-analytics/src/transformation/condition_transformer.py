""" 
Confition Transformer
converts fhir condition resources into analytics ready pandas dataframe
"""
from __future__ import annotations
from typing import Any
import pandas as pd 
from src.transformation.base_transformer import BaseTransformer

class  ConditionTransformer(BaseTransformer):
    
    """
    Transform FHIR Condition resources.
    """
    def transform(
        self,
        resources : list[dict[str, Any]],
    ) -> pd.DataFrame:
        
        rows : list[dict[str, Any]] = []
        
        for condition in resources:
            
            if condition.get("resourceType") != "Condition":
                continue
            
            rows.append(
                {
                    "condition_id" : condition.get("id"),
                    "patient_id" : self._extract_patient_id(condition),
                    "encounter_id" : self._extract_encounter_id(condition),
                    "code_system" : self._extract_code_system(condition),
                    "diagnosis_code": self._extract_diagnosis_code(condition),
                    "condition_name": self._extract_condition_name(condition),
                    "clinical_status": self._extract_clinical_status(condition),
                    "verification_status": self._extract_verification_status(condition),
                    "onset_date": self._extract_onset_date(condition),
                    "recorded_date": condition.get("recordedDate"),
                }
            )
        return pd.DataFrame(rows)
        
    def _extract_patient_id(
        self,
        condition : dict[str, Any],
    ) -> str | None:
    
        subject = condition.get("subject", {})
        reference = subject.get("reference")
        
        if not reference:
            return None
            
        if reference.startswith("urn:uuid:"):
            reference.replace("urn:uuid:", "", 1)
            
        return reference.split("/")[-1]
        
    def _extract_encounter_id(
        self,
        condition : dict[str, Any],
    ) -> str | None:
    
        encounter = condition.get("encounter", {})
        reference = encounter.get("reference")
        
        if not reference:
            return None
            
        if reference.startswith("urn:uuid:"):
            reference.replace("urn:uuid:", "", 1)
            
        return reference.split("/")[-1]
    def _extract_code_system(
        self,
        condition : dict[str, Any],
    ) -> str | None:
    
        coding = (condition.get("code", {}).get("coding", []))
        
        for item in coding:
            system = item.get("system")
            
            if system:
                return system
                
        return None
        
    def _extract_diagnosis_code(
        self,
        condition : dict[str, Any],
    ) -> str | None:
    
        coding = (condition.get("code", {}).get("coding", []))
        
        for item in coding:
            code = item.get("code")
            
            if code:
                return code
                
        return None
        
    def _extract_condition_name(
        self,
        condition : dict[str, Any]
    ) -> str | None:
    
        code = condition.get("code", {})
        text = code.get("text")
        
        if text:
            return text
            
        coding = code.get("coding", [])
        
        for item in coding:
            display = item.get("display")
            
            if display:
                return display
        return None
        
    def _extract_clinical_status(
        self,
        condition : dict[str, Any],
    ) -> str | None:
        
        status = condition.get("clinicalStatus", {})
        
        return self._extract_codeable_concept_text(status)
    
    
    def _extract_verification_status(
        self,
        condition: dict[str, Any],
    ) -> str | None:
        """
        Extract verification status.
        """

        status = condition.get(
            "verificationStatus",
            {},
        )
        return self._extract_codeable_concept_text(status)
    
        
    def _extract_codeable_concept_text(
        self,
        concept : dict[str, Any],
    ) -> str | None:

        text = concept.get("text")
        
        if text:
            return text
            
        coding = concept.get("coding", [])
        
        for item in coding:
            display = item.get("display")
            
            if display:
                return display
                
            code = item.get("code")
            
            if code:
                return code
                
        return None
        
    def _extract_onset_date(
        self,
        condition : dict[str, Any],
    ) -> str | None:
    
        onset_date = condition.get("onsetDateTime")
        
        if onset_date:
            return onset_date
            
        onset_period = condition.get("onsetPeriod", {})
        
        if onset_period:
            return onset_period.get("start")
            
        return None