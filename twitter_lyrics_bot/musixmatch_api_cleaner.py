import requests 
import json 
import random 
from os import environ

#musixmatch api base url
base_url = "https://api.musixmatch.com/ws/1.1"

#your api key
api_key = environ['MUSIXMATCH_api_key']
sp_chars = [".","'","/","?","#",'@',"'",',','/','-']

#api methods
lyrics_matcher = "matcher.lyrics.get"
track_matcher = "matcher.track.get"

# format url 
format_url = "?format = json&callback=callback"

#parameters
artist_search_parameter = "&q_artist="
track_search_parameter = "&q_track="

def find_nth(haystack, needle, n):
  """Find the nth occurence of substring in a string."""
  start = haystack.find(needle)
  while start >= 0 and n>1:
    start = haystack.find(needle,start+len(needle))
    n-=1
  return start

def getLine(list):
  """Get line from list iterator"""
  no = (list.count('\n'))
  no = int(no)
  n=random.randint(1,no-1)
  start = find_nth(list,'\n',n)
  end = find_nth(list,'\n',n+1)
  line = list[start:end].replace('\n','')
  return line
