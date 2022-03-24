CHUNK_METADATA = {
    'parens': {
        'opener': "(",
        'closer': ")",
        'points': 3
    },
    'square': {
        'opener': "[",
        'closer': "]",
        'points': 57
    },
    'curly': {
        'opener': "{",
        'closer': "}",
        'points': 1197
    },
    'angle': {
        'opener': "<",
        'closer': ">",
        'points': 25137
    }
}


OPENING_BRACKETS = "".join(map(lambda x: x.get('opener'), CHUNK_METADATA.values()))
CLOSING_BRACKETS = "".join(map(lambda x: x.get('closer'), CHUNK_METADATA.values()))


def check_navdata(nav: str) -> int:
    """Validates a navigation subsystem's data.

    Args:
        nav: A string containing navigation chunks.

    Returns:
        An integer indicating the point value of the first illegal character encountered.
        0 if the supplied navdata is valid.
    """

    nav_stack = []

    for char in nav:
        if char in OPENING_BRACKETS:
            nav_stack.append(char)
        if char in CLOSING_BRACKETS:
            chunk_opener = nav_stack.pop()
            for chunk_type in CHUNK_METADATA.values():
                if char == chunk_type.get('closer') and chunk_opener != chunk_type.get('opener'):
                    return chunk_type.get('points')

    return 0


if __name__ == '__main__':
    score = 0
    with open("inputs.txt", "r") as f:
        for navdata in f.readlines():
            score += check_navdata(navdata)

    print(score)

