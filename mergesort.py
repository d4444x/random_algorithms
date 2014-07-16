

'''
Mergesort implemented recursively
doesnt sort in place : ' (
'''
def mergesort(ls):
    a = 0
    b = len(ls)
    if b<2:
        return ls
    left =  mergesort(ls[a:(b-a)//2])
    right = mergesort(ls[(b-a)//2:b])
    return merge(left,right)

def merge(left,right):
    res = []
    while(len(left)!=0 and len(right)!=0):
        if(left[0]>right[0]):
            res += [right.pop(0)]
            continue
        res += [left.pop(0)]
    if len(left)!=0:
        res+=left
    if len(right)!=0:
        res+=right
    return res

def sort(ls):
    return mergesort(ls)

