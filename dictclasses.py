r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/dictclasses.py
 Facilities for classes that can be converted to dictionaries for data
 classes.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-15t22:57
 Version   : 1.5.3-alpha
 '''

from collections import OrderedDict # to preserve order
from inspect import ismethod

# primitive types in valid JSON
JSON_PRIMITIVES = ( str, int, bytes, float, bool )
# represent JSON arrays
JSON_ARRAYS = ( list, tuple )
# represent JSON objects
JSON_OBJECTS = ( dict, )

def asdict(obj, visited=[]):
    r'''
     Converts an object to a dictionary.
     @param obj : object = to convert
     @minver 0.0.0
     @return a dictionary representation of the given object
     '''
    # BASE CASE:
    try:
        if (obj in visited):
            return None
    except KeyError:
        return None

    # if `null`, then return `None`
    if (obj is None):
        return None
    # if (not(obj))

    # if a primitive, return it
    if (isinstance(obj, JSON_PRIMITIVES)):
        return obj
    # end if (isinstance(obj, JSON_PRIMITIVES))

    # INDUCTIVE STEP:

    # record visited
    visited.append(obj)

    # if an array, convert each element
    if (isinstance(obj, JSON_ARRAYS)):
        return [ asdict(elem, visited) for elem in obj ]
    # end if (isinstance(obj, JSON_ARRAYS))

    # if a JSON object:
    if (isinstance(obj, JSON_OBJECTS)):
        # convert each value
        # stringify each key
        converted = { str(key): asdict(value, visited)
                      for (key, value) in obj.items()  }
        # preserves order of insertion
        ordered = OrderedDict(converted)
        # return the result
        return ordered
    # end if (isinstance(obj, JSON_OBJECTS))

    # otherwise, if a Python object:
    
    # if a Python object:
    try:
        # get the names of the attributes of the object
        obj_attr_names = dir(obj)
    # if type error, then obj does not support __dict__,
    # thus dir either:
    except TypeError:
        # so return the object itself
        return None
    # get the public fields of the object
    obj_fields = { name: attr
                   for (name, attr) in
                   ( (name, getattr(obj, name))
                     for name in obj_attr_names
                     if (
                        # double checking attributes
                        hasattr(obj, name)
                        # ignoring private attributes
                        and not(name.startswith(r'_'))
                     )
                   )
                   # and ignoring function
                   if (not(callable(attr)))
                 }
    # recursively process the dictionary
    return asdict(obj_fields, visited)
    # end except TypeError
# end def asdict(obj)
