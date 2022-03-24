
opening_brackets = "([{<"
closing_brackets = ")]}>"

def check_navdata(nav: str) -> bool:
    """Validates a navigation subsystem's data

    Checks navigation data for corrupted chunks and returns a boolean indicating whether the nav data is valid or not.
    """
    nav_stack = []

    for char in nav:
        if char in opening_brackets:
            nav_stack.append(char)
        if char in closing_brackets:
            chunk_opener = nav_stack.pop()
            # TODO(arepavich): Investigate pairing chunk openers/closers to allow concise checking of characters
            if char == ")" and chunk_opener != "(":
                return False
            elif char == "]" and chunk_opener != "[":
                return False
            elif char == "}" and chunk_opener != "{":
                return False
            elif char == ">" and chunk_opener != "<":
                return False

    return True


if __name__ == '__main__':
    pass
