# merge sorted lists 

# given 2 sorted lists of integers A and B,
# with A having as many open slots as there are items 
# in B, return A containing the combined sorted list of valid items 
# from A and B


# A = [1,4,5,9,None, None, None]
# B = [2,6,7]

# Result: 
# A = [1,2,4,5,6,7,9]


# Ot(valid elements in A + len valid elements in B)
# Os(valid elements in A + len valid elements in B)
def merge(A,B):
    if not A:
        A = []
        return A 
    elif not B:
        return A 
    
    i = j = k = 0   
    retA = ['']*(len(A))
    while i < (len(A) - len(B)) and j < len(B):
        if A[i] < B[j]:
            retA[k] = A[i]
            i += 1
        elif A[i] >= B[j]:
            retA[k] = B[j]
            j += 1
        k += 1

    while i < (len(A) - len(B)):
        retA[k] = A[i]
        i += 1
        k += 1
    while j < len(B): 
        retA[k] = B[j]
        j +=1
        k += 1
    
    A = retA
    return A


# Ot(valid elements in A + len valid elements in B)
# Os(1)
def merge_in_place_mine(A, B):
    if not A:
        A = []
        return A 
    elif not B:
        return A 
    
    i = 0
    while i < (len(A) - len(B)):
        if A[i] >= B[0]:
            A[i], B[0] = B[0], A[i]
        i += 1

    j = 1
    while j < len(B):
        if B[0] < B[j]:
            A[i] = B[0]
            B[0] = float('inf')
        else:
            A[i] = B[j]
            j += 1
        i += 1
        
    if B[0] < float('inf'):
        A[i] = B[0]
    return A

# better solution (easier to read code) by Blake Adkins 
# moving pointers from right to left
def mergeLists(A, B):
  if len(B) == 0:
    return A
  if A[0] is None:
    return B
  if not A:
    return []
  
  insertionPtr = len(A) - 1
  pA = 0
  pB = len(B) - 1
  for i in range(len(A)):
    if A[i] is not None:
      pA = i
    else:
      break
      
  while pB >= 0:
    if A[pA] < B[pB]:
      A[insertionPtr] = B[pB]
      pB -= 1
    else:
      A[insertionPtr] = A[pA]
      pA -= 1
    insertionPtr -= 1
    
  return A

# Ot((valid elements in A + len valid elements in B)^2)
# Os(1)
def merge_in_place_traditional(A, B):
    if not A:
        A = []
        return A 
    elif not B:
        return A 

    a = 0
    b = len(A)-len(B)   
    # slot B into end of A
    A[b:] = B

    while a < b and b < len(A):
        if A[a] < A[b]:
            a += 1 
        else:
            index = b
            temp = A[b]
            # move over by 1
            while index >= a:
                A[index] = A[index-1]
                index -= 1
            # 
            A[a] = temp
            b += 1 
        #
    return A


def testing():
    # ex1 
    A = [1,4,5,9,None, None, None]
    B = [2,6,7]
    print(merge(A,B) == [1,2,4,5,6,7,9])
    A = [1,4,5,9,None, None, None]
    B = [2,6,7]
    print(merge_in_place_mine(A,B) == [1,2,4,5,6,7,9])
    A = [1,4,5,9,None, None, None]
    B = [2,6,7]
    print(merge_in_place_traditional(A,B) == [1,2,4,5,6,7,9])

    # # ex2 
    A = []
    B = []
    print(merge(A,B) == [])
    A = []
    B = []
    print(merge_in_place_mine(A,B) == [])
    A = []
    B = []
    print(merge_in_place_traditional(A,B) == [])

    # # ex3 
    A = [None, None]
    B = [1,2]
    print(merge(A,B) == [1,2])
    A = [None, None]
    B = [1,2]
    print(merge_in_place_mine(A,B) == [1,2])
    A = [None, None]
    B = [1,2]
    print(merge_in_place_traditional(A,B) == [1,2])

    # # ex4 
    A = [1,2]
    B = []
    print(merge(A,B) == [1,2])
    A = [1,2]
    B = []
    print(merge_in_place_mine(A,B) == [1,2])
    A = [1,2]
    B = []
    print(merge_in_place_traditional(A,B) == [1,2])

testing()