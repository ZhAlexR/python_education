"""Module description should be here"""


def func(elem1: str, elem2: str) -> str:
    """Some short function description
    A little bit more description
    """
    return f"{elem1} + {elem2}"


print(func.__doc__)
