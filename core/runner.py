from modules.recon.orchestrator import ReconOrchestrator
from modules.recon.modules.subdomain_passive import PassiveSubdomainRecon


def run(args):
    """
    Main execution runner – Phase 1 Step 5 (Passive Recon).
    """

    # ----------------------------
    # 1. Target handling
    # ----------------------------
    target = args.target
    targets = [target]

    # ----------------------------
    # 2. Recon Phase
    # ----------------------------
    print("[+] Running reconnaissance phase")

    orchestrator = ReconOrchestrator(targets)
    orchestrator.register_module(PassiveSubdomainRecon)

    results = orchestrator.run()

    # ----------------------------
    # 3. Print results
    # ----------------------------
    if not results:
        print("[!] No recon results returned")
        return

    for t, outputs in results.items():
        print(f"[+] Recon results for {t}")
        for output in outputs:
            print(output)
