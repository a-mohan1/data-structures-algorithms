import numpy as np

# Binary search
# Return index of value, or return -1 if value is not found
def bin_search(val, arr):
    n = len(arr)
    if n==0: 
        return -1
    elif n==1 & arr[n-1]!=val:
        return -1
    elif n==1 & arr[n-1]==val:
        return 0
    else:
        mid = int(n/2)
        if val==arr[mid]:
            return mid
        elif val<arr[mid]:
            return bin_search(val, arr[:mid])
        else:
            return bin_search(val, arr[mid+1:])

# Interpolation search
def interp_search(arr, value):
    n = len(arr)
    lo = 0
    hi = n-1
    
    found = False
    while not found and hi>=lo:
        mid = int(lo + (hi-lo)/(arr[hi] - arr[lo])*(value-arr[lo]) )
        if value==arr[mid]:
            found = True
        elif value < arr[mid]:
            hi = mid
        else:
            lo = mid+1
    if found:
        return mid
    else:
        return -1
                
# Merge sort
def merge_sort(arr):
    n = len(arr)
    if n<=1:
        return arr
    else:
        mid = int(n/2)
        sorted_left = merge_sort(arr[:mid])
        sorted_right = merge_sort(arr[mid:])
        sorted_arr = merge_sorted_arrs(sorted_left, sorted_right)
        return sorted_arr
    
def merge_sorted_arrs(left_arr, right_arr):
    idx_l = 0
    idx_r = 0
    nl = len(left_arr)
    nr = len(right_arr)
    merged_arr = [0]*(nl+nr)
    idx_m = 0
    while idx_l < nl and idx_r < nr:
        if left_arr[idx_l] <= right_arr[idx_r]:
            merged_arr[idx_m] = left_arr[idx_l]
            idx_m += 1
            idx_l += 1
        else:
            merged_arr[idx_m] = right_arr[idx_r]
            idx_m += 1
            idx_r += 1
    while idx_l < nl:
        merged_arr[idx_m] = left_arr[idx_l]
        idx_l += 1
        idx_m += 1
    while idx_r < nr:
        merged_arr[idx_m] = right_arr[idx_r]
        idx_r += 1
        idx_m += 1
    return merged_arr

# Quicksort
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo-1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1

def quicksort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr)-1
    if lo<hi:
        pivot_idx = partition(arr, lo, hi)
        quicksort(arr, lo, pivot_idx-1)
        quicksort(arr, pivot_idx+1, hi)

# Heap sort
# For node i as root node, node 2i+1 is left node and node 2i+2 is right node
# Max heap
def heapify(heap, n, i):
    maxnode = i
    leftnode = 2*i+1
    rightnode = 2*i+2
    if leftnode < n and heap[i] < heap[leftnode]:
        maxnode = leftnode
    if rightnode < n and heap[maxnode] < heap[rightnode]:
        maxnode = rightnode
    if maxnode != i:
        heap[i], heap[maxnode] = heap[maxnode], heap[i]
        # Need to sort only the subtree which is modified
        heapify(heap, n, maxnode)

def heapsort(heap):
    n = len(heap)
    # Heapify starting from leaves, so that, for each node, its left and right subtrees will be sorted first
    for i in range(n, -1, -1):
        heapify(heap, n, i)
    # Move root (max value) to end of array and heapify the rest of the array
    for i in range(n-1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        # Heapify the rest of the heap 
        heapify(heap, i, 0)

    return heap

# Bubble sort
def bubblesort(arr):
    n = len(arr)
    not_srted = True
    while not_srted:
        swaps = 0
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
        if swaps==0:
            not_srted=False

# Insertion sort
def insert_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in np.arange(i,-1,-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
# Selection sort
def sel_sort(arr):
    s = []
    n = len(arr)
    if n==1:
        s.extend(arr)
    else:
        min_el = min(arr)
        s.append(min_el)
        arr.remove(min_el)
        s.extend(sel_sort(arr))        
    return s

if __name__=="__main__":
    heap = [np.random.randint(100) for _ in range(10)]
    print(heap)
    print("Sorted by heap sort: ", heapsort(heap))
    quicksort(heap)
    print("Sorted by quicksort", heap)
