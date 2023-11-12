def get_highest_common_divider(num_1: int, num_2: int) -> int:
    for factor in range(20, 0, -1):
        if num_1 % factor != 0:
            continue
        if num_2 % factor != 0:
            continue
        return factor
    return 1
