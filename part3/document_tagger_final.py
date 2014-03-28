import re, sys, os

def open_files():
    dir = sys.argv[1]
    documents = []
    for fl in (os.listdir(dir)):  #for each item that appears in the directory
        if fl.endswith('.txt'):       #if it's a text file
            print 'Processing {0}.'.format(fl)
    
            fl_path = os.path.join(dir, fl) #the full path to the file is the directory plus
                                                  #the file name
    
            with open(fl_path, 'r') as f:         #open the file as f
                full_text = f.read()    
                documents.append(full_text)
                
    return documents

def compile_kw():
    searches = {}
    for kw in sys.argv[2:]:
        searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
    return searches

def count_kw(full_text, title, searches):
    #title_search = re.compile(r'(title:\s*)(?P<title>.*)', re.IGNORECASE)
    #title = re.search(title_search, full_text).group('title')
    print "Here's the keyword info for {}:".format(title)
    for search in searches:
        print "\"{0}\": {1}".format(search, len(re.findall(searches[search], full_text)))

def get_metadata(full_text, searches):
    title_search = re.compile(r'(title:\s*)(?P<title>.*\s*.*)', re.IGNORECASE)
    author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
    translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
    illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
    
    title = re.search(title_search, full_text).group('title')
    author = re.search(author_search, full_text)
    translator = re.search(translator_search, full_text)
    illustrator = re.search(illustrator_search, full_text)
    if author: 
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')

    print "***" * 25
    print "Title:  {}".format(title)
    print "Author(s): {}".format(author)
    print "Translator(s): {}".format(translator)
    print "Illustrator(s): {}".format(illustrator)
    print "---" * 25
    print '{0} is {1} characters long'.format(title, len(full_text))
    print "---" * 25
    count_kw(full_text, title, searches)
   
    
def main(argv=sys.argv):
    docs = open_files()
    keywords = compile_kw()
    for doc in docs:
        get_metadata(doc, keywords)
        #count_kw(keywords, doc)



if __name__ == '__main__':  
   main()
