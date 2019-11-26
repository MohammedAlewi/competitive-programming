def radix_sort(unsorted_list,max_num):
    max_num=0
    i=0
    final_list=[]
    for i in unsorted_list: 
        if max_num>i: max_num=i;
    while(max_num//i>0):
        i=i*10
        small=0;
        for i in range(len(unsorted_list)):
            if(unsorted_list[i]//i<small//i):
                unsorted_list[i],unsorted_list[small]

    
    return final_list


def main():
    unsorted_list=[9,2,3,6,2,1]
    print( radix_sort(unsorted_list,9))

if __name__=='__main__':main()
    