""" 
CSV writer
writes transformed dataframes into the processsed data folder
"""

from __future__ import annotations
from pathlib import Path
from src.config import PROCESSED_DATA
import pandas as pd

class CSVWriter:
    """ writes dataframes to csv files"""

    @staticmethod
    def write(
        df : pd.DataFrame,
        file_name : str
    ) -> Path:
        
        PROCESSED_DATA.mkdir(
            parents = True,
            exist_ok= True
        )
        
        output_path = PROCESSED_DATA / file_name
        
        df.to_csv(
            output_path,
            index = False
        )
        
        print(f"output path -> {output_path}")
        
        return output_path