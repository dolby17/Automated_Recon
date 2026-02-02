from modules.recon.orchestrator import ReconOrchestrator
from modules.recon.modules.subdomain_passive import PassiveSubdomainRecon


def run(targets, options=None):
    """
    Central execution runner.
    Phase 1 Step 4: Orchestration only.

    Args:
        targets (list[str]): List of target domains
        options (dict | None): CLI/options context (unused in Phase 1)

    Returns:
        dict: Aggregated reconnaissance results
    """

    # Initialize orchestrator with targets
    orchestrator = ReconOrchestrator(targets)

    # Register Phase 1 passive recon module
    orchestrator.register_module(PassiveSubdomainRecon)

    # Execute recon workflow
    results = orchestrator.run()

    return results
