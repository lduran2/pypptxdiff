#!/usr/bin/env python3
r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/pptx2json.py
 Converts a PowerPoint presentation to JSON.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-14t13:17
 Version   : 1.0.1

 CHANGELOG :
    v1.0.1 - 2022-01-14t13:17
        added documentation

    v1.0.0 - 2022-01-14t12:59
        abstracted `each2json.py`
        opening each file

    v0.1.0 - 2021-12-31t02:53
        loop through filenames

    v0.0.0 - 2021-12-31t01:58
        hello world implementation
 '''

from sys import argv
from each2json import jsoneach
from pptx import Presentation

def main(argv):
    r'''
     Prints json representations of Presentations specified by the
     filenames in arguments argv.
     @param argv : [str] = commandline arguments containing filenames
     @minver 0.1.0
     '''
    jsoneach(argv[1:], Presentation)
# end def main(argv)

# if main module
if (__name__ == "__main__"):
    main(argv)
# end if (__name__ == "__main__")
