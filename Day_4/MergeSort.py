def merge_sort(unsorted_list):
    if(len(unsorted_list)==2):
        if(unsorted_list[0]>unsorted_list[1]):
            unsorted_list[0],unsorted_list[1]=unsorted_list[1],unsorted_list[0]
        return unsorted_list
    list1=merge_sort(unsorted_list[0:len(unsorted_list)//2]);
    list2=merge_sort(unsorted_list[len(unsorted_list)//2:]);
    sorted=[]
    i,j=0,0;
    while(i<len(list1) and j<len(list2)):
        if(list1[i]>list2[j]):sorted.append(list2[j]); j+=1
        else:sorted.append(list1[i]); i+=1
    while(i<len(list1)): sorted.append(list1[i]) ;i+=1;
    while(j<len(list2)): sorted.append(list2[j]) ;j+=1;
    
    return sorted

def main():
    input1=input("enter numbers separated by comma >>")
    input1=input1.split(',')
    unsorted_list=[int(i) for i in input1]
    print( merge_sort(unsorted_list))
if __name__=='__main__':main()