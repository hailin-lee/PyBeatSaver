from abc import abstractmethod

from src.pybeatsaver.models.enum.base_enum import BaseEnum


class HumanEnum(BaseEnum):
    @abstractmethod
    def human_readable(self) -> str:
        pass