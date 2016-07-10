"""
the ability to count inversions can be helpful in problems such as measuring
how 2 lists differ: in collaborative filtering, compare 2 peoples' top 10
favorite whatever

in the worst case, there can be n squared inversions
1 2 3 4 5 6
6 5 4 3 2 1
5+4+3+2+1 = 15 = 6 choose 2 inversions because every pair is inverted when
the input is a sorted list in descending order
"""

def merge_and_count_split_inversions(left, right):
    i = 0
    j = 0
    left_len = len(left)
    right_len = len(right)
    new_list = []
    split_inversions = 0
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            new_list.append(left[i])
            i+=1
        else:
            split_inversions += (left_len-i)
            new_list.append(right[j])
            j+=1
    if i == left_len:
        new_list.extend(right[j:])
    else:
        new_list.extend(left[i:])
    return split_inversions, new_list

def sort_and_count_inversions(list_numbers):
    if len(list_numbers)==1: return 0, list_numbers
    half_way_point = len(list_numbers)/2
    left_half  = list_numbers[:half_way_point]
    right_half = list_numbers[half_way_point:]
    c0, left_half = sort_and_count_inversions(left_half)
    c1, right_half = sort_and_count_inversions(right_half)
    c2, list_numbers = merge_and_count_split_inversions(left_half, right_half)
    return c0+c1+c2, list_numbers

def count_inversions_in_file(filename):
    with open(filename) as input:
        list_numbers = []
        for line in input:
            list_numbers.append(int(line))
        # print list_numbers
        return sort_and_count_inversions(list_numbers)[0]

assert count_inversions_in_file('./test_case.txt') == 3

assert count_inversions_in_file('./IntegerArray.txt') == 2407905288