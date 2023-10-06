from __future__ import annotations
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Union

PACKAGE_ROOT = Path(__file__).resolve().parents[2]

@dataclass
class Config:
    chart_studio_username: str
    chart_studio_api_key: str
    inventory_path: str
    corr_plots_folder: str
    watermark_path: str
    config_file: Path
    
    @classmethod
    def set_config_file(cls, config_file: Union[Path, str] = PACKAGE_ROOT / 'config.json'):
        config_file = Path(config_file)
        cls.config_file = config_file
    
    @classmethod
    def read_config(cls) -> Config:
        try:
            with open(cls.config_file, 'r') as file:
                config_data = json.load(file)
        except FileNotFoundError:
            print('No config file found. Try setting it with `Config.set_config_file()` first.')
        else:
            return cls(**config_data)

Config.set_config_file()
