from collections import defaultdict
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    occurance = defaultdict(lambda:0)

    for str_val in strings:
        occurance[ str_val ] += 1

    result = []

    for key in queries:
        result.append( occurance[ key ] )

    return result