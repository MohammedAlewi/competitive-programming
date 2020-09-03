from collections import defaultdict
def getMostBooked(arr):
    freq=defaultdict(lambda: 0)
    for val in arr:
        if val[0]=='+':
            freq[val[1:]]+=1

    room=''
    count=0

    for val in freq.items():
        if val[1]>count:
            count=val[1]
            room=val[0]
        if val[1]==count and val[0]<room:
            room=val[0]

    return room


v=getMostBooked(["+1A", "+3E", "+4F", "-3E"])
print(v)