def insertion_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(i):
            if(unsorted_list[j]>unsorted_list[i]):
                buffer=unsorted_list[j]
                unsorted_list[j]=unsorted_list[i]
                unsorted_list[i]=buffer
    return unsorted_list

def main():
    input1=input("enter numbers separated by comma >>")
    unsorted_list=input1.split(',')
    print( insertion_sort(unsorted_list))

if __name__=='__main__':main()