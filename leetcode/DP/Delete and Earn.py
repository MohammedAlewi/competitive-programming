#🔥
import collections
class Solution:
    def deleteAndEarn(self, nums) -> int:
        ans={}
        children= self.get_childs(nums)
        for i in range(len(nums)):
            if nums[i] in ans:
                continue
            ans[nums[i]]=self.do_bfs(children,i,nums)
        maximum=max(ans.values())
        return maximum

    def do_bfs(self,children,node,nums):
        answer=0
        visited=set()
        queue=collections.deque()

        visited.add(node)
        queue.append(node)
        while len(queue):
            node=queue.popleft()
            answer+=nums[node]
            for index in children[node]:
                if index not in visited:
                    queue.append(index)
                    visited.add(index)
        return answer

    def get_childs(self,nums):
        chidrens={}
        for index in range(len(nums)):
            if index-1 in chidrens and nums[index-1]== nums[index]:
                chidrens[index]=chidrens[index-1]
                continue
            chidrens[index]=set()
            for child_index in range(len(nums)):
                if abs(nums[child_index] - nums[index])!=1:
                    chidrens[index].add(child_index)

        return chidrens


# s=Solution()
# ans=s.deleteAndEarn([2,3,4])
# print(ans)