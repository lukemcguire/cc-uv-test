def foo(bar: str) -> str:
    """Tautological Function.

    Returns whatever string is supplied to it.

    Args:
        bar: Some string.

    Returns:
        Whatever you gave it.
    """

    return bar


def bar() -> str:
    """Just returns 'bar'.

    This function takes no variables and returns 'bar'.
    It's pretty useless.

    Returns:
        'bar'.  That's it.
    """
    return "bar"


if __name__ == "__main__":  # pragma: no cover
    pass
