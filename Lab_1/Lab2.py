

"""
1- Given a list of numbers, create a function that returns a list where all similar adjacent
elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
Note: You may create a new list or modify the passed in list.
"""
# def remove_adjacent_duplicates(nums):
#     result = []
#
#     for i in range(len(nums)):
#         if i == 0 or nums[i] != nums[i - 1]:
#             result.append(nums[i])
#
#     return result
#
# input_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]
# print(remove_adjacent_duplicates(input_list))

#*************************************************************************************************

"""
2-Consider dividing a string into two halves
Case1:
The length is even, the front and back halves are the same length.
Case2:
The length is odd, we’ll say that the extra char goes in the front half.
E.g. ‘abced’, the front half is ‘abc’, the back half’de.
Given 2 strings, a and b, return a string of the form:
(a-front + b-front) + (a-back +b-back)
"""
# def split_string(string):
#     length = len(string)
#     middle = length // 2
#     if length % 2 == 0:
#         return string[:middle], string[middle:]
#     else:
#         return string[:middle + 1], string[middle + 1:]
#
# def merge_strings(a, b):
#     a_front, a_back = split_string(a)
#     b_front, b_back = split_string(b)
#     return a_front + b_front + a_back + b_back
#
# a = "abcdef"
# b = "123456"
# print(merge_strings(a, b))
#
# a = "abcde"
# b = "12345"
# print(merge_strings(a, b))

#*************************************************************************************************

"""
3- Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other.
E.X. [1,5,7,9] -> True
[2,4,5,5,7,9] -> False
"""
# def all_unique(seq):
#     return len(seq) == len(set(seq))
#
# sequence1 = [1, 5, 7, 9]
# sequence2 = [2, 4, 5, 5, 7, 9]
#
# print(all_unique(sequence1))
# print(all_unique(sequence2))

#*************************************************************************************************

"""
4- Given unordered list, sort it using algorithm bubble sort
( read about bubble sort and try to implement it)
"""
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# my_list = [10,15,1,3,50,4]
# print("Original list:", my_list)
#
# bubble_sort(my_list)
#
# print("Sorted list:", my_list)

#*************************************************************************************************

