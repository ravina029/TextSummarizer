from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)  #this is not python class but dataclass, here you can define the veriables without using self keyword.
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path


@dataclass(frozen=True)  #this is not python class but dataclass, here you can define the veriables without using self keyword.
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    ALL_REQUIRED_FILES:list


@dataclass(frozen=True)  #this is not python class but dataclass, here you can define the veriables without using self keyword.
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path