def q2(arr1,arr2):
    final=[]
    for i in arr2:
        while(arr1.count(i)>0):
            arr1.remove(i)
            final.append(i)
    arr1.sort()
    return final+arr1


def main():
    unsorted_list=[1,3,2,4,4,4,6,3,2,1,7]
    arr2=[1,3,4]
    print( q2(unsorted_list,arr2))

if __name__=='__main__':main()

           