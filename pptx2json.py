#!/usr/bin/env python3
r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/pptx2json.py
 Converts a PowerPoint presentation to JSON.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2021-12-31t02:53
 Version   : 0.1.0

 CHANGELOG :
     v0.1.0 - 2021-12-31t02:53
         loop through filenames

     v0.0.0 - 2021-12-31t01:58
         hello world implementation
 '''

from sys import argv

def main(argv):
    # loop through arguments
    for filename in argv[1:]:
        print(filename)
    # next filename in argv[1:]
# end def main()

# if main module
if (__name__ == "__main__"):
    main(argv)
# end if (__name__ == "__main__")