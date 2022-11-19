import sys
import json

# Returns a flattened dict object
# Params:
#   - jObject: dictionary
#   - key: string, used to construct key when the JSON object is nested. Default: empty string
def flatten(jObject, key = ""):

    flattened = {}

    # iterate over every key value pair in the object
    for i in jObject:

        # build the key for this value by appending previous key to current key
        if key: instanceKey = key + "." + i
        else: instanceKey = i

        # if value stored at i is a dict (i.e. it's a nested JSON object)
        if isinstance(jObject[i], dict):

            # recursive call to flatten and then append the result to the object currently being built
            flattened = flattened | flatten(jObject[i], instanceKey)
        
        # if it's a simple key-value pair
        else:
            # append key-value pair to the object currently being built
            flattened[instanceKey] = jObject[i]

    return flattened


if __name__ == '__main__':
    files = sys.argv[1:]

    # for each JSON file to flatten
    for f in range(len(sys.argv[1:])):

        with open(files[f]) as user_file:
            file_contents = user_file.read()
        
        # load JSON
        loadedJSON = json.loads(file_contents)

        # flatten this object
        flattenedDict = flatten(loadedJSON)

        # parse path to file for output file name
        fileName = files[f].split("/")

        # output the flattened JSON object to the outputs folder as a .json file
        with open(f"./outputs/{fileName[-1]}", "w") as outfile:
            json.dump(flattenedDict, outfile)


# mention python version
# mention JSON conversion
# convert to JSON Object, not dict