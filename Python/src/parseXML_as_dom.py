#!/usr/bin/python
from xml.dom.minidom import parse
import xml.dom.minidom

class Movie:
    def __init__(self, title):
        self.title = title
        self.type = ""
        self.format = ""
        self.rating = ""
        self.year = ""
    
    def setType(self, type):
        self.type = type
    
    def setFormat(self, format):
        self.format = format
    
    def setRating(self, rating):
        self.rating = rating
        
    def setYear(self, year):
        self.year = year
    
    def __str__(self):
        return "%s\n**************************************\n%s, %s, %s\n" %(self.title, self.type, self.format, self.year)
        
    


DOMTree = parse("../data/movies.xml")
collection = None
if (DOMTree.documentElement.tagName == "collection"):
    collection = DOMTree.documentElement
movieNodes = []
movies = [] # list of movie objects
if collection:
    movieNodes = collection.getElementsByTagName("movie")

nodeList = None
for movieNode in movieNodes:
    if movieNode.hasAttribute("title"):
        # build movie object
        movie = Movie(movieNode.getAttribute("title"))
        #print movieNode.getAttribute("title")
        #print "########################"
        # get all the [type] tags
        nodeList = movieNode.getElementsByTagName("type")
        if nodeList:
            for node in nodeList:
                for childNode in node.childNodes:
                    #print childNode.data
                    movie.setType(childNode.data)
            nodeList = None
        
        # get all the [format] tags
        nodeList = movieNode.getElementsByTagName("format")
        if nodeList:
            for node in nodeList:
                for childNode in node.childNodes:
                    #print childNode.data
                    movie.setFormat(childNode.data)
            nodeList = None
        
        # get all the [year] tags
        nodeList = movieNode.getElementsByTagName("year")
        if nodeList:
            for node in nodeList:
                for childNode in node.childNodes:
                    #print childNode.data
                    movie.setYear(childNode.data)
            nodeList = None
        
        
        # end of one movieNode
        movies.append(movie)

if len(movies) > 0:
    for movie in movies:
        print movie
    
        
        
                
        
        