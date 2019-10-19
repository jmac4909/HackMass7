import requests
import urllib.request
from googlesearch import search
from selenium import webdriver

driverPath = "C:\\Users\\danzhang41\\Desktop\\Workspaces\\Hackathon\\HackUMass7"

def getHTML(url,path):
  driver = webdriver.Chrome(path)
def getHtml(url):
  fp = urllib.request.urlopen(url)
  html = fp.read()
  print(html)
  return html

def Google_search(query, start, stop):
  #if you want to verify these, go to chrome incognito tab, search the query, then append &gl=us&pws=0 to the end of the
  # resulting url and hit enter
  results= []
  for j in search(query, num=10, start = start, stop=stop, pause=1): #pause is how long in second you want to wait for request
      results.append(j)
      print(j)
  return results



#result = Google_search("water bottle",1,2)
#print(result)
##print(html)



#print(Google_search("water bottle", 1, 5))
