def count_items(items: list) -> dict:
    if not isinstance(items, list):
        raise TypeError("Input must be a list")

    counts = {}

    for item in items:
        try:
            counts[item] = counts.get(item, 0) + 1
        except TypeError:
            raise TypeError("All items must be hashable")

    return counts

print(count_items(["a", "b", "a", "c", "c", "c"]))