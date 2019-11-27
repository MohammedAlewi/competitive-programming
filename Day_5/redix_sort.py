def radix_sort(unsorted_list,max_num):
    max_num=0
    i=0
    final_list=[]
    for i in unsorted_list: 
        if max_num>i: max_num=i;
    while(max_num//i>0):
        i=i*10
        small=0;
        sorted_list=[0]*(max_num+1)
        final_list=[]
        for i in unsorted_list: sorted_list[i]+=1
        for i in range(len(sorted_list)):
            for j in range(0,sorted_list[i]):
                final_list.append(i)

    
    return final_list


def main():
    unsorted_list=[9,2,3,6,2,1]
    print( radix_sort(unsorted_list,9))

if __name__=='__main__':main()
    