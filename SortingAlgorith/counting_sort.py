def counting_sort(unsorted_list,max_num):
    sorted_list=[0]*(max_num+1)
    final_list=[]
    for i in unsorted_list: sorted_list[i]+=1
    for i in range(len(sorted_list)):
        for j in range(0,sorted_list[i]):
            final_list.append(i)
    return final_list


def main():
    unsorted_list=[9,2,3,6,2,1]
    print( counting_sort(unsorted_list,9))

if __name__=='__main__':main()
    