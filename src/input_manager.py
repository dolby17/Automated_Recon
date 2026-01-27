from typing import List, Union

def normalize_targets(raw: Union[str, list[str]]) -> List[str]:
    if isinstance(raw, str):
        raw_items = [raw]
    elif isinstance(raw, list):
        raw_items = raw
    else:
        raise TypeError("Unsupported input type")

    seen = set()
    normalized: List[str] = []

    for item in raw_items:
        if not isinstance(item, str):
            continue

        value = item.strip().lower()

        if not value:
            continue

        if value.startswith("https://"):
            value = value[len("https://"):]
        elif value.startswith("http://"):
            value = value[len("http://"):]

        value = value.rstrip("/")

        if value not in seen:
            seen.add(value)
            normalized.append(value)

    if not normalized:
        raise ValueError("No valid targets provided")

    return normalized
