r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/each2json.py
 Converts files to JSON.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-14t13:54
 Version   : 1.7.0
 '''

import json
# to convert to dictionary between file and JSON
from dictclasses import asdict

def jsoneach(filenames, openfunc):
    r'''
     Prints json representations of objects representing each file
     specified by the filenames created using the openfunc.
     @param filenames : [str] = list of names of files
     @param openfunc : function = to create the object representing an
        open file
     @minver 1.0.0
     '''
    # loop through arguments
    for filename in filenames:
        # open the file
        file = openfunc(filename)
        # convert to dictionary
        a_dict = asdict(file)
        # convert to JSON
        a_json = json.dumps(a_dict, sort_keys=True, indent=4)
        # print the result
        print(a_json)
    # next filename in filenames
# end def jsoneach(filenames, openfunc)
