from collections.abc import Iterable

def compare(old: Iterable[str], new: Iterable[str]) -> dict[str, list[str]]:
    """Compare release names and return added and removed values."""
    a, b = set(old), set(new)
    return {"added": sorted(b - a), "removed": sorted(a - b)}
