class VulnContext:
    """
    Shared context for vulnerability checks.
    Comes from recon phase.
    """

    def __init__(self, headers=None, ports=None, urls=None):
        self.headers = headers or {}
        self.ports = ports or []
        self.urls = urls or []
