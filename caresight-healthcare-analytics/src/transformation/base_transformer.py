""" Base transformer for all FHIR resources"""

from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

class BaseTransformer(ABC):
    """ Base class for all the FHIR transformers"""
    
    @abstractmethod
    def transform(
        self,
        resources :list[dict],
    ) ->pd.DataFrame:
        
        """Transform FHIR resources into a DataFrame"""
        pass