import sys

def solution(A):
  """Your solution goes here."""
  values=sum(A)
  target=values//2
  ans=0
  for i in range(len(A)):
    val=do_dfs(A,target,i,set())
    if abs(ans-target)>abs(val-target):
      ans=val
      
  return abs(values-2*ans)
  

  
def do_dfs(A,target,index,used):
    sum_val=0
    used.add(index)
    for i in range(len(A)):
      if i in used:
        continue
      val=do_dfs(A,target-A[index],i,used)
      
      if abs(target-val-A[index]) < abs(target-sum_val-A[index]):
        sum_val=val
    
    used.remove(index)
    return sum_val+A[index]

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
