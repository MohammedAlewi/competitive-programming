def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_num=i
        for j in range(i+1,len(unsorted_list)):
            if(unsorted_list[min_num]>unsorted_list[j]): min_num=j;
        buffer=unsorted_list[i]
        unsorted_list[i]=unsorted_list[min_num]
        unsorted_list[min_num]=buffer
    return unsorted_list

def main():
    input1=input("enter numbers separated by comma >>")
    unsorted_list=input1.split(',')
    print( selection_sort(unsorted_list))

if __name__=='__main__':main()