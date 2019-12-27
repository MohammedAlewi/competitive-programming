def counting_sort(arr, max_value, get_index):
  counts = [0] * max_value

  for a in arr:s
    counts[get_index(a)] += 1
  
  for i, c in enumerate(counts):
    if i == 0:
      continue
    else:
      counts[i] += counts[i-1]

  for i, c in enumerate(counts[:-1]):
    if i == 0:
      counts[i] = 0
    counts[i+1] = c

  ret = [None] * len(arr)

  for a in arr:
    index = counts[get_index(a)]
    ret[index] = a
    counts[get_index(a)] += 1
  
  return ret


def get_digit(n, d):
  for i in range(d-1):
    n //= 10
  return n % 10

def get_num_difit(n):
  i = 0
  while n > 0:
    n //= 10
    i += 1
  return i

def radix_sort(arr, max_value):
  num_digits = get_num_difit(max_value)
  for d in range(num_digits):
    arr = counting_sort(arr, max_value, lambda a: get_digit(a, d+1))
  return arr