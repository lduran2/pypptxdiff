#!/usr/bin/env python3
r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/each2json.py
 Converts a PowerPoint presentation to JSON.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-14t12:53
 Version   : 1.0.0

 CHANGELOG :
    v1.0.0 - 2022-01-14t12:53
        abstracted from pptx2json.py
        opening each file

    v0.1.0 - 2021-12-31t02:53
        pptx2json.py :
            loop through filenames

    v0.0.0 - 2021-12-31t01:58
        pptx2json.py :
            hello world implementation
 '''

def jsoneach(filenames, openfunc):
    # loop through arguments
    for filename in filenames:
        print(openfunc(filename))
    # next filename in filenames
# end def jsoneach(filenames, openfunc)
