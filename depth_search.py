import threading
import wikipedia

MAX_THREADS = 125


def depth_search(user_start_page, depth_row, target_page, pages_hit, depth):
    """
    #user_start_page: the Wikipedia page instantiated from the user's command line arguments
    #depth_row: a list of links to all Wikipedia pages in a given depth
    #target_page: the Wikipedia page instantiated from the user's command line arguments
    #pages_hit: a hash map used to keep track of pages already seen
    #depth: an integer value representing the current depth

    Method that searches through all paths of one depth for descending
    """

    # check if the target page is the current depth
    global MAX_THREADS
    if found_in_current_depth(depth_row, target_page):
        print("Found the target page \"" + target_page.title + "\" at a depth of " + str(
            depth) + " from \"" + user_start_page.title + "\"")
        return depth
    print("Target page not found at depth " + str(depth))
    print("Building new search...")
    thread_list = []
    next_depth_row = []
    # iterate the page links for the current depth
    for link in depth_row:
        # check if already seen
        if link not in pages_hit:
            if len(thread_list) <= MAX_THREADS:
                new_thread = threading.Thread(target=build_next_depth, args=(link, next_depth_row, pages_hit, depth))
                thread_list.append(new_thread)
            else:
                for thread in thread_list: thread.start()
                for thread in thread_list: thread.join()
                thread_list = []
    # start and join threads, start depth search on next depthSearch
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    depth_search(user_start_page, next_depth_row, target_page, pages_hit, depth + 1)


def found_in_current_depth(current_depth_row, target_page):
    """
    #current_depth_row: a list of titles that reference Wikipedia articles
    #target_page: the Wikipedia page instantiated from the user's command line arguments

    Determines whether or not the target page is in the current depth
    """

    return target_page.title in current_depth_row


def build_next_depth(link, next_depth_row, pages_hit, depth):
    """
    #link: the current page link
    #next_depth_row: the list of pages to search in the next depth
    #pages_hit: the hash table containing the pages already visited

    Obtains the pages links from the Wikipedia API
    """

    print("Searching the \"" + link + "\" page at depth " + str(depth))
    pages_hit[link] = 1
    # build the next depth's link list
    get_links_for_search_terms(wikipedia.search(link), next_depth_row)
    return


def get_links_for_search_terms(results, depth_row):
    """
    #results: the output of a wikipedia.search() call
    #depth_row: links for the current row

    Encodes the search results and generates a list
    """

    for page in results:
        depth_row.append(page.encode("utf-8"))
    return
