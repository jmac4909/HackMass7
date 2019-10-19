import requests
import urllib.request

def getHtml(url):
  fp = urllib.requst.urlopen(url)
  html = fp.read()
  print(html)
  return html

print("test")
