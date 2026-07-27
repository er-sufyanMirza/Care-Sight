""" FILE MANAGER UTILITIES

Responsible for reading and writing project files
"""

from __future__ import annotations
from datetime import datetime
from typing import Any
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
    def create_timestamp() -> str:
        """ return a timestamp suitable for filenames
        
        example: 3494885_8585858
        """
        return datetime.now().strftime("%Y%m%d_%H%M%S")
        
        
    @staticmethod
    def get_resource_directory(resource : str) -> Path:
        """ return the raw data directory for FHIR resource """
        directory = RAW_DATA/resource
        
        FileManager.ensure_directory(directory)
        
        return directory
        
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
        
    @staticmethod
    
    def load_json(path : Path) -> Any:
        
        """load json from disc """
        
        with open(path, "r", encoding = "utf-8") as file:
            return json.load(file)
        