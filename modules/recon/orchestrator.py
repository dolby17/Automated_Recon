from typing import List, Dict
from modules.recon.modules.base import ReconModule

class ReconOrchestrator:
    def __init__(self, targets: List[str]):
        self.targets = targets
        self.modules = []

    def register_module(self, module_cls):
        self.modules.append(module_cls)

    def run(self) -> Dict[str, list]:
        results = {}

        for target in self.targets:
            results[target] = []
            for module_cls in self.modules:
                module = module_cls(target)
                results[target].append(module.run())

        return results
