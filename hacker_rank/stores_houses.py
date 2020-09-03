def closest_stores(stores,houses):
    stores.sort()

    result=[]

    for house in houses:
        result.append(closest_one(house,stores))
    return result

def closest_one(house,stores):
    start,end=0,len(stores)-1

    while start<end:
        mid = (start+end)//2
        if start==mid:
            if abs(house-stores[start])<=abs(house-stores[end]):
                return stores[start]
            return stores[end]
        if stores[mid] < house:
            start=mid
        elif stores[mid]>house:
            end=mid-1
        elif stores[mid]==house: 
            return house

    return stores[start]
            
stores=[5, 3, 1, 2, 6]
houses=[4, 8, 1, 1]
print(closest_stores(stores,houses))