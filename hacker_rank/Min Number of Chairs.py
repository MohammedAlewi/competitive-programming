import heapq
def min_num_chairs(start,end):
    time_table=[]
    for i in range(len(start)):
        time_table.append((start[i],end[i]))

    time_table.sort()

    heap=[]
    max_chair=0
    index=0
    while index< len(time_table):
        time=time_table[index]
        if len(heap)==0:
            heapq.heappush(heap,(time[1],time[0]))
            max_chair=max(max_chair,len(heap))
            index+=1
        else:
            if heap[0][0]<=time[0]:
                heapq.heappop(heap)
            else:
                heapq.heappush(heap,(time[1],time[0]))
                max_chair=max(max_chair,len(heap))
                index+=1 
    return max_chair

print(min_num_chairs([1, 2, 6, 5, 3],[5, 5, 7, 6, 8]))
