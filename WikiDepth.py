import sys, wikipedia
from DepthSearch import *

def wikiDepth(reader, writer):
	for pair in parser(reader):
		"""
		parse inputs, handle initial error checking, and kick off search
		"""
		userStartPage = wikipedia.page(pair[1])
		initialDepthRow = userStartPage.links
		userTargetPage = wikipedia.page(pair[3])
		pagesSearched = {}
		initialDepth = 0
		depthSearch(userStartPage, initialDepthRow, userTargetPage, pagesSearched, initialDepth)
		print("\n\n")

def parser(reader):
	"""
	splits input based on the " character
	"""
	return (map(str, line.split("\"")) for line in reader)

wikiDepth(sys.stdin, sys.stdout)
