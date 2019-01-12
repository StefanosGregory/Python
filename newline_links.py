from bs4 import BeautifulSoup
import urllib2
print "Welcome to newLine&Links finder"
link = raw_input("Give a link (http://www.example.com): ")
type(link)
response = urllib2.urlopen(link)
page_source = response.read()
#print page_source
soup = BeautifulSoup(page_source, 'html.parser')
br = soup.find_all('br')
p = soup.find_all('p')
links = soup.find_all('a')
#print br
print "New line with br :",len(br)
#print p
print "New line with p :",len(p)
print "Links :", len(links)
