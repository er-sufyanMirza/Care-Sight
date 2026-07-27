""" FILE MANAGER UTILITIES

Responsible for reading and writing project files
"""

from __future__ import annotations
import json
from pathlib import Path

from src.config import RAW_DATA

class FileManager:
    """ utilities class for file operations"""
    
    @staticmethod
    def ensure_directory(path: Path) -> None:
        "create directory if it does not exists"
        
        path.mkdir(parents = True, exist_ok = True)
        
    @staticmethod
    def save_json(
        data : dict,
        folder : str,
        filename: str,
    ) -> Path:
        """ save json data to raw data folder
        
        return the saved file path.
        """
        
        directory = RAW_DATA/folder
        
        FileManager.ensure_directory(directory)
        
        file_path = directory/filename
        
        with open(file_path, "w", encoding = "utf-8") as file:
            json.dump(
                data,
                file,
                indent = 4,
                ensure_ascii= False,
            )
            
            return file_path