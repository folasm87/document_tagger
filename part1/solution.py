import re
import sys
from pg_sample_texts import DIV_COMM, MAG_CART
 
documents = [DIV_COMM, MAG_CART]

title_search = re.compile(r'(title:\s*)(?P<title>.*\s*.*)', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

 
# first we need to do something with the user supplied keywords
# which we're getting with sys.argv. Remember, the script name itself
# is at index 0 in sys.argv, so we'll slice everything from index 1 forward.
searches = {}
for kw in sys.argv[1:]:
  searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
 
for i, doc in enumerate(documents):
  title = re.search(title_search, doc).group('title')
  author = re.search(author_search, doc)
  translator = re.search(translator_search, doc)
  illustrator = re.search(illustrator_search, doc)
  if author: 
    author = author.group('author')
  if translator:
    translator = translator.group('translator')
  if illustrator:
    illustrator = illustrator.group('illustrator')

  print "***" * 25
  
  print "Here's the info for doc {}:".format(i)
  print "Title:  {}".format(title)
  print "Author(s): {}".format(author)
  print "Translator(s): {}".format(translator)
  print "Illustrator(s): {}".format(illustrator)
  print "\n"

  print "Here's the keyword info for doc {}:".format(i)
  for search in searches:
    print "\"{0}\": {1}".format(search, len(re.findall(searches[search], doc)))