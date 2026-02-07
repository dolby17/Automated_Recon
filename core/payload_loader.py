class PayloadLoader:
    """
    Loads payloads from payload files.
    """

    def __init__(self, base_path="payloads"):
        self.base_path = base_path

    def load(self, name):
        """
        Load payloads by filename (without extension).

        Example:
            load("xss") → payloads/xss.txt
        """
        payloads = []
        path = f"{self.base_path}/{name}.txt"

        try:
            with open(path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        payloads.append(line)
        except FileNotFoundError:
            print(f"[!] Payload file not found: {path}")

        return payloads
    
        if not payloads:
            print(f"[!] No payloads loaded for: {name}")

