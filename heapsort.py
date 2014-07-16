def add_to_heap(h, e):
    length = len(h)
    if length==0:
        return [e]
    h.append(e)
    index = length
    while True:
        if index == 0:
            return h
        parent = (index-2+index%2*1)/2
        if h[parent]<h[index]:
            temp = h[index]
            h[index] = h[parent]
            h[parent] = temp
            index = parent
            continue
        return h

def pop_off_heap(h):
    if len(h)==1:
        return [], h[0]
    if len(h)==0:
        return [],None
    e = h.pop()
    our_ret = h[0]
    h[0] = e
    index = 0
    length = len(h)
    while True:
        left = index*2+1
        right = left+1
        left_valid = left>=length
        right_valid = right>=length
        if left_valid and right_valid:
            return h,our_ret
        if  (right_valid or h[left]>=h[right]) and h[index]<h[left]:
            temp = h[index]
            h[index] = h[left]
            h[left] = temp
            index = left
            continue
        if not right_valid and h[index]<h[right]:
            temp = h[index]
            h[index] = h[right]
            h[right] = temp
            index = right
            continue
        return h,our_ret

def heapsort(l):
    heap = []
    for i in range(len(l)):
        heap = add_to_heap(heap,l.pop())
    ret = []
    print heap
    for i in range(len(heap)):
        heap, e = pop_off_heap(heap)
        ret.append(e)
    return ret
        
