r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/each2json.py
 Converts files to JSON.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-14t13:15
 Version   : 1.0.1

 CHANGELOG :
    v1.1.0 - 2022-01-14t13:54
        converting to `dict`

    v1.0.1 - 2022-01-14t13:15
        added documentation

    v1.0.0 - 2022-01-14t12:53
        abstracted from `pptx2json.py`
        opening each file

    v0.1.0 - 2021-12-31t02:53
        pptx2json.py :
            loop through filenames

    v0.0.0 - 2021-12-31t01:58
        pptx2json.py :
            hello world implementation
 '''

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
        json = a_dict
        # print the result
        print(json)
    # next filename in filenames
# end def jsoneach(filenames, openfunc)
