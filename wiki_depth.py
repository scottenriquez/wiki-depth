from depth_search import *
import sys


def wiki_depth(reader, writer):
    """
    #reader: sys.in
    #writer: sys.out

    Run WikiDepth
    """
    for pair in parser(reader):
        """
        parse inputs, handle initial error checking, and kick off search
        """
        pair_list = list(pair)
        user_start_page = wikipedia.page(pair_list[1])
        initial_depth_row = user_start_page.links
        user_target_page = wikipedia.page(pair_list[3])
        pages_searched = {}
        initial_depth = 0
        depth_search(user_start_page, initial_depth_row, user_target_page, pages_searched, initial_depth)
        print("\n\n")


def parser(reader):
    """
    splits input based on the " character
    """
    return (map(str, line.split("\"")) for line in reader)


wiki_depth(sys.stdin, sys.stdout)
