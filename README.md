wiki-depth
==========

A multithreaded-Python script that finds the shortest path between two Wikipedia articles. It's powered by 
<a href = "https://github.com/goldsmith/Wikipedia">Goldsmith's Python-wrapped Wikipedia API</a> and written using Python 2.7. 
I wanted to experiment with the Wikipedia API in a meaningful way, however this is a quick project that I don't have any 
intention of expanding or maintaining.
 
To run the scripts, simply clone the repo and use the following command:<br>
<code>python WikiDepth.py < inputFile.in > outputFile.out</code>

The input file accepts lines of type:<br>
<code>"Start Page" "Target Page"</code>
Where <code>"Start Page"</code> and <code>"End Page"</code> are valid titles of Wikipedia articles. There is no error checking to make sure that these pages 
are valid.

Also inside the repo are a sample input file and a sample output file. The output contains a list of all the pages searched, 
as well as the depth that the links were found in. Due to Python's threading, the *.out files are somewhat poorly formatted.
