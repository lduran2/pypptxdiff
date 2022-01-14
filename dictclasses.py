r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/dictclasses.py
 Facilities for classes that can be converted to dictionaries for data
 classes.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-14t14:43
 Version   : 1.3.1
 '''

# primitive types in valid JSON
JSON_PRIMITIVES = ( int, float, str )
# represent JSON arrays
JSON_ARRAYS = ( list, tuple )
# represent JSON objects
JSON_OBJECTS = ( dict, )

def asdict(obj):
    r'''
     Converts an object to a dictionary.
     @param obj : object = to convert
     @minver 0.0.0
     @return a dictionary representation of the given object
     '''
    # if a primitive, return it
    if (isinstance(obj, JSON_PRIMITIVES)):
        return obj
    # end if (isinstance(obj, JSON_PRIMITIVES))

    # if an array, convert each member
    if (isinstance(obj, JSON_ARRAYS)):
        return [ asdict(elem) for elem in obj ]
    # end if (isinstance(obj, JSON_ARRAYS))

    # initialize to the dictionary of the object
    result = obj.__dict__
    # replace each object with a 
    return result
# end def asdict(obj)
