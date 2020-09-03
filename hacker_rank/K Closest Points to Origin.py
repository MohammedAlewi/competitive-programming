import heapq
import math

def k_closest_point(points,k):
    heap=[]

    for index in range(len(points)):
        point=points[index]
        distance= math.sqrt((point[0]*point[0] + point[1]*point[1])) 
        heapq.heappush(heap,(distance,index))

    result=[]
    for i in range(k):
        point= heapq.heappop(heap)
        result.append(points[point[1]])

    return result

print(k_closest_point([[1,3],[-2,2]],1))