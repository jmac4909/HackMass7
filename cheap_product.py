import requests
import urllib.request

def getHtml(url):
  fp = urllib.request.urlopen(url)
  html = fp.read()
  print(html)
  return html

def Google_search(query, start, stop):
    #if you want to verify these, go to chrome incognito tab, search the query, then append &gl=us&pws=0 to the end of the
    # resulting url and hit enter
    results= []
    for j in search(query, num=10, start = start, stop=stop, pause=1):
        results.append(j)
        print(j)
    return results
