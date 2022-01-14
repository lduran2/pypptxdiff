r'''
 Canonical : https://github.com/lduran2/pypptxdiff/blob/master/dictclasses.py
 Facilities for classes that can be converted to dictionaries for data
 classes.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2022-01-14t13:50
 Version   : 1.0.0

 CHANGELOG :
    v0.0.0 - 2022-01-14t14:05
        shallow copy implementation

    v0.0.0 - 2022-01-14t13:50
        stub implementation
 '''

def asdict(obj):
    r'''
     Converts an object to a dictionary
     @param obj : object = to convert
     @minver 0.0.0
     @return a dictionary representation of the given object
     '''
    # initialize to the dictionary of the object
    result = obj.__dict__
    return result
# end def asdict(obj)
