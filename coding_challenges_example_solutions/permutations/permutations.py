"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
exp =  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
exp =  [[0,1],[1,0]]

Example 3:
Input: nums = [1]
exp =  [[1]]

"""

import time

# number of resulting permutations is n! if all n are different

# Os(n!) given that I need to track all permutions
# Ot(n!), whcih can be seen when looking at the stack solution
def permute_rec(nums):
    # 
    def perm_remains(prefix, remains, res):
        # if no more to permute, append combo
        if len(remains) == 0:
            # if not found already due to duplicate elements
            if not prefix in res:
                res.append(prefix)
                return res
        else:
            for i in range(0, len(remains)):
                # take out i element and append to prefix
                num = remains[i]
                # take i elemment out from remains
                remainsNew = remains[:i]+remains[i+1:]
                res = perm_remains(prefix+[num], remainsNew, res)
        return res
    #
    return perm_remains([], nums, [])




#### using stack and pickle

# Os(n!) 
# Ot(n!) 
# e.g. if nums = [1,2,3], then the 1st 
# for loop loops over 3 items and produced 3 stack entries each 2 items long
# hence, the second for loop runs 3 times and each time 
# loops over 2 items and, after appending the single items that are left, 
# produces 6 premutations
# 
# Hence, 3 * 2 * (1)  = 6 = 3!


import pickle

def make_permuted_stack(nums):
  if len(nums) == 1:
      return [nums]
  res = []
  S = [([],nums)]
  while S:
    prefix, remainder = S.pop()
    for i in range(0,len(remainder)):
        prefixN = pickle.loads(pickle.dumps(prefix))
        prefixN.append(remainder[i])
        remainderN = remainder[:i]+remainder[i+1:]
        if len(remainderN) == 1:
            prefixN = prefixN+remainderN
            if not prefixN in res:
                res.append(prefixN) 
        else:
            S.append((prefixN, remainderN))
  return res





def testing():
    # Example 1:
    nums = [1,2,3]
    exp =  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permute_rec(nums) == exp) 
    print(sorted(make_permuted_stack(nums)) == exp) 

    # Example 2:
    nums = [0,1]
    exp =  [[0,1],[1,0]]
    print(permute_rec(nums) == exp) 
    print(sorted(make_permuted_stack(nums)) == exp) 

    # Example 3:
    nums = [1]
    exp =  [[1]]
    print(permute_rec(nums) == exp) 
    print(sorted(make_permuted_stack(nums)) == exp) 

    # Example 4:
    nums = [1,1,3,4]
    exp =  [[1, 1, 3, 4], [1, 1, 4, 3], [1, 3, 1, 4], [1, 3, 4, 1], 
        [1, 4, 1, 3], [1, 4, 3, 1], [3, 1, 1, 4], [3, 1, 4, 1], 
        [3, 4, 1, 1], [4, 1, 1, 3], [4, 1, 3, 1], [4, 3, 1, 1]]
    print(permute_rec(nums) == exp) 
    print(sorted(make_permuted_stack(nums)) == exp) 

testing()

