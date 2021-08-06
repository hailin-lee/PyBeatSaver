from dataclasses import dataclass

from dataclasses_json import dataclass_json

from src.pybeatsaver.models.fields import default


@dataclass_json
@dataclass
class MapParitySummary:
    errors: int = default()
    resets: int = default()
    warns: int = default()

