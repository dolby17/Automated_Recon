import re


_DOMAIN_REGEX = re.compile(
    r"^(?!\-)(?:[a-zA-Z0-9\-]{1,63}\.)+[a-zA-Z]{2,63}$"
)


def is_valid_domain(domain: str) -> bool:
    if not domain:
        return False

    if domain.replace(".", "").isdigit():
        return False

    return bool(_DOMAIN_REGEX.fullmatch(domain))
