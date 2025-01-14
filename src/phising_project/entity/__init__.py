
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfiguration:
    root_dir_name: Path
    data_set_url: str
    local_data_path: Path
    unzip_data_path: Path