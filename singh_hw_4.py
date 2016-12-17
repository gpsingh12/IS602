import bs4
from bs4 import BeautifulSoup
import urllib2


url= "http://businessoverbroadway.com/top-10-skills-in-data-science"
page = urllib2.urlopen(url)
soup = bs4.BeautifulSoup(page.read(), 'html.parser')
mytext = soup.find('p').getText()

print mytext



#Take this text and store it in the program to use in the next step.


# Part 2

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

response = alchemyapi.keywords('text', mytext)
print "Keywords"   '\t'  '\t' "Relevance"
for kyw in response['keywords'][1:10]:
        k1=  kyw['text']
        r1=  kyw['relevance']
        print "              "
        print "--------------------------------------"
        print k1, '\t', '\t', r1
