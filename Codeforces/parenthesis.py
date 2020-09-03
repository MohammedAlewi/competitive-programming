from functools import lru_cache

@lru_cache(maxsize=None)
def number(n):
    if n<1:
        return ['']
    if n==1:
        return ['()']
    else:
        result=set()
        values= number(n-1)
        for val in values:
            result.add('('+val+')')
            for v in range(len(val)+1):
                result.add(val[:v]+'()'+val[v:])
        return list(result)

print(number(8))

# number(13)