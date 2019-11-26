def quick_sort(unstorted):
    if len(unstorted)<2:
        return unstorted
    index=unstorted.pop()
    list1=[]
    list2=[]
    for i in unstorted: 
        if(index>i):list1.append(i)
        elif(index<=i):list2.append(i)
    return quick_sort(list1) +[index] +quick_sort(list2)

def main():
    input1=input("enter numbers separated by comma >>")
    unsorted_list=input1.split(',')
    print( quick_sort(unsorted_list))

if __name__=='__main__':main()
    