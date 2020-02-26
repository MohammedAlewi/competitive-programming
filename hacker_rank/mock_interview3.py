# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         marked=set() #contains the marked nodes
#         temp_node=head
#         while temp_node:
#             if temp_node.val in marked:
#                 return False
#             marked.add(temp_node.val)
#             temp_node=temp_node.next
#         return True


# for i,num in enumerate([5,4,3,20]):
#     print(i,num)


# from collections import defaultdict

# values=[5,3,45,3,4343,5,34,6,34,34]


# accessor=defaultdict(int)


# for _,num in enumerate(values):
#     accessor[num]+=1

# print(accessor)







# from collections import Counter


# c=Counter(values)
# print(c)



# import string

# print(string.hexdigits)




# from itertools import product, permutations, combinations

# print(list(product("ab","cd")))
# print(list(product(["ab","ad"],["cd","ds"])))

# print(list(combinations(['a','b',3],2)))

# import math
# print(math.inf)