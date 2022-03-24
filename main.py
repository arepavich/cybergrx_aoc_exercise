from typing import Tuple

CHUNK_METADATA = {
    'parens': {
        'opener': "(",
        'closer': ")",
        'points': 3,
        'autocomplete_points': 1
    },
    'square': {
        'opener': "[",
        'closer': "]",
        'points': 57,
        'autocomplete_points': 2
    },
    'curly': {
        'opener': "{",
        'closer': "}",
        'points': 1197,
        'autocomplete_points': 3
    },
    'angle': {
        'opener': "<",
        'closer': ">",
        'points': 25137,
        'autocomplete_points': 4
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


def repair_navdata(nav: str) -> Tuple[str, int]:
    """Autocompletes navdata lines which are incomplete.

    Args:
        nav: A string containing navigation chunks

    Returns:
        A tuple containing a string representing the repaired navdata and
        an integer representing the autocomplete score.
    """

    # TODO(arepavich): Refactor this to leverage the initial processing already done by check_navdata
    nav_stack = []
    for char in nav:
        if char in OPENING_BRACKETS:
            nav_stack.append(char)
        if char in CLOSING_BRACKETS:
            nav_stack.pop()

    score = 0
    while len(nav_stack) > 0:
        chunk_opener = nav_stack.pop()
        for chunk_type in CHUNK_METADATA.values():
            if chunk_opener == chunk_type.get('opener'):
                nav = f"{nav}{chunk_type.get('closer')}"
                score = (score * 5) + chunk_type.get('autocomplete_points')

    return nav, score


if __name__ == '__main__':
    validation_score = 0
    with open("inputs.txt", "r") as f:
        for navdata in f.readlines():
            validation_score += check_navdata(navdata)

    print(validation_score)
