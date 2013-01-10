#!/usr/bin/env python
import sys
import cgi, os
import cgitb; cgitb.enable()
from web_readability import websummarize

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass
target = '/var/www/readability/files/'
form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open(target +'temp.txt', 'wb').write(fileitem.file.read())
#   text = text.read
#   text = text.close
    s = target +'temp.txt'
    websummarize(s)
   #Open uploaded text
#    text = open('fn', 'w')
#    message = (websummarize(text))
 #   s = s.close()
else:
   message = 'No file was uploaded'
   print """\
   Content-Type: text/html\n
   <html><body>
   <p>%s</p>
   </body></html>
   """ % (message,)
