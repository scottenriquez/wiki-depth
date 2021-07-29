wiki-depth
==========

A multithreaded Python script that finds the shortest path between two Wikipedia articles. It's powered by 
<a href = "https://github.com/goldsmith/Wikipedia">Goldsmith's Python-wrapped Wikipedia API</a> and written using Python 3.9. I wanted to experiment with the Wikipedia API in a meaningful way, however this is a quick project that I don't have any intention of expanding or maintaining.
 
To run the scripts, simply clone the repo and use the following command:<br>
<code>python wiki_depth.py < input_file.in > output.out</code>

The input file accepts lines of type:<br>
<code>"Start Page" "Target Page"</code>
Where <code>"Start Page"</code> and <code>"End Page"</code> are valid titles of Wikipedia articles. There is no error checking to make sure that these pages are valid.

Note that if a large number of the HTTP requests begin to fail, try reducing the number of threads by changing the global variable <code>MAX_THREADS</code>.