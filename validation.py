def validScore(value) -> int:
    intValue = value
    try:
        intValue = int(intValue)
    except ValueError:
        raise ValueError("Invalid Scores")
    if 0 <= intValue <= 10:
        return intValue
    raise ValueError("Invalid Scores")


def validInteger(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def valueToInteger(value):
    if validInteger(value):
        return int(value)
    else:
        raise ValueError("The given value is not a valid integer!")


def validPositon(participants: list, pos) -> int:
    pos = valueToInteger(pos)
    if pos >= len(participants):
        raise ValueError("The position is not valid!")
    return pos


def validProblemNumber(value) -> str:
    problems = ["P1", "P2", "P3"]
    if value not in problems:
        raise ValueError("Invalid problem number!")
    return value


def validRelation(value):
    relations = ["<", ">", "="]
    if value in relations:
        return value
    raise ValueError("Invalid relation!")
