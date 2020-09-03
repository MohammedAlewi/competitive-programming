def watering_flowers(plants,cap1,cap2):
    curr_1,curr_2=0,0
    count=0
    start,end=0,len(plants)-1

    while start<=end:
        if start==end:
            count= count+1 if curr_1+curr_2 < plants[start] else count
            break
        if curr_1 < plants[start]:
            curr_1=cap1
            count+=1
        if curr_2 < plants[end]:
            curr_2=cap2
            count+=1
        
        curr_1-=plants[start]
        curr_2-=plants[end]
        start+=1
        end-=1

    return count


print(watering_flowers([2,4,5,1,2],5,7))