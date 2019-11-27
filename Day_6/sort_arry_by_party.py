def party(list_val):
    odd_list=[i  for i in list_val if i%2!=0]
    even_list=[i  for i in list_val if i%2==0]
    index=0
    while(len(list_val)>index):
        list_val[index]=even_list.pop()
        index+=1
        list_val[index]=odd_list.pop()
        index+=1
    return list_val;

def main():
    unsorted_list=[1,3,2,4]
    print( party(unsorted_list))

if __name__=='__main__':main()



            