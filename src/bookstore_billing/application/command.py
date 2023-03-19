from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Command(ABC):
    @abstractmethod
    def fqn(self) -> str:
        return NotImplemented
