r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/dictclasses.py
 Facilities for classes that can be converted to dictionaries for data
 classes.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-14t15:02
 Version   : 1.5.1
 '''

from collections import OrderedDict # to preserve order

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
    # BASE CASE:

    # if a primitive, return it
    if (isinstance(obj, JSON_PRIMITIVES)):
        return obj
    # end if (isinstance(obj, JSON_PRIMITIVES))

    # if an array, convert each element
    if (isinstance(obj, JSON_ARRAYS)):
        return [ asdict(elem) for elem in obj ]
    # end if (isinstance(obj, JSON_ARRAYS))

    # if a JSON object:
    if (isinstance(obj, JSON_OBJECTS)):
        # convert each value
        converted = { key: asdict(value)
                      for (key, value) in obj.items() }
        # preserves order of insertion
        ordered = OrderedDict(converted)
        # return the result
        return ordered
    # end if (isinstance(obj, JSON_OBJECTS))

    # INDUCTIVE STEP:
    # if a Python object:
    try:
        # process the dictionary of the object
        return asdict(obj.__dict__)
    # end try obj.__dict__
    # if type error, then obj does not support __dict__:
    except TypeError:
        # so return the object itself
        return obj
    # end except TypeError
# end def asdict(obj)
