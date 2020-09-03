import sys

def solution(A):
  row_count=0
  
  values=set()
  vals=[]
  for index in range(len(A)):
    if index not in values:
      val=do_dfs(A,index,values)
      vals.append(val)
      values=values.union(set(val))
      row_count+=1
  return row_count

def do_dfs(A,index,values):
  path=[]
  
  for i in range(index+1,len(A)):
    if i in values:
      continue
    
    if A[index]>A[i]:
      
      paths=do_dfs(A,i,values)
      
      if len(path)<len(paths):
        path=paths
        
  path.append(index)
  
  return path
    

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
