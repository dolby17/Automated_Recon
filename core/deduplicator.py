def deduplicate(findings):
    """
    Remove duplicate findings.
    """

    seen = set()
    unique = []

    for f in findings:
        key = (
            f.get("vulnerability"),
            f.get("url"),
            f.get("payload"),
        )

        if key in seen:
            continue

        seen.add(key)
        unique.append(f)

    return unique
