# # def calculate(str_val):
# #     chars=set()
# #     index=0
# #     build=""
# #     for i in str_val:
# #         if i not in chars and (index==0 or index==len(build)-1):
# #             if index==0:
# #                 build=i+build
# #                 index=0
# #             else:
# #                 build=build+i
# #                 index=len(build)-1
# #             chars.add(i)
# #         elif i in chars: 
# #             if build[max(0,index-1)]==i:
# #                 index=max(index-1,0)
# #             elif build[min(len(build)-1,index+1)]==i:
# #                 index=min(len(build)-1,index+1)
# #             elif build[index]!=i:
# #                 print("NO")
# #                 return
# #     print("YES")

# #     for i in range(97,123):
# #         if chr(i) not in chars:
# #             build+=chr(i)
# #             chars.add(i)

# #     print(build)



# def calculate(str_val):
#     values={}
#     for i in range(len(str_val)-1):
#         if values.get(i)==None:
#             values[str_val[i]]=set()
#         values[str_val[i]].add(str_val[max(i-1,0)])
#         values[str_val[i]].add(str_val[min(len(str_val)-1,i+1)])
#         if len(values[str_val[i]])>2:
#             print("NO")
#             return

#     if values.get(str_val[len(str_val)-1])==None:
#         values[str_val[len(str_val)-1]]=set()
#     values[str_val[len(str_val)-1]].add(str_val[len(str_val)-2])
    
#     min_len=2
#     min_key=""
#     for i in values.keys():
#         min_len=min(min_len,len(values[i]))
#         if 1==len(values[i]):
#             min_key=i


#     if min_len==2:
#         print("NO")
#         return

#     ans=[]
#     visited={}
#     do_visites(visited,ans,min_key,values)

#     build="".join(ans)
#     for i in range(97,123):
#         if chr(i) not in visited.keys():
#             build+=chr(i)

#     print("YES")
#     print(build)


# def do_visites(visited,values,node,childs):
#     values.append(node)
#     visited[node]=True
#     for i in childs[node]:
#         if i not in visited:
#             do_visites(visited,values,i,childs)
        





# # calculate("abcdefghijklmnopqrstuvwxyza")

# def runner():
#     val=input()
#     for i in range(int(val)):
#         ans=input()
#         calculate(ans)
# runner()





def calculate(str_val):
    chars=set()
    index=0
    build=""
    for i in str_val:
        if i not in chars:
            if index==0:
                build=i+build
                index=0
            elif index==len(build)-1:
                build=build+i
                index=len(build)-1
            else:
                print("NO")
                return 
            chars.add(i)
        else: 
            if build[max(0,index-1)]==i:
                index=max(index-1,0)
            elif build[min(len(build)-1,index+1)]==i:
                index=min(len(build)-1,index+1)
            else:
                print("NO")
                return
    print("YES")
 
    for i in range(97,123):
        if chr(i) not in chars:
            build+=chr(i)
            chars.add(i)
 
    print(build)
 
 
 
def runner():
    val=input()
    for i in range(int(val)):
        ans=input()
        calculate(ans)
runner()