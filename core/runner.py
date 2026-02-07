from modules.recon.orchestrator import ReconOrchestrator

# Import recon modules here
from modules.dns_enum import DNSEnumerationModule
from modules.subdomain_enum import SubdomainEnumerationModule
from modules.ip_resolution import IPResolutionModule
from modules.port_scan import PortScanModule


def run(targets, options=None):
    """
    Central execution runner.
    Returns ReconContext per target.
    """

    orchestrator = ReconOrchestrator(targets)

    # Register Phase 2 recon modules (ORDER MATTERS)
    orchestrator.register_module(DNSEnumerationModule)
    orchestrator.register_module(SubdomainEnumerationModule)
    orchestrator.register_module(IPResolutionModule)
    orchestrator.register_module(PortScanModule)

    # Execute workflow
    results = orchestrator.run()

    for context in results.values():
        context.finalize()

    return results
