# newsApiProject
A program that uses NewsAPI to get relevant news stories and write them to a latex file (that can then be compiled and emailed, read, etc...)

Requires a newsAPI key, an installed TEX distribution, and the pylatex package (which can be installed via pip). This program 
will NOT work "out of the box" - it requires an additional file called api.py that contains a newsAPI key stored in a variable
called apiKey. After acquiring this key, the user should put api.py in the same folder as newsApi.py and simply run newsApi.py. 

News sources and topics are specified in the source code itself - next steps include adding a GUI, additional functionality, and user customizability in the form of optional inputs - like say news articles from within a time frame.
