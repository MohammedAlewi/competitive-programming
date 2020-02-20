
/*
N friends go to a restaurant.
Each person orders the same food.
They get the total bill of S dollars.
Person i pays A_i dollars.
In order to settle among each other, people who paid less should transfer money to the people who paid more.
Find, all pairs of people where person_A should pay person_B, amount_AB.

Example
[5, 8, 17]  0->2 :5  1-> 2: 2
[(5,0)]= a1
[(2,2),(3,3)]= a2
[(-2,2),]
    
 0, 1  , 2
Output:
0 -> 2: 5 dollars
(0,2,5)
*/

sum=total_sum / 30
value= total_sum/lenth 10

d={}
for i in 0,arr.lenght:
  d[value-arr[i]]=i
  
# ans=[]
# for key in d:
#   if d[-1*key] exist:
#     tup=(d[key],d[-1*key],key)
#     ans.add(t)
    
def  get_values(arr):
  	total_sum=sum(arr)
    values=total_sum/len(arr)
    payers=[]
    getters=[]
    for i in range(len(arr)):
      current= values- arr[i]
      if current>0:
        payers.append((current,i))
      elif current<0:
        getters.append((current,i))
        
    return payers,getters
  
  
def do_matching(arr):
  	payers,getters=get_values(arr)
    i,j=0,0
    
    answer=[]
    while i <len(payers) and j < len(getters):
      c_p=payers[i]
      c_g=getters[j]
      tmp= c_p[0]-c_g[0]
      current_answer=(i,j,tmp)
      answer.append(current_answer)
      if tmp==0:
        i+=1
        j+=1
        
      elif tmp>0:
        j+=1
        payers[i]=(tmp,i)
        
      else:
        i+=1
        getters[j]=(tmp,j)
      
    return answer
    
    

  
