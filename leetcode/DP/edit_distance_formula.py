def edit_str(s1,s2,n,m):
    if n<0 or m<0:
        return max(m,n)+1

    elif s1[n]==s2[m]:
        return edit_str(s1,s2,n-1,m-1)
    else:
        return min(edit_str(s1,s2,n-1,m-1),edit_str(s1,s2,n,m-1),edit_str(s1,s2,n-1,m)) +1


print(edit_str("kitten","sitting",5,6))