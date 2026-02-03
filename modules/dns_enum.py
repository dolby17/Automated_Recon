import dns.resolver
from typing import List

from modules.base import ReconModule
from core.context import ReconContext


class DNSEnumerationModule(ReconModule):
    """
    Performs DNS enumeration for common record types.
    """

    name = "dns_enumeration"

    RECORD_TYPES: List[str] = ["A", "AAAA", "MX", "NS", "TXT"]

    def run(self, context: ReconContext) -> None:
        domain = context.target
        results = {}

        for record_type in self.RECORD_TYPES:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                results[record_type] = [str(rdata) for rdata in answers]
            except Exception:
                results[record_type] = []

        context.dns_records = results
