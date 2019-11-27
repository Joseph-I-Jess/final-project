#!/usr/bin/env python3
"""
Placeholder docstring.
"""

def merge_sort(list): 
    if len(list) >1: 
        mid = len(list)//2 #Finding the mid of the array 
        left_list = list[:mid] # Dividing the array elements
        right_list = list[mid:] # into 2 halves 

        merge_sort(left_list) # Sorting the first half 
        merge_sort(right_list) # Sorting the second half 

        index_l = index_r = index_merge = 0

        # Copy data to temp arrays L[] and R[] 
        while index_l < len(left_list) and index_r < len(right_list): 
            if left_list[index_l] < right_list[index_r]: 
                list[index_merge] = left_list[index_l] 
                index_l += 1
            else: 
                list[index_merge] = right_list[index_r] 
                index_r += 1
            index_merge += 1

        # Checking if any element was left 
        while index_l < len(left_list): 
            list[index_merge] = left_list[index_l] 
            index_l += 1
            index_merge += 1

        while index_r < len(right_list): 
            list[index_merge] = right_list[index_r] 
            index_r += 1
            index_merge += 1


test_list = [(5, 0, 0), (1, 3, 1), (1, 2, 2), (1, 1, 3), (1, 0, 4), (0, 5, 0), (0, 4, 1), (4, 0, 1), (4, 1, 0), (4, 0, 1), (3, 1, 1), (3, 0, 2), (2, 3, 0), (4, 1, 0), (2, 
2, 1), (2, 1, 2), (2, 0, 3), (1, 4, 0), (0, 3, 2), (0, 2, 3), (0, 1, 4), (0, 0, 5), (4, 0, 1), (3, 2, 0)]

merge_sort(test_list)
test_list = test_list[::-1]
print(test_list)