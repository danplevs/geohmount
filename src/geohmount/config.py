from __future__ import annotations
from dataclasses import dataclass
import json
from pathlib import Path

@dataclass
class Config:
    chart_studio_username: str
    chart_studio_api_key: str
    inventory_path: str
    corr_plots_folder: str
    config_file: Path = Path(__file__).resolve().parents[2] / 'config.json'
    
    @classmethod
    def set_config_file(cls, config_file: Path):
        cls.config_file = config_file
    
    @classmethod
    def read_config(cls) -> Config:
        with open(cls.config_file, 'r') as file:
            config_data = json.load(file)
            return cls(**config_data)
        
    