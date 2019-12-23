class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        jobs=set(tasks)
        task=[]
        for i in jobs:
            task.append((tasks.count(i),i))
        task=sorted(task,reverse=True)

        interval=0
        ans=""
        counter=-1
        while(task[0][0]!=0):
            for i in range(len(task)):
                if task[i][0]>0 and counter<n:
                    task[i]=task[i][0]-1,task[i][1]
                    counter+=1
                    interval+=1
                    ans+=task[i][1]
            ans+="I"*(n-counter)
            interval+=n-counter
            counter=-1
        print(ans.strip('I'))
        return len(ans.strip('I'))

s=Solution()
print(s.leastInterval(["A","A","A","A","B","B","B","c","c","c",'D','D','D','D','D','E','E','E','E','E','E'],3))