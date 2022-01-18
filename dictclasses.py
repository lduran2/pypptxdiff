r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/dictclasses.py
 Facilities for classes that can be converted to dictionaries for data
 classes.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-18t00:12
 Version   : 1.7.2-alpha
 '''

from collections import OrderedDict # to preserve order

JSON_STRINGS = ( str, bytes )
# primitive types in valid JSON
JSON_NUMBERS = ( int, float, bool )
# represent JSON arrays
JSON_ARRAYS = ( list, tuple )
# represent JSON objects
JSON_OBJECTS = ( dict, )

def asdict(obj, ancestors=[], tracename=""):
    r'''
     Converts an `obj`ect to a dictionary.
     @param obj : object = to convert
     @minver 0.0.0
     @return a dictionary representation of the given object
     '''
    # BASE CASE:
    # if this object is its own ancestor, return a string copy
    print(tracename)
    try:
        if (obj in ancestors):
            return str(obj)
        # end if (obj in ancestors)
    # end try (obj in ancestors)
    # if there was an error searching
    except KeyError:
        # return the string copy
        return str(obj)
    # end except KeyError

    # record in ancestors
    ancestors += [obj]

    # if `null`, then return `None`
    if (obj is None):
        return None
    # end if (not(obj))

    # if a string, make sure it's stringified
    if (isinstance(obj, JSON_STRINGS)):
        return str(obj)
    # end if (isinstance(obj, JSON_STRINGS))

    # if a number, return it
    if (isinstance(obj, JSON_NUMBERS)):
        return obj
    # end if (isinstance(obj, JSON_NUMBERS))

    # INDUCTIVE STEP:

    # if has iterable items:
    if (hasattr(obj, r'items')):
        items = obj.items()
        if (hasattr(items, r'__iter__')):
            # convert each value
            # stringify each key
            converted = {
                str(key): asdict(value, ancestors,
                                 tracename + '[' + str(key) + ']')
                for (key, value) in items
            }
            # no need to preserve order, json.dumps sorts
            # return the result
            return converted
        # end if (hasattr(obj.items, r'__iter__'))
    # end if (hasattr(obj, r'items')))

    # if is iterable:
    if (hasattr(obj, r'__iter__')):
        # convert each element
        return [
            asdict(elem, ancestors, tracename + '[' + str(index) + ']')
            for index, elem in enumerate(obj)
        ]
    # end if (isinstance(obj, JSON_ARRAYS))

    # otherwise, if a Python object:
    try:
        # get the names of the attributes of the object
        obj_attr_names = dir(obj)
    # if type error, then obj does not support __dict__,
    # thus dir either:
    except TypeError:
        # so return the object itself
        return None
    # end except TypeError

    # get the public fields of the object
    obj_fields = {
        name: attr
        # generating attribute names and values
        for (name, attr) in (
            (name, getattr(obj, name))
            # looping through attribute names
            for name in obj_attr_names
            if (
                # keeping only attributes that exist
                typesafe_hasattr(obj, name)
                # and are public
                and not(name.startswith(r'_'))
            ) # end if
        ) # end (name, attr) in
        # keep only attributes that are not functions
        if (not(callable(attr)))
    } # end obj_fields
    # recursively process the dictionary
    return asdict(obj_fields, ancestors, tracename)
    # end except TypeError
# end def asdict(obj)

def typesafe_hasattr(obj, name):
    r'''
     Checks whether the `name` is an attribute of the `obj`ect,
     returning false on a `TypeError`.
     @param obj : object = to check for the attribute
     @param name : str = name of the attribute for which to check `obj`
     @return `True` if the `name` is an attribute of the `obj`ect and
        checking does not cause a TypeError; `False` otherwise.
     '''
    found = False
    # try checking the attribute
    try:
        found = hasattr(obj, name)
    # end try hasattr(obj, name)
    except TypeError:
        pass
    except ValueError:
        pass
    return found
# end def typesafe_hasattr(obj, name)

# # References
# 1: [@Santhosh]. (2019). python : object.__dict__ not showing all
#   attributes. Retrieved from <https://stackoverflow.com/q/57576522>
# 2: [@Eric Wilson]. (2014). How to list all fields of a class (and no
#   methods)?. Retrieved from <https://stackoverflow.com/q/21945067>
