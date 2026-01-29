from abc import ABC, abstractmethod

class ReconModule(ABC):
    def __init__(self, target: str):
        self.target = target

    @abstractmethod
    def run(self) -> dict:
        pass
