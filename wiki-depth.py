import sys, wikipedia

def foundInCurrentDepth(currentDepthRow, targetPage):
	"""
	#currentDepthRow: a list of titles that reference Wikipedia articles
	#targetPage: the Wikipedia page instantiated from the user's command line arguments
	
	determines whether or not the target page is in the current depth
	"""

	return targetPage.title in currentDepthRow

def getLinksForSearchTerms(results):
	"""
	#results: the output of a wikipedia.search() call
	
	encodes the search results and generates a list
	"""

	pageTitles = []
	for page in results:
		pageTitles.append(page.encode("utf-8"))
	return pageTitles

def depthSearch(userStartPage, depthRow, targetPage, pagesHit, depth):
	"""
	#userStartPage: the Wikipedia page instantiated from the user's command line arguments
	#depthRow: a list of links to all Wikipedia pages in a given depth
	#targetPage: the Wikipedia page instantiated from the user's command line arguments
	#pagesHit: a hash map used to keep track of pages already seen
	#depth: an integer value representing the current depth

	recursive method that searchs through all paths of one depth for descending
	"""
	
	#check if the target page is the current depth
	if foundInCurrentDepth(depthRow, targetPage):
		print("Found the target page: " + targetPage.title + " at a depth of " + str(depth) + " from " + userStartPage.title)
		return depth
	print("Target page not found at depth " + str(depth))
	print("Building new search...")
	nextDepthRow = []
	#iterate the page links for the current depth
	for link in depthRow:
		#check if already seen
		if link not in pagesHit:
			print("Searching the \"" + link + "\" page at depth " + str(depth))
			pagesHit[link] = 1
			#build the next depth's link list
			nextDepthRow += getLinksForSearchTerms(wikipedia.search(link))
	#go to next depth
	depthSearch(userStartPage, nextDepthRow, targetPage, pagesHit, depth + 1)

"""
parse inputs, handle initial error checking, and kick off search
"""
userStartPage = wikipedia.page(sys.argv[1])
initialDepthRow = userStartPage.links
userTargetPage = wikipedia.page(sys.argv[2])
pagesSearched = {}
initialDepth = 0
depthSearch(userStartPage, initialDepthRow, userTargetPage, pagesSearched, initialDepth)