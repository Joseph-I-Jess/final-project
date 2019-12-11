#!/usr/bin/env python3
"""
Make strings unto tuples.

Makes strings unto tuples, as was foretold.
(The strings in question are in the following format: "(2, 1, 2)\n"; they are
stripped of punctuation, the numbers are extracted, and they are crammed into
tuples, which are returned.)

Gareth Miller, Tony Sierra, Srikar Valluri
"""


def tuple_izer(line):
    """
    Turn a string into a tuple.

    Turns a string of the format "(2, 1, 2)\n" into a tuple, by first removing
    newline characters, then spaces, then punctuation, and finally by plucking
    out the numbers, turning them into integers, and stuffing them into a
    tuple, which is then returned.

    Parameters
    ----------
    line : str
        A string in the format of "(2, 1, 2)\n" to be converted into a tuple.

    Returns
    -------
    line : tuple
        The resultant tuple from above.

    """
    import string
    from not_a_number import NotANumberError
    line = line.replace("\n","")
    line = line.replace(" ","")
    line = line.translate(line.maketrans("","", string.punctuation))
    line = line.translate(line.maketrans("","", string.ascii_lowercase))
    line = line.translate(line.maketrans("","", string.ascii_uppercase))
    try:
        if len(line) != 0:
            p1_win = int(line[0])
            p2_win = int(line[1])
            draw = int(line[2])
            line = (p1_win, p2_win, draw)
            return line
        else:
            raise NotANumberError
    except NotANumberError:
        return "(text input)"

# Testing Material:

# test = "(0, 1, 2)"
# print(test)
# test = tuple_izer(test)
# print(test)
