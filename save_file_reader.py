#!/usr/bin/env python3
"""
Read the save log and turn its contents into a list of tuples.

Reads the save log and turns its contents into a list of tuples.
"""


def reader(list_games):
    """
    Placeholder
    """
    from the_tuple_izer import tuple_izer
    try:
        with open("save_log.txt", "r") as in_file:
            past_record = in_file.readlines()
            list_games = []
            for line in past_record:
                line = tuple_izer(line)
                list_games.append(line)
    except FileNotFoundError:
        in_file = open("save_log.txt", "x")
        in_file = open("save_log.txt", "r")
        past_record = in_file.readlines()
        list_games = []
        for line in past_record:
            line = tuple_izer(line)
            list_games.append(line)
        in_file.close()
    return list_games
