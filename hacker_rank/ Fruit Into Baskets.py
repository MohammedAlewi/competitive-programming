def max_fruits(fruits):
    max_count=0

    type_1=None
    type_2=None

    curr_count=0

    for i in range(len(fruits)):
        if fruits[i]== type_1:
            curr_count+=1
        
        elif fruits[i]== type_2:
            curr_count+=1

        elif None == type_1:
            type_1=fruits[i]
            curr_count+=1

        elif None == type_2:
            type_2=fruits[i]
            curr_count+=1

        else:
            max_count=max(max_count,curr_count)
            type_1=fruits[i-1]
            type_2=fruits[i]
            curr_count=2

    max_count=max(max_count,curr_count)

    return max_count


print( max_fruits( [3,3,3,1,2,1,1,2,3,3,4] ) )