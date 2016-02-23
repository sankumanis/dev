#!/user/bin/python
#### example of low memory Simple API for XML (SAX) usage
## SAX does not read the whole file in memory
## this is slow but less memory intensive

import xml.sax

# create your own ContentHandler by subclassing xml.sax.ContentHandler
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentTag = ""
        self.title = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""
    
    def startDocument(self):
        print "Starting document"
        print "##################################################"
        
    def endDocument(self):
        print "Ending document"
        print "##################################################"
    
    def startElement(self, tag, attributes):
        self.CurrentTag = tag
        if self.CurrentTag == "movie":
            self.title = attributes["title"]
    
    # called when the content of each tag is read
    def characters(self, content):
        if self.CurrentTag == "type":
            self.type = content
        elif self.CurrentTag == "format":
            self.format = content
        elif self.CurrentTag == "year":
            self.year = content
        elif self.CurrentTag == "rating":
            self.rating = content
        elif self.CurrentTag == "stars":
            self.stars = content
        elif self.CurrentTag == "description":
            self.description = content
    
    def toString(self):
        print "%s\n**************************************\n%s, %s, %s, %s, %s\n********************" %(self.title, self.type, self.year, self.rating, self.stars, self.description)
    
    # called when end tag is read
    def endElement(self, tag):
        self.CurrentTag = None
        if tag == "movie":
            #print "%s\n********************\n%s, %s, %s, %s, %s\n********************" %(self.title, self.type, self.year, self.rating, self.stars, self.description)
            self.toString()
            



if __name__ == "__main__":
    
    # create a new SAX (Simple API for XML) parser
    parser = xml.sax.make_parser()
    # set naspace to be false
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # create instance of the MovieHandler
    movieHandler = MovieHandler()
    # set the parser with the handler
    parser.setContentHandler(movieHandler)
    # parse the movies.xml document
    parser.parse("../data/movies.xml")
    
    





    
    
    
    
        
            
        