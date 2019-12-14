def main(len,nums):
    length=int(len)
    nums=nums.split(" ")
    index=[]
    val=1
    flag=True
    for i in range(1,length):
        if nums[i-1]>nums[i] and flag:
            flag=False
            continue
        elif nums[i-1]>nums[i]: 
            index.append(val)
            flag=True
            val=1
            continue
        val+=1
    index.append(val)
    print(max(index))

def runner():
    length=input()
    nums=input()
    main(length,nums)

length=""
nums=""
main(length,nums)