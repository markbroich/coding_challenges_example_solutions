# Matching Pairs of Brackets

# write code to find the matching pairs in the list as per the matching brackets

# Input : test_list = [('(', 1), ('(', 2), (')', 3), (')', 4)]
# Output : [(2, 3), (1, 4)]
# Input : test_list = [('(', 1), (')', 4)]
# Output : [(1, 4)]

# test_list = [('(', 7), ('(', 9), (')', 10), (')', 11), ('(', 15), (')', 100)] 
  
# test_list = [('(', 7), ('(', 9), (')', 10), (')', 11), ('(', 15), (')', 100)]
# The paired elements : [(9, 10), (7, 11), (15, 100)]

test_list = [('(', 7), ('(', 9), (')', 10), (')', 11), ('(', 15), (')', 100)]
def find_matching_pairs(test_list):
    if not test_list:
        return -1
    stack = []
    result = []
    for tup in test_list:
        if tup[0] == '(':
            stack.append((tup[0],tup[1]))
        elif not stack:
            return -1
        else: 
            result.append((stack.pop()[1],tup[1]))
    if stack:
        return -1
    return result

def check(expected, output):
    if expected == output:
        return True
    else:
        return False

expected_1 = find_matching_pairs([('(', 1), ('(', 2), (')', 3), (')', 4)])
output_1 = [(2, 3), (1, 4)]
print(check(expected_1, output_1))

expected_2 = find_matching_pairs([('(', 1), (')', 4)])
output_2 = [(1, 4)]
print(check(expected_2, output_2))

expected_3 = find_matching_pairs([('(', 7), ('(', 9), (')', 10), (')', 11), ('(', 15), (')', 100)])
output_3 = [(9, 10), (7, 11), (15, 100)]
print(check(expected_1, output_1))

expected_4 = find_matching_pairs([])
output_4 = -1
print(check(expected_4, output_4))


expected_5 = find_matching_pairs([('(', 2), (')', 3), (')', 4)])
output_5 = -1
print(check(expected_5, output_5))

expected_6 = find_matching_pairs([('(', 99), ('(', 1), ('(', 2), (')', 3), (')', 4)])
output_6 = -1
print(check(expected_6, output_6))

print(find_matching_pairs(test_list))




