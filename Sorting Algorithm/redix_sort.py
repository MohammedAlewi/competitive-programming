def counting_sort(arr,max_num):
    output = [0] *max_num
    count = [0] *max_num
    ans = ["" for _ in arr]  
    for i in arr: 
        count[i] += 1
    for i in range(max_num): 
        count[i] += count[i-1] 
    for i in range(len(arr)): 
        output[count[arr[i]]-1] = arr[i] 
        count[arr[i]] -= 1
    return output  

# def get_digit(num,digit):
#     val=str(num)
#     if(len(val)<=digit): return 0
#     return int(val[len(val)-1-digit])

# def radix_sort(uncount,max_num):
#     digit=len(str(max_num))
#     for i in range(digit): 
#         uncount=counting_sort(uncount,max_num)
    
#     return final_list


def main():
    uncount=[3,6,4,1,3,4,1,9,4]
    print( counting_sort(uncount,9))

if __name__=='__main__':main()
    



# class Solution:
# def reorganizeString(self, S: str) -> str:
#     val2=""
#     d=dict()
#     for i in S:
#         if(d.get(i)==None):d[i]=1
#         else:d[i]+=1
#     val=list(d.values())
#     val.sort()
#     if(val[-1]*2-sum(val)>=2):return ""
#     while(sum(list(d.values()))!=0):
#         for key in d:
#             if(d[key]>0):val2+=key; d[key]-=1
#     return val2