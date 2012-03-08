from xml.sax import make_parser
from xml.sax.handler import ContentHandler 
from collections import defaultdict
import sys



collaborations = [u'www', u'phdthesis', u'inproceedings', u'incollection', u'proceedings', u'book', u'mastersthesis', u'article']

#col = set([])


#authors = defaultdict(lambda: [])
authors = {}

import pdb


class DblpHandler(ContentHandler):
    def __init__(self):
        self.save = False
    def startElement(self, name, attrs):
        if name in collaborations:
            self.tmp = []
        if name == "author":
            #print attrs.getQNames()
            self.save = True
            self.newAuthor = []
        # if "mdate" in attrs.getQNames():
        #     col.add(name)
    def endElement(self,name):
        if name == "author":
            self.save = False
            self.tmp.append(''.join(self.newAuthor))

        if name in collaborations:
            #print self.tmp
            # for x in self.tmp:
            #     sys.stdout.write(x.encode("latin-1"))
            #     sys.stdout.write('\n')
            for i,author in enumerate(self.tmp):
                if author in authors:
                    authors[author].update(self.tmp[:i])
                else:
                    authors[author] = set(self.tmp[:i])
                authors[author].update(self.tmp[i+1:])
            del self.tmp

        

    def characters(self,ch):
        if self.save:
            self.newAuthor.append(ch)


dblp = DblpHandler()
saxparser = make_parser()
saxparser.setContentHandler(dblp)

datasource = open("dblp.xml","r")
saxparser.parse(datasource)

#print col


print 'HERE'
for author in authors:
    authors[author] = list(authors[author])


import pickle
authorsFile = open('authors','w')
pickle.dump(authors,authorsFile)
