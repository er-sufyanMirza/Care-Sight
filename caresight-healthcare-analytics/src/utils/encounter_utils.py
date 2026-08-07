from __future__ import annotations
from datetime import datetime

class EncounterUtils:
    
    @staticmethod
    def calculate_length_of_stay(
        start : str | None,
        end : str | None,
    ) -> int |None:
        
        """ Returns encounter duration in days"""
        
        if not start or not end:
            return None
        
        start_dt = datetime.fromisoformat(
            start.replace("z", "+00:00")
        )
        
        end_dt = datetime.fromisoformat(
            end.replace("z", "+00:00")
        )
        
        return(end_dt - start_dt).days
    