def get_highest_common_divider(num_1: int, num_2: int) -> int:
    """Returns `1` if `num_1` and `num_2` don't have common divider. Otherwise retruns common divider."""

    for factor in range(100, 0, -1):
        if num_1 % factor != 0:
            continue
        if num_2 % factor != 0:
            continue
        return factor
    return 1
