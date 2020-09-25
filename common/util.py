def full_range(start, stop): return range(start, stop + 1)


def get_percentage(part, whole):
    if whole == 0:
        return 0
    return 100 * float(part) / float(whole)
