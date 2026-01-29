from modules.recon.modules.base import ReconModule
import subprocess

class PassiveSubdomainRecon(ReconModule):
    def run(self) -> dict:
        result = {
            "module": "passive_subdomain",
            "target": self.target,
            "subdomains": [],
            "error": None
        }

        try:
            proc = subprocess.run(
                ["subfinder", "-d", self.target, "-silent"],
                capture_output=True,
                text=True,
                timeout=60
            )

            if proc.stdout:
                result["subdomains"] = proc.stdout.strip().split("\n")

        except Exception as e:
            result["error"] = str(e)

        return result
