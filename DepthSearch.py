import sys, wikipedia, threading

def depthSearch(userStartPage, depthRow, targetPage, pagesHit, depth):
	"""
	#userStartPage: the Wikipedia page instantiated from the user's command line arguments
	#depthRow: a list of links to all Wikipedia pages in a given depth
	#targetPage: the Wikipedia page instantiated from the user's command line arguments
	#pagesHit: a hash map used to keep track of pages already seen
	#depth: an integer value representing the current depth

	threaded recursive method that searchs through all paths of one depth for descending
	"""
	
	#check if the target page is the current depth
	if foundInCurrentDepth(depthRow, targetPage):
		print("Found the target page: " + targetPage.title + " at a depth of " + str(depth) + " from " + userStartPage.title)
		return depth
	print("Target page not found at depth " + str(depth))
	print("Building new search...")
	threadList = []
	nextDepthRow = []
	#iterate the page links for the current depth
	for link in depthRow:
		#check if already seen
		if link not in pagesHit:
			newThread = threading.Thread(target = buildNextDepth, args = (link, nextDepthRow, pagesHit, depth))
			threadList.append(newThread)
	#start and join threads, start depth search on next depthSearch
	for thread in threadList: thread.start()
	for thread in threadList: thread.join()
	depthSearch(userStartPage, nextDepthRow, targetPage, pagesHit, depth + 1)

def foundInCurrentDepth(currentDepthRow, targetPage):
	"""
	#currentDepthRow: a list of titles that reference Wikipedia articles
	#targetPage: the Wikipedia page instantiated from the user's command line arguments
	
	determines whether or not the target page is in the current depth
	"""

	return targetPage.title in currentDepthRow

def buildNextDepth(link, nextDepthRow, pagesHit, depth):
	"""
	#link: the current page link
	#nextDepthRow: the list of pages to search in the next depth
	#pagesHit: the hash table containing the pages already visited

	obtains the pages links from the Wikipedia API
	"""
	print("Searching the \"" + link + "\" page at depth " + str(depth))
	pagesHit[link] = 1
	#build the next depth's link list
	getLinksForSearchTerms(wikipedia.search(link), nextDepthRow)
	return

def getLinksForSearchTerms(results, depthRow):
	"""
	#results: the output of a wikipedia.search() call
	#depthRow: links for the current row

	encodes the search results and generates a list
	"""

	for page in results:
		depthRow.append(page.encode("utf-8"))
	return