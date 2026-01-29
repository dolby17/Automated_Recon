from modules.recon.modules.base import ReconModule

class DummyRecon(ReconModule):
    def run(self) -> dict:
        return {
            "module": "dummy",
            "target": self.target,
            "status": "ok"
        }
