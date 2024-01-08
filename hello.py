
import json
import sys

def initial():
    try:
        # some JSON:
        x = '{ "name":"John", "age":30, "city":"New York"}'
        
        # parse x:
        y = json.loads(x)
        # return x
        
        # the result is a Python dictionary:
        print(y["name"])
        print(y["number"])
        print(y["age"])
        print("End of function initial")
    except Exception as e:
        print("Exception in initial", e)
        return e
        sys.exit(1)
