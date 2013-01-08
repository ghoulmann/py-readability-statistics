#!/usr/bin/python
#generate flesch kincaid report
import sys
from readability import summarize
if len(sys.argv) == 2:
	text = sys.argv[1]
	summarize(text)
else:
	import Tkinter, tkFileDialog
	from tkFileDialog import askopenfilename
	root = Tkinter.Tk()
	root.withdraw()
	text = askopenfilename()
	f = file(text +'.summary.txt','w')
	sys.stdout = f
	summary = (summarize(text))
	f.close()


		
