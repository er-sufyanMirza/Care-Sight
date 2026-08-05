from __future__ import annotations
from datetime import date, datetime

class DateUtils:
    
    @staticmethod
    def calculate_age(
        birth_date : str | None,
    ) -> int | None:
        
        if not birth_date:
            return None
        
        dob = datetime.strptime(
            birth_date,
            "%Y-%m-%d",
        ).date()
        
        today = date.today()
        
        age = today.year - dob.year - ((today.month, today.day) > (dob.month, dob.day))
        
        return age
    
    @staticmethod
    def age_group(
        age : int | None,
    ) -> str | None:
        
        if age is None:
            return None
        
        if age < 13:
            return "Child"
        
        if age < 20:
            return "Teen"
        
        if age < 60:
            return "Adult"
        
        return "Senior"
    
    