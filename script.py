import sys
import json

# Returns a flattened JSON object
# Params:
#   - jObject: dictionary
#   - key: string, used to construct key when the JSON object is nested. Default: empty string
def flatten(jObject, key = ""):

    flattened = {}

    # iterate over every key value pair in the object
    for i in jObject:
        
        # if value stored at i is a dict (i.e. it's a nested JSON object)
        if isinstance(jObject[i], dict):

            # recursive call to flatten and then append the result to the object currently being built
            flattened = flattened | flatten(jObject[i], i)
        
        # else if it's a simple key - value pair
        else:

            # build the key for this value
            if key: instanceKey = key + "." + i
            else: instanceKey = i

            # append key-value pair to 
            flattened[instanceKey] = jObject[i]

    return flattened


# this function transforms True to true
# Take input using stdin
files = sys.argv[1:]
for f in range(len(sys.argv[1:])):
    print(f)
    with open(files[f]) as user_file:
        file_contents = user_file.read()
    
    loaded = json.loads(file_contents)
    print(flatten(loaded))