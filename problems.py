# import math
# from collections import defaultdict
# import re
# def getPotentialOfWinner(potential, k):
#     win = 0

#     while win is not k:
#         winner = potential[0]
#         player = potential[1]
#         if player > winner:
#             potential.remove(winner)
#             potential.append(winner)
#             win = 1
#         else:
#             potential.remove(player)
#             potential.append(player)
#             win+= 1
#     return winner

# print(getPotentialOfWinner([3, 2, 1, 4],3))



# def maxProfit(costPerCut, salePrice, lengths):
#     maxTotalProfit = 0
#     saleLength = 1
#     while saleLength <= max(lengths):
#         totalUniformRods = 0
#         totalCuts = 0
#         for length in lengths:
#             if length >= saleLength:
#                 totalUniformRods += (length // saleLength)
#                 if length % saleLength == 0:
#                     totalCuts += (length // saleLength) - 1
#                 else:
#                     totalCuts += (length // saleLength)

#             else:
#                 continue
#         totalProfit = totalUniformRods * saleLength * salePrice - totalCuts * costPerCut
#         if maxTotalProfit < totalProfit:
#             maxTotalProfit = totalProfit
#         saleLength += 1
#     return maxTotalProfit

# print(maxProfit(1, 10, [30, 59, 110]))

# def getPrintedStrings(arrays):
#     printedStrings = []
#     cursor_position = 0
#     for array in arrays:
#         command = array[0]
#         value = array[1]
#         if command == 'Insert':
#             word = value
#             cursor_position += len(value)
#         elif command == 'Right':
#             right = int(value)
#             cursor_position += right
#         elif command == 'Delete':
#             delete = int(value)
#             if delete < len(word) - cursor_position:
#                 word = word[:cursor_position] + word[cursor_position + delete:]
#             else:
#                 word = word[:cursor_position]
#         elif command == 'Left':
#             left = int(value)
#             cursor_position -= left
#             if cursor_position < 0:
#                 cursor_position = 0
#         elif command == 'Backspace':
#             backspace = int(value)
#             if backspace < cursor_position:
#                 word = word[:cursor_position - backspace] + word[cursor_position:]
#                 cursor_position -= backspace
#             else:
#                 word = word[cursor_position:]
#                 cursor_position = 0

#         else:
#             printed = int(value)

#             if cursor_position > printed:
#                 appended_word = word[cursor_position - printed:cursor_position + printed]
#                 cursor_position = 0
#             else:
#                 appended_word= word
#             printedStrings.append(appended_word)
#             cursor_position = 0
#     return printedStrings

# twoDArray = [['Insert', 'hello'], ['Left', '3'], ['Delete', '1'], ['Right', '2'], ['Backspace', '1'], ['Print', '4'], ['Insert', 'goodbye'],['Print', '7']]
# print(getPrintedStrings(twoDArray))




# def merge_two(list1, list2):
#     list3 = list1 + list2
#     sorted_merged = sorted(list3)
#     return sorted_merged

# print(merge_two([1, 2, 4], [1, 3, 4]))


# def getMaximumDistinctCount(a, b, k):
#     set_a = set(a)
#     i = 1
#     while i <= k:
#         for num in b:
#             if num not in set_a:
#                 for num_a in a:
#                     num_count = dict()
#                     if num_a in num_count:
#                         num_count[num_a] += 1
#                     else:
#                         num_count[num_a] = 1

#                 for num_a in a:
#                     if num_a in num_count and num_count[num_a] >= 2:
#                         temp = num_a
#                         num_a = num
#                         num = temp
#                 set_a.add(num)

#         i+=1
#     return len(set_a)

# array1 = [3, 5, 3, 5, 5]
# array2 = [2, 4, 1, 2, 1]
# print(getMaximumDistinctCount(array1, array2, 3))


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 print('first list1', list1)
#                 list1 = list1.next
#                 print('second list1', list1)
#             else:
#                 tail.next = list2
#                 print('first list2', list2)
#                 list2= list2.next
#                 print('second list2', list2)
#             tail= tail.next

#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2

#         return dummy.next


# list1 = ListNode(1, ListNode(3, ListNode(5)))
# list2 = ListNode(2, ListNode(4, ListNode(6)))

# solution = Solution()
# print(solution.mergeTwoLists(list1, list2))


#  1. INTEGER_ARRAY numbers
#  2. INTEGER target
#

# def two_sum(numbers, target):
#     for i in range(len(numbers)-1):
#         j = i + 1
#         while j < len(numbers):
#             if numbers[i] + numbers[j] == target:
#                 return [i + 1, j+1]
#             else:
#                 j+=1
#     return None

# print(two_sum([2 ,3, 4], 6))


# def check_inclusion(s1, s2):
#     string_array = list(s2)
#     for i in range(len(string_array) - 1):
#         j = i+1
#         string_fragment = string_array[i] + string_array[j]
#         if s1 == string_fragment or s1[::-1] == string_fragment:
#             return True

#     return False


# def check_inclusion(s1, s2):
#     len_s1 = len(s1)
#     for i in range(len(s2) - len_s1 + 1):
#         string_fragment = s2[i:i+len_s1]
#         print(string_fragment)
#         if string_fragment == s1 or string_fragment == s1[::-1]:
#             return True
#     return False


# def plusMinus(arr):
#     array_size = len(arr)
#     pos_count = 0
#     neg_count = 0
#     zero_count = 0
#     for num in arr:
#         if num > 0:
#             pos_count+=1
#         elif num < 0:
#             neg_count += 1
#         else:
#             zero_count += 1
#     pos_ratio = round(pos_count / array_size, 6)
#     neg_ratio = round(neg_count / array_size, 6)
#     zero_ratio = round(zero_count / array_size, 6)

#     return pos_ratio, neg_ratio, zero_ratio

# # print(plusMinus([1, 1, 0, -1, -1]))
# def plusMinus(arr):
#     array_size = len(arr)
#     pos_count = 0
#     neg_count = 0
#     zero_count = 0
#     for num in arr:
#         if num > 0:
#             pos_count += 1
#         elif num < 0:
#             neg_count += 1
#         else:
#             zero_count += 1
#     pos_ratio = pos_count / array_size
#     neg_ratio = neg_count / array_size
#     zero_ratio = zero_count / array_size

#     return "{:.6f}".format(pos_ratio), "{:.6f}".format(neg_ratio), "{:.6f}".format(zero_ratio)

# print(plusMinus([1,1,0,-1,-1]))


# def timeConversion(s):
#     # Write your code here
#     ltr_val = s[-2:]
#     num_val = s[:-2]
#     if ltr_val == 'PM' and s[:3] == '12':
#         return num_val
#     if ltr_val == 'PM' and s[:3] != '12':
#         int_val = int(num_val[:3])
#         sub_int_val= int_val + 12
#         string_int_val = str(sub_int_val)
#         return string_int_val + num_val[3:]
#     if ltr_val == 'AM' and s[:3] == '12':
#         int_val = int(num_val[:3])
#         print('this is the int_val', int_val)
#         sub_int_val= int_val - 12
#         string_int_val = str(sub_int_val)
#         return string_int_val + num_val[3:]
#     else:
#         return num_val

# print(timeConversion('12:01:00AM'))

# def diagonalDifference(arr):
#     upper_left_val = arr[0][0]
#     upper_right_val = arr[0][len(arr)-1]
#     middle_num = len(arr) // 2
#     middle_val = arr[middle_num][middle_num]
#     lower_left_val = arr[len(arr)-1][0]
#     lower_right_val = arr[len(arr)-1][len(arr)-1]

#     if len(arr) <= 3:
#         return abs((upper_left_val + middle_val + lower_right_val) - (upper_right_val + middle_val + lower_left_val) )

#     else:
#         i = 1
#         j = len(arr) -2
#         additional_left_vals = 0
#         additional_right_vals = 0
#         while i <= len(arr) -2:
#             additional_left_vals += arr[i][i]
#             i+= 1
#         while j > 0:
#             additional_right_vals += arr[j][j]
#             j-= 1
#         return abs((upper_left_val + additional_left_vals + lower_right_val) - (upper_right_val + additional_right_vals + lower_left_val))


# arr1 = [[-1, 1, -7, -8], [-10,-8,-5,-2], [0, 9, 7, -1], [4, 4, -2, 1]]


# print(diagonalDifference(arr1))


# def diagonalDifference(arr):
#     n = len(arr)
#     upper_left_val = arr[0][0]
#     upper_right_val = arr[0][n - 1]
#     middle_val = arr[n // 2][n // 2]
#     lower_left_val = arr[n - 1][0]
#     lower_right_val = arr[n - 1][n - 1]

#     if n <= 3:
#         return abs((upper_left_val + middle_val + lower_right_val) - (upper_right_val + middle_val + lower_left_val))

#     else:
#         additional_left_vals = 0
#         additional_right_vals = 0
#         for i in range(1, n - 1):
#             additional_left_vals += arr[i][i]
#             additional_right_vals += arr[i][n - 1 - i]

#         return abs((upper_left_val + additional_left_vals + lower_right_val) - (upper_right_val + additional_right_vals + lower_left_val))

# arr1 = [[-1, 1, -7, -8], [-10,-8,-5,-2], [0, 9, 7, -1], [4, 4, -2, 1]]
# print(diagonalDifference(arr1))

# def countingSort(arr):
#     # Create a frequency array with 100 elements initialized to 0
#     frequency = [0] * 100
#     print('this is the freq---', frequency)
#     # Count the occurrences of each value in the input array and store in frequency array
#     for num in arr:
#         frequency[num] += 1

#     return frequency

# arr1= [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]
# print(countingSort(arr1))



# import numpy as np

# def maximize_upper_left_sum(matrix):
#     n = len(matrix) // 2
#     upper_left_matrix = matrix[:n, :n]

#     # Calculate the initial sum of the upper left quadrant
#     initial_sum = np.sum(upper_left_matrix)

#     # Create lists to store row and column sums
#     row_sums = [np.sum(row) for row in matrix]
#     col_sums = [np.sum(col) for col in matrix.T]

#     # Sort rows and columns by their sums in descending order
#     sorted_rows = sorted(range(len(row_sums)), key=lambda i: -row_sums[i])
#     sorted_cols = sorted(range(len(col_sums)), key=lambda i: -col_sums[i])

#     # Initialize the best configuration as the original matrix
#     best_config = np.copy(matrix)
#     best_sum = initial_sum

#     # Iterate through all possible row and column reversals
#     for i in range(n):
#         for j in range(n):
#             new_matrix = np.copy(matrix)
#             new_matrix[sorted_rows[i], :] = matrix[sorted_rows[i], ::-1]
#             new_matrix[:, sorted_cols[j]] = matrix[:, sorted_cols[j]][::-1]

#             # Calculate the sum of the new upper left quadrant
#             new_sum = np.sum(new_matrix[:n, :n])

#             # Update the best configuration if the new sum is greater
#             if new_sum > best_sum:
#                 best_config = new_matrix
#                 best_sum = new_sum

#     return best_config

# # Example usage:
# matrix = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12],
#                   [13, 14, 15, 16]])

# result_matrix = maximize_upper_left_sum(matrix)
# print(result_matrix)


# def maxMin(k, arr):
#     min_diff = math.inf
#     sorted_arr = sorted(arr)
#     for i in range(len(sorted_arr)-k+1):
#         array_fragment = sorted_arr[i:i+k]
#         diff = max(array_fragment) - min(array_fragment)
#         if diff < min_diff:
#             min_diff = diff

#     return min_diff

# arr_1 = [10000,
# 2430,
# 7312,
# 3388,
# 3611,
# 5536,
# 7718,
# 4945,
# 4900,
# 3226,
# 4081,
# 3342,
# 9022,
# 1638,
# 1989,
# 8337,
# 5366,
# 8535,
# 4187,
# 3927]
# print(maxMin(2, arr_1))

# def dynamicArray(n, queries):
#     arr = [[] for _ in range(n)]
#     lastAnswer = 0
#     answers = []  # Initialize an empty list to store the answers

#     for query in queries:
#         query_type = query[0]
#         x = query[1]
#         y = query[2]

#         if query_type == 1:
#             # Query type 1: Append the integer y to the x-th array
#             arr[x].append(y)
#         else:
#             # Query type 2: Use modulo to wrap around the index
#             index = (x ^ lastAnswer) % n
#             variable = arr[index][y]
#             # Append the value to the answers array
#             answers.append(variable)
#             lastAnswer = variable

#     return answers


# def asteroidCollision(asteroids):
#         stack = []

#         for asteroid in asteroids:
#             # Check if there's a collision
#             while stack and stack[-1] > 0 and asteroid < 0:
#                 top_asteroid = stack.pop()

#                 # Determine the outcome of the collision
#                 if abs(top_asteroid) == abs(asteroid):
#                     # Both asteroids are destroyed
#                     break
#                 elif abs(top_asteroid) > abs(asteroid):
#                     # The top asteroid survives
#                     stack.append(top_asteroid)
#                     break
#                 else:
#                     # The current asteroid survives, continue checking
#                     continue
#             else:
#                 # No collision, simply add the asteroid to the stack
#                 stack.append(asteroid)

#         return stack


#Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

#The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

#Example
#Input: "UD"
#Output: true
#Example 2:
#Input: "LL"
#Output: false

#position array with two values [0,0]
#iterate through moves, changing position values as needed
#if position ever equals [0,0], return true- if not, return false

# def self_dividing_number(left, right):
#     self_divide_array = []

#     for num in range(left, right + 1):
#         string_num = str(num)

#         if '0' in string_num:
#             continue

#         is_self_dividing = True

#         for digit_char in string_num:
#             individual_int = int(digit_char)

#             if num % individual_int != 0:
#                 is_self_dividing = False
#                 break

#         if is_self_dividing:
#             self_divide_array.append(num)

#     return self_divide_array



# left1 = 1
# left2 = 22
# print(self_dividing_number(left1, left2))

# def extractErrorLogs(logs):
#     print('these are the logs', logs)
#     status_logs = []
#     for log in logs:
#         status = log[2]
#         if status == 'ERROR' or status == 'CRITICAL':
#             status_logs.append(log)


# logs_1 = [['01-01-2022', '18:00', 'CRITICAL', 'failed'], ['01-01-2023', '15:00', 'ERROR', 'failed'], ['01-01-2023', '16:00', 'SUCCESS', 'established']]
# extractErrorLogs(logs_1)


# def getMatchingProducts(products, queries):
#     print('products---', products)
#     print('queries---', queries)
#     sorted_products = sorted(products, key=lambda products: int(products[1]))
#     print('sorted_products---', sorted_products)
#     returned_products = []

#     for query in queries:
#         returned_products.append([])
#         for product in sorted_products:
#             if query[0] == 'Type1':
#                 if query[1] == product[2]:
#                     returned_products[-1].append(product[0])
#                 else:
#                     continue
#             elif query[0] == 'Type2':
#                 if int(query[1]) > int(product[1]):
#                     returned_products[-1].append(product[0])
#                 else:
#                     continue
#             elif query[0] == 'Type3':
#                 if int(query[1]) < int(product[1]):
#                     returned_products[-1].append(product[0])
#     return returned_products

# def countPalindromicSubsequence(s):
#     palindromes = set()
#     left = set(s[0])
#     right = defaultdict(int)
#     for i in range(2, len(s)):
#         char = s[i]
#         right[char] += 1

#     for i in range(1,len(s)-1):
#         mid_char = s[i]

#         for left_char in left:
#             if right[left_char] > 0:
#                 palindromes.add(f'{left_char}{mid_char}{left_char}')
#         right[s[i+1]] -= 1
#         left.add(mid_char)
#     return len(palindromes)
# month = []

# def updateLeapYear(year):
#     if year % 400 == 0:
#         month[2] = 29
#     elif year % 100 == 0:
#         month[2] = 28
#     elif year % 4 == 0:
#         month[2] = 29
#     else:
#         month[2] = 28

# def storeMonth():
#     month[1] = 31
#     month[2] = 28
#     month[3] = 31
#     month[4] = 30
#     month[5] = 31
#     month[6] = 30
#     month[7] = 31
#     month[8] = 31
#     month[9] = 30
#     month[10] = 31
#     month[11] = 30
#     month[12] = 31

# def findPrimeDates(d1, m1, y1, d2, m2, y2):
#     storeMonth()
#     result = 0

#     while(True):
#         x = d1
#         x = x * 100 + m1
#         x = x * 10000 + y1
#         if x % 4 == 0 or x % 7 == 0:
#             result = result + 1
#         if d1 == d2 and m1 == m2 and y1 == y2:
#             break
#         updateLeapYear(y1)
#         d1 = d1 + 1
#         if d1 > month[m1]:
#             m1 = m1 + 1
#             d1 = 1
#             if m1 > 12:
#                 y1 =  y1 + 1
#                 m1 = 1
#     return result;

# for i in range(1, 15):
#     month.append(31)

# line = input()
# date = re.split('-| ', line)
# d1 = int(date[0])
# m1 = int(date[1])
# y1 = int(date[2])
# d2 = int(date[3])
# m2 = int(date[4])
# y2 = int(date[5])

# result = findPrimeDates(d1, m1, y1, d2, m2, y2)
# print(result)
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

#iterate through arrray
#create left_array and right_array variable
#if sum is equal, return "YES", else "NO"

# def balancedSums(arr):
#     if len(arr) == 1:
#         return "YES"
#     if len(arr) == 2 and arr[0] == arr[1]:
#         return "YES"
#     if len(arr) == 3 and arr[0] == arr[2]:
#         return "YES"
#     if arr[0] == sum(arr[1:len(arr)]):
#         return "YES"

# def balancedSums(arr):
#     left_sum = 0
#     total_sum = sum(arr)
#     for i in range(len(arr)):
#         right_sum = total_sum - left_sum - arr[i]
#         if left_sum == right_sum:
#             return "YES"
#         else:
#             left_sum = left_sum + arr[i]
#     return "NO"















# arr1= [1, 2, 3]
# arr2= [1, 1, 4, 1, 1]


# print(balancedSums(arr1))
# print(balancedSums(arr2))



# def getWinner(arr, k):
#         if k>= len(arr):
#             return max(arr)

#         wins = 0
#         curr_winner = arr[0]
#         i = 1

#         while wins < k and i < len(arr):
#               opponent = arr[i]
#               if curr_winner > opponent:
#                     wins += 1
#               else:
#                     curr_winner = opponent
#                     wins = 1
#               i += 1
#               i %= len(arr)


#         return curr_winner





# print(getWinner([2,1,3,5,4,6,7], 2))
# print(getWinner([3,2,1], 10))
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque
# def invertTree(root: TreeNode) -> TreeNode:
#     if not root:
#         return None

#     queue = deque()
#     queue.append(root)

#     while queue:
#         node = queue.popleft()

#         node.left, node.right = node.right, node.left

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

#     return root


# class TreeNode:
#     def __init__(self, x):
#      self.val = x
#      self.left = None
#      self.right = None

# def lowestCommonAncestor(root, p, q):
#    def valArray

# def diameterOfBinaryTree(root) :
#             diameter = 0
#             def depth(node):
#                 nonlocal diameter
#                 if node is None:
#                     return 0

#                 left = depth(node.left)
#                 right = depth(node.right)

#                 diameter = max(diameter, left + right)
#                 return 1 + max(left, right)

#             depth(root)
#             return diameter


# def commonSubstring(a, b):
#     for i in range(len(a)):
#         element_a = a[i]
#         element_b = b[i]

#         found_common_char = False

#         for char in element_a:
#             if char in element_b:
#                 print('YES')
#                 found_common_char = True
#                 break

#         if not found_common_char:
#             print('NO')
# commonSubstring(['hello', 'world'], ['he', 'bye'])

# def commonSubstring(a, b):
#     for s1, s2 in zip(a,b):
#         letters = set(s1)
#         found = False

#         for letter in s2:
#             if letter in letters:
#                 print('YES')
#                 found = True
#                 break
#         if not found:
#             print('NO')



# def getLatestKRequests(requests, K):
#     res = list()
#     res.append(requests[len(requests)-1])
#     for i in range(len(requests) -2, 0, -1):
#         if len(res) == K:
#             break
#         req = requests[i]
#         if req not in res:
#             res.append(req)
#     return res


# def getLatestKRequests(requests, K):
#     seen = set()
#     res = list()
#     for req in requests[::1]:
#         if req not in seen:
#             seen.add(req)
#             res.append(req)

#         if len(res) == K:
#             break
#     return res



# print(getLatestKRequests(['item3', 'item2', 'item1', 'item2', 'item3'], 3))
# from collections import Counter

# def countCharacters(words, chars):
#         total = 0
#         count = Counter(chars)
#         print('count---', count)


#         for word in words:
#             word_count = Counter(word)
#             print('word_count---', word_count)

#             if all(word_count[char] <= count[char] for char in word):
#                 total += len(word)


#         return total
# print(countCharacters(["cat","bt","hat","tree"], 'atach'))

# def isPangram (stringy):
#     return len(set(filter(str.isalpha, stringy.lower()))) == 26

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# def list_to_tree(lst):
#     if not lst:
#         return None

#     nodes = [None if val is None else TreeNode(val) for val in lst]
#     for i in range(len(nodes)):
#         if nodes[i] is not None:
#             left_child_index = 2 * i + 1
#             right_child_index = 2 * i + 2
#             if left_child_index < len(nodes):
#                 nodes[i].left = nodes[left_child_index]
#             if right_child_index < len(nodes):
#                 nodes[i].right = nodes[right_child_index]

#     return nodes[0]

# def isBalanced(root):
#     def dfs(root):
#         if not root: return [True, 0]

#         left, right = dfs(root.left), dfs(root.right)
#         balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

#         return [balanced, 1 + max(left[1], right[1])]

#     return dfs(root)[0]

# tree_root = list_to_tree([1,2,2,3,3,None,None,4,4])

# print(isBalanced(tree_root))
# def isSameTree(p, q):
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
#         else:
#             return (
#                 p.val == q.val
#                 and isSameTree(p.left, q.left)
#                 and isSameTree(p.right, q.right)
#  )

# def issubtree(root, subroot):
#     stack = []
#     stack.append(root)
#     while len(stack) > 0:
#         node = stack.pop()
#         if isSameTree(node, subroot):
#              return True
#         else:
#              stack.append(node.right)
#              stack.append(node.left)
#     return False

# from collections import deque
# def lowestCommonAncestor(root, p, q):
#     def isAncestor(root, target):
#         if root is None:
#             return False

#         if root == target:
#             return True

#         left_result = isAncestor(root.left, target)
#         right_result = isAncestor(root.right, target)

#         return left_result or right_result
#     ancestors = list()
#     queue = deque()
#     queue.append(root)
#     while queue:
#         node = queue.popleft()
#         if isAncestor(node, p) and isAncestor(node, q):
#             ancestors.append(node)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     return ancestors[0]
# def lowestCommonAcnestor(root, p, q):
#     curr = root
#     while curr:
#         if p.val > curr.val and q.val > curr.val:
#             curr = curr.right
#         elif p.val < curr.val and q.val < curr.val:
#             curr = curr.left
#         else:
#             return curr

# from collections import deque
# def levelOrder(root):
#         if not root:
#             return []

#         else:
#             queue = deque()
#             queue.append(root)
#             order_list = list()

#             while queue:

#                 level_sub_array = []

#                 for _ in range(len(queue)):
#                     node = queue.popleft()
#                     level_sub_array.append(node.val)

#                     if node.left:
#                         queue.append(node.left)

#                     if node.right:
#                         queue.append(node.right)

#                 order_list.append(level_sub_array)

#             return order_list
# def rightSideView(root):
#      if not root:
#             return []

#      queue = deque()
#      queue.append(root)
#      right_list = []

#      while queue:
#         level_size = len(queue)

#         for i in range(level_size):
#             node = queue.popleft()

#             if i == level_size - 1:
#                     right_list.append(node.val)

#             if node.left:
#                     queue.append(node.left)
#             if node.right:
#                     queue.append(node.right)

#      return right_list


# def onesMinusZeros(grid):
#         ROWS = len(grid)
#         COLS = len(grid[0])

#         difference = [[0 for _ in range(COLS)] for _ in range(ROWS)]

#         row_ones = [0]*ROWS
#         col_ones = [0]*COLS

#         print(row_ones, col_ones)

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == 1:
#                     row_ones[r] += 1
#                     col_ones[c] += 1

#         for r in range(ROWS):
#             for c in range(COLS):
#                 difference[r][c] = row_ones[r] + col_ones[c] - (ROWS-row_ones[r]) - (COLS-col_ones[c])

#         return difference

# print(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))


# adjList = {
#     1: [2, 5],
#     2: [1, 3, 5],
#     3: [2, 4],
#     4: [3, 5, 6],
#     5: [1, 2, 4],
#     6: [4]
# }

# def printBreadthFirst(start):
#     queue = deque()
#     queue.append(start)
#     visited_set = set()
#     visited_set.add(start)

#     while queue:
#         node = queue.popleft()
#         print(node)
#         for number in adjList[node]:
#             if number not in visited_set:
#                 queue.append(number)
#                 visited_set.add(number)


# print("First Test:")
# printBreadthFirst(3)

# print("Second Test:")
# printBreadthFirst(6)


# print("Third Test:")
# printBreadthFirst(4)

# adjList = {
#     1: [2, 5],
#     2: [1, 3, 5],
#     3: [2, 4],
#     4: [3, 5, 6],
#     5: [1, 2, 4],
#     6: [4]
# }

# def printDepthFirst(start):
#     stack = list()
#     stack.append(start)
#     visited_set = set()
#     visited_set.add(start)

#     while stack:
#         node = stack.pop()
#         print(node)
#         for number in adjList[node]:
#             if number not in visited_set:
#                 stack.append(number)
#                 visited_set.add(number)

# print("First Test:")
# printDepthFirst(3)


# from collections import deque

# adjList = {
#     1: [2, 5],
#     2: [1, 3, 5],
#     3: [2, 4],
#     4: [3, 5, 6],
#     5: [1, 2, 4],
#     6: []
# }
# def aShortestPath(start, end):
#     queue = deque()
#     queue.append([start])
#     visited_set = set()
#     visited_set.add(start)

#     while queue:
#         path = queue.popleft()
#         last_node = path[-1]
#         print('the last node', last_node)

#         if last_node == end:
#             return len(path) - 1
#         else:
#             for neighbor in adjList[last_node]:
#                 if neighbor not in visited_set:
#                     visited_set.add(neighbor)
#                     copy_path = path[:]
#                     copy_path.append(neighbor)
#                     queue.append(copy_path)
#     return False


# print("First Test:")
# print(aShortestPath(1, 3))
# print("Second Test:")
# print(aShortestPath(6,1))






# def compressedString(message):
#     new_str = ''
#     seen_letter = ''
#     count = 0

#     for letter in message:

#         if letter != seen_letter:
#             new_str += f'{seen_letter}{count if count > 1 else ""}'
#             seen_letter = letter
#             count = 0

#         count+=1

#     new_str += f'{seen_letter}{count if count > 1 else ""}'

#     return new_str






# def minimumMoves(arr1, arr2):
#     count = 0

#     for i in range(len(arr1)):
#         number1, number2 = str(arr1[i]), str(arr2[i])

#         for i in range(len(number1)):
#             digit1, digit2 = int(number1[i]), int(number2[i])

#             if digit1 == digit2:
#                 count +=0
#             else:
#                 count += abs(digit1 - digit2)

#     return count

# arr1 = [123, 956]
# arr2 = [224, 456]

# print(minimumMoves(arr1, arr2))

#for each number, add all elements in array to subset_array
#cut off last element of array each time, adding new array to queue
#when queue is finished, add number to set


# from collections import deque

# def subsets(nums):
#     subset_arrays = []
#     queue = deque()
#     queue.append(([], nums))

#     while queue:
#         current_subset, remaining_nums = queue.popleft()
#         subset_arrays.append(current_subset)

#         for i, num in enumerate(remaining_nums):
#             queue.append((current_subset + [num], remaining_nums[i+1:]))

#     return subset_arrays



# def combinationSum(candidates, target):
#     subset_arrays = list()
#     queue = deque()
#     queue.append(([], candidates))

#     while queue:
#         current_subset, remaining_nums = queue.popleft()
#         if sum(current_subset) == target:
#             subset_arrays.append(current_subset)

#         elif sum(current_subset) < target:
#             for i, num in enumerate(remaining_nums):
#                 queue.append((current_subset + [num], remaining_nums[i:]))


#     return subset_arrays

# candidates = [7, 2,3,6,]
# target = 7

# print(combinationSum(candidates, target))

# from collections import defaultdict
# def leastBricks(self, wall: List[List[int]]) -> int:
#         gap_count = defaultdict(int)

#         for row in wall:
#             total = 0
#             for brick in row[:-1]:
#                 total += brick
#                 gap_count[total] += 1

#         gap_vals = gap_count.values()

#         print(gap_count)
#         return len(wall) if len(gap_vals) == 0 else len(wall) - max(gap_vals)



# def numIslands(grid):
#     def findNeighbors(node, matrix):
#         [row, col] = node

#         neighbors = [
#         [row - 1, col],
#         [row + 1, col],
#         [row, col - 1],
#         [row, col + 1],
#         ]


#         valid_neighbors = [
#             current_node
#             for current_node in neighbors
#             if (
#                 0 <= current_node[0] < len(matrix)
#                 and 0 <= current_node[1] < len(matrix[0])
#                 and matrix[current_node[0]][current_node[1]] == 1
#             )
#         ]
#         return valid_neighbors
# from collections import deque
# def numIslands(grid):

#     def findNeighbors(node, matrix):
#         [row, col] = node

#         neighbors = [
#             [row - 1, col],
#             [row + 1, col],
#             [row, col - 1],
#             [row, col + 1],
#         ]

#         valid_neighbors = [
#             tuple(current_node)
#             for current_node in neighbors
#             if (
#                 0 <= current_node[0] < len(matrix)
#                 and 0 <= current_node[1] < len(matrix[0])
#                 and int(matrix[current_node[0]][current_node[1]]) == 1
#             )
#         ]
#         return valid_neighbors

#     islands_count = 0
#     visited = set()

#     for row in range(len(grid)):
#         for column in range(len(grid[row])):
#             node = [row, column]
#             if tuple(node) not in visited and int(grid[row][column]) == 1:
#                 islands_count += 1
#                 visited.add(tuple(node))

#                 queue = deque([node])
#                 while queue:
#                     current_node = queue.popleft()
#                     neighbors = findNeighbors(current_node, grid)
#                     for neighbor in neighbors:
#                         if neighbor not in visited:
#                             queue.append(neighbor)
#                             visited.add(neighbor)

#     return islands_count

# print(numIslands([["1", "1", "1", "1", "0"],
#                  ["1", "1", "0", "1", "0"],
#                  ["1", "1", "0", "0", "0"],
#                  ["0", "0", "0", "0", "0"]]))


# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


# def cloneGraph(node:['Node']):
#     graph = list()
#     queue = deque()
#     queue.append(node)
#     visited = set()

#     while queue:

#         curr_node = queue.popleft()
#         val = curr_node.val
#         if val not in visited:
#             visited.add(val)
#             sub_array = []
#             neighbors = curr_node.neighbors
#             for neighbor in neighbors:
#                 sub_array.append(neighbor.val)
#             graph.append(sub_array)
#     return graph


# def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
#         if not node:
#             return None

#         original_to_clone = {}
#         queue = deque()
#         queue.append(node)
#         visited = set()

#         while queue:
#             curr_node = queue.popleft()
#             val = curr_node.val

#             if val not in visited:
#                 visited.add(val)

#                 # Check if the node is already cloned
#                 if val not in original_to_clone:
#                     original_to_clone[val] = Node(val)
#                 cloned_node = original_to_clone[val]

#                 # Process neighbors
#                 for neighbor in curr_node.neighbors:
#                     neighbor_val = neighbor.val
#                     if neighbor_val not in original_to_clone:
#                         original_to_clone[neighbor_val] = Node(neighbor_val)
#                         queue.append(neighbor)
#                     cloned_node.neighbors.append(original_to_clone[neighbor_val])

#         # Return the cloned node corresponding to the input node
#         return original_to_clone[node.val]


# from collections import deque

# def numIslands(grid):

#     def findNeighbors(node, matrix):
#         [row, col] = node

#         neighbors = [
#             [row - 1, col],
#             [row + 1, col],
#             [row, col - 1],
#             [row, col + 1],
#         ]

#         valid_neighbors = [
#             tuple(current_node)
#             for current_node in neighbors
#             if (
#                 0 <= current_node[0] < len(matrix)
#                 and 0 <= current_node[1] < len(matrix[0])
#                 and int(matrix[current_node[0]][current_node[1]]) == 1
#             )
#         ]
#         return valid_neighbors

#     islands_count = 0
#     visited = set()

#     for row in range(len(grid)):
#         for column in range(len(grid[row])):
#             node = [row, column]
#             if tuple(node) not in visited and int(grid[row][column]) == 1:
#                 islands_count += 1
#                 visited.add(tuple(node))

#                 queue = deque([node])
#                 while queue:
#                     current_node = queue.popleft()
#                     neighbors = findNeighbors(current_node, grid)
#                     for neighbor in neighbors:
#                         if neighbor not in visited:
#                             queue.append(neighbor)
#                             visited.add(neighbor)

#     return islands_count

# print(numIslands([["1", "1", "1", "1", "0"],
#                  ["1", "1", "0", "1", "0"],
#                  ["1", "1", "0", "0", "0"],
#                  ["0", "0", "0", "0", "0"]]))

# from collections import deque
# def maxAreaOfIsland(grid):
#         def findNeighbors(node, matrix):
#             [row, col] = node

#             neighbors = [
#                 [row - 1, col],
#                 [row + 1, col],
#                 [row, col - 1],
#                 [row, col + 1],
#             ]

#             valid_neighbors = [
#                 tuple(current_node)
#                 for current_node in neighbors
#                 if (
#                     0 <= current_node[0] < len(matrix)
#                     and 0 <= current_node[1] < len(matrix[0])
#                     and matrix[current_node[0]][current_node[1]] == 1
#                 )
#             ]
#             return valid_neighbors

#         max_area = 0
#         visited = set()
#         for row in range(len(grid)):
#             for column in range(len(grid[row])):
#                 island_area = 0
#                 node = tuple([row, column])
#                 if node not in visited and (grid[row][column] == 1):
#                     visited.add(node)
#                     island_area += 1

#                     queue = deque([node])
#                     while queue:
#                         current_node = queue.popleft()
#                         neighbors = findNeighbors(current_node, grid)
#                         for neighbor in neighbors:
#                             if neighbor not in visited:
#                                 queue.append(neighbor)
#                                 visited.add(neighbor)
#                                 island_area +=1
#                     if island_area > max_area:
#                         max_area = island_area
#         return max_area


## iteratre through matrix- for each node, if all of its left neighbors (and neighbor's neighbors, etc.) OR all of its right neighbors AND all of its up neighbors OR all of its down neighbors are valid, add it to ouptut
## top row, leftmost column- if a node's closest neighbor is less than or equal, and all the other right or bottom neighbors are in ascending order, add
##last row, rightmost column- if a node's closest neighbor is less than or equal, and all other left or top neighbors are in ascending order, add

# def pacificAtlantic(heights):
#     def dfs(row, col, prev_value, ocean):
#         if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]) or visited[row][col] or heights[row][col] < prev_value:
#             return

#         visited[row][col] = True

#         if ocean == "pacific":
#             pacific_reachable[row][col] = True
#         elif ocean == "atlantic":
#             atlantic_reachable[row][col] = True

#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         for dr, dc in directions:
#             new_row, new_col = row + dr, col + dc
#             dfs(new_row, new_col, heights[row][col], ocean)

#     if not heights:
#         return []

#     rows, cols = len(heights), len(heights[0])
#     visited = [[False] * cols for _ in range(rows)]
#     pacific_reachable = [[False] * cols for _ in range(rows)]
#     atlantic_reachable = [[False] * cols for _ in range(rows)]

#     for row in range(rows):
#         dfs(row, 0, float('-inf'), "pacific")

#     for col in range(cols):
#         dfs(0, col, float('-inf'), "pacific")

#     visited = [[False] * cols for _ in range(rows)]

#     for row in range(rows):
#         dfs(row, cols - 1, float('-inf'), "atlantic")

#     for col in range(cols):
#         dfs(rows - 1, col, float('-inf'), "atlantic")

#     valid_nodes = []
#     for row in range(rows):
#         for col in range(cols):
#             if pacific_reachable[row][col] and atlantic_reachable[row][col]:
#                 valid_nodes.append([row, col])

#     return valid_nodes

# heights1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# print(pacificAtlantic(heights1))


# def superDigit(n, k):
#     def calculate_super_digit(number_string):
#         if len(number_string) == 1:
#             return int(number_string)

#         digit_sum = sum(int(digit) for digit in number_string)
#         return calculate_super_digit(str(digit_sum))

#     initial_super_digit = sum(int(digit) for digit in n) * k
#     return calculate_super_digit(str(initial_super_digit))





# def counterGame(n):
#     turn = 0

#     while n != 1:
#         if n & (n - 1) == 0:
#             n //= 2
#         else:
#             largest_power_of_two = 1 << ( - 1)
#             n -= largest_power_of_two

#         turn += 1

#     return 'Richard' if turn % 2 == 0 else 'Louise'



# n = 4  # binary: 1010
# x = 0  # binary: 0111

# # Using bitwise XOR
# result_xor = n ^ x

# # Using addition
# result_addition = n + x

# print(result_xor)
# print(result_addition)


# def count_unset_bits(n):
#     count = 0
#     while n:
#         count += n % 2 == 0
#         n //= 2
#     return count

# def sumXor(n):
#     unset_bits_count = count_unset_bits(n)
#     print(unset_bits_count)
#     result = 2 ** unset_bits_count
#     return result

# print(sumXor(4))



# def flippingMatrix(matrix):
#     max_total = 0
#     n = int(len(matrix)/2)

#     for i in range(n):
#         for j in range(n):
#             max_s = max(matrix[i][j], matrix[i][(2*n-1)-j], matrix[(2*n-1)-i][j], matrix[(2*n-1)-i][(2*n-1)-j])
#             max_total += max_s

#     return max_total





# matrix1 = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]


# ##Expected OutPut is uppermatrix 119, 114, 56, 125 = 414
# print(flippingMatrix(matrix1))



# from collections import Counter
# def anagram(s):
#     if len(s) % 2 != 0:
#         return -1


#     split = len(s) // 2
#     s_1 = sorted(s[0:split])
#     s_2 = sorted(s[split:])

#     if s_1 == s_2:
#         return 0


#     else:
#         changes = 0

#         for i in range(len(s_1)):
#             if s_1[i] != s_2[i]:
#                 changes += 1




#     return changes

# print(anagram('aaabbb'))
# print(anagram('ab'))
# print(anagram('abc'))
# print(anagram('mnop'))
# print(anagram('xyyx'))
# print(anagram('xaxbbbxx'))



#key = place in grid, value = i

# def replace_char(string, index, new_char):
#             string = string[:index] + new_char + string[index + 1:]
#             return string


# def bomberMan(n, grid):
#             row = len(grid)
#             char = len(grid[0])

#             def detonate(grid):
#                     chords = set()
#                     for i in range(row):
#                             j = grid[i].find("O")
#                             print('this is j', j)
#                             while j != -1:
#                                     if grid[i][j] == "O":
#                                             chords.update([(i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
#                                     j = grid[i].find("O", j + 1)
#                             grid[i] = "O" * char
#                     for i, j in chords:
#                             if 0 <= i < row and 0 <= j < char:
#                                     grid[i] = replace_char(grid[i], j, ".")
#                     return grid

#             if n == 1:
#                     return grid
#             elif n % 2 == 0:
#                     return ["O" * char for i in range(row)]
#             elif n == 3:
#                     return detonate(grid)
#             elif (n + 1) % 4 == 0:
#                     return detonate(grid)
#             else:
#                     return detonate(detonate(grid))

# n = 3
# grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']

# print(bomberMan(n, grid))


# from collections import Counter
# def isValid(s):
#     count = Counter(s)
#     vals = list(count.values())
#     first_val = vals[0]
#     dif_count = 0
#     for i in range(len(vals)):
#         if vals[i] != first_val:
#             dif_count += 1
#         if dif_count >= 2:
#             return 'NO'
#     return 'YES'

# print(isValid('aaaabbcc'))

# def minimumBribes(q):
#     bribes = 0

#     index_map = {s: i for i, s in enumerate(q, start=1)}
#     position_map = {i: s for i, s in enumerate(q, start=1)}

#     for index in range(len(q), 0, -1):
#         print('index_map', index_map)
#         print('position_map', position_map)
#         position = index_map[index]
#         print('index', index)
#         print('position', position)

#         diff = index - position
#         if diff > 2:
#             print('Too chaotic')
#             return
#         bribes += diff

#         # update position infos (simulates removing item 'index')
#         for i in range(position, index):
#             index_to_move = position_map[i + 1]
#             index_map[index_to_move] = i
#             position_map[i] = index_to_move

#         del index_map[index]

#     print(bribes)

# minimumBribes([2, 1, 5, 3, 4])


# def climbingLeaderboard(ranked, player):

#     scores = list()
#     for score in player:
#         ranked_set = list(set(ranked))
#         ranked_set.append(score)
#         ranked_set.sort(reverse=True)
#         rank = ranked_set.index(score) + 1
#         scores.append(rank)

#     return scores



# def climbingLeaderboard(ranked, player):

#     for i, score in enumerate(player):
#         ranked_set = list(set(ranked))
#         ranked_set.append(score)
#         ranked_set.sort(reverse=True)
#         rank = ranked_set.index(score) + 1
#         player[i] = rank


#     return player

# def climbingLeaderboard(ranked, player):
#     unique_ranked = sorted(set(ranked), reverse=True)  # Remove duplicates and sort in descending order
#     print('unique_ranked', unique_ranked)
#     scores = []
#     for score in player:
#         rank = find_rank(unique_ranked, score)
#         scores.append(rank)

#     return scores

# def find_rank(rankedList, score):
#     low, high = 0, len(rankedList) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if rankedList[mid] == score:
#             return mid + 1
#         elif rankedList[mid] > score:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return low + 1


# ranked = [100, 100, 50, 40, 40, 20, 10]

# player = [5, 25, 50, 120]

# print(climbingLeaderboard(ranked, player))
# from collections import defaultdict

# def icecreamParlor(m, arr):
#     index_dict = {}  # A dictionary to store the indices of visited elements

#     for i, cost in enumerate(arr):
#         complement = m - cost

#         if complement in index_dict:
#             # Found a pair that adds up to m
#             return [index_dict[complement] + 1, i + 1]

#         # Add the current element and its index to the dictionary
#         index_dict[cost] = i

#     return None  # No such pair found

# print(icecreamParlor(8, [2, 6, 3, 4, 8]))




# def isBalanced(s):
#     symbol_dict = {'}': '{', ']': '[', ')': '('}
#     keys = symbol_dict.keys()
#     stack = list()

#     for char in s:
#         if char not in keys:
#             stack.append(char)
#         elif char in keys and stack:
#             matched = stack.pop()
#             if symbol_dict[char] != matched:
#                 return 'NO'

#     return 'NO' if stack else 'YES'








# s1 = "{[()]}" #YES
# s2 = "[(])" #NO
# s3 = '{{[[(())]]}}' #YES
# s4 = '{{([])}}' #YES
# s5 = '{{)[](}}' #NO
# s6 = '{(([])[])[]}' #YES
# s7 = '{(([])[])[]]}' #NO
# s8 = '{(([])[])[]}[]' #YES


# print(isBalanced(s1))
# print(isBalanced(s2))
# print(isBalanced(s3))
# print(isBalanced(s4))
# print(isBalanced(s5))
# print(isBalanced(s6))
# print(isBalanced(s7))
# print(isBalanced(s8))


# def waiter(number, q):
#     def primeArray(number):
#         def isPrime(num):
#             if num < 2:
#                 return False
#             for i in range(2, int(num**0.5) + 1):
#                 if num % i == 0:
#                     return False
#             return True

#         prime_array = []
#         i = 2
#         while len(prime_array) < number:
#             if isPrime(i):
#                 prime_array.append(i)
#             i += 1

#         return prime_array

#     primes = primeArray(q)
#     answers = []
#     stackA = []
#     stackB = []

#     for n in range(q):
#         current_prime = primes[n]
#         for plate in number:
#             if plate % current_prime == 0:
#                 stackB.append(plate)
#             else:
#                 stackA.append(plate)
#         while stackB:
#             answers.append(stackB.pop())
#         number = stackA
#         stackA = []

#     while number:
#         answers.append(number.pop())

#     return answers



# # number1 = [3, 4, 7, 6, 5]

# number2 = [3, 3, 4, 4, 9]

# # print(waiter(number1, 1))
# print(waiter(number2, 2))


# def reverse(llist=None, prev=None):
#     if llist is None:
#         return prev
#     temp = llist.next
#     llist.next = prev
#     prev = llist
#     return reverse(temp, prev)


# def reverseDouble(llist):
#     if llist is None:
#         return None
#     next_node = llist.next
#     llist.next, llist.prev = llist.prev, llist.next
#     if next_node is None:
#         return llist
#     return reverseDouble(next_node)


# def insertNodeAtPosition(llist, data, position):

#     new_node = SinglyLinkedListNode(data)
#     prev_node = None
#     next_node = llist
#     while position > 0:
#         prev_node, next_node = next_node, next_node.next
#         position -= 1
#     if prev_node is not None:
#         prev_node.next = new_node
#     new_node.next = next_node
#     return llist

# def mergeTwoLists(list1, list2):
#         cur = new_list = ListNode()
#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2

#         if list1 or list2:
#             cur.next = list1 if list1 else list2

#         return new_list.next

# def maxAdjSum(A):
#     count = 0
#     sums = {}
#     prev_sum = -1
#     for i in range(len(A) - 1):
#         current_sum = A[i] + A[i + 1]
#         print('current_sum', current_sum)
#         if current_sum not in sums:
#             sums[current_sum] = 1
#             prev_sum = current_sum
#         elif current_sum != prev_sum:
#             sums[current_sum] += 1
#             prev_sum = current_sum
#         else:
#             prev_sum = -1
#         print('sums', sums)
#         count = max(count, sums[current_sum])
#         print('count', count)

#     return count

# print("[10, 1, 3, 1, 2, 2, 1, 0, 4]: ",maxAdjSum([10, 1, 3, 1, 2, 2, 1, 0, 4])) # 3
# print("[5, 3, 1, 3, 2, 3]: ",maxAdjSum([5, 3, 1, 3, 2, 3])) # 1
# print("[9, 9, 9, 9, 9]: ",maxAdjSum([9, 9, 9, 9, 9])) # 2
# print("[1, 5, 2, 4, 3, 3]: ",maxAdjSum([1, 5, 2, 4, 3, 3])) # 3


# ]

#helper function to count occurances of each value in A
#another helper function to find substing with least unique values
#turn substring with least unique values to a variable, remove variable from A. Turn A into a set and return length of set
# from collections import Counter
# def solution(A, R):
#     string_list = [str(num) for num in A]

#     def least_unique(string_list, substring_length):
#         count = Counter(string_list)
#         max = 0
#         max_substring = list()
#         for i in range(len(string_list)):
#             substring = string_list[i: i+substring_length]
#             substring_count = 0
#             for char in substring:
#                 if count[char] > 1:
#                     substring_count += 1
#             if substring_count > max:
#                 max = substring_count
#                 max_substring = substring
#         return max_substring

#     B = least_unique(string_list, R)
#     for element in B:
#         if element in string_list:
#             string_list.remove(element)

#     return len(set(string_list))








# A = [1, 2, 3, 4, 5, 2, 3, 1, 4]
# R = 3
# result = solution(A, R)
# print(result)
# # Output: 5

# print(solution([2, 2, 3, 2, 2, 2], 3))




# def truckTour(petrolpumps):
#     n = len(petrolpumps)

#     start = 0
#     total_petrol = 0
#     current_petrol = 0

#     for i in range(n):
#         petrol, distance = petrolpumps[i]
#         total_petrol += petrol - distance
#         print('current_petrol', current_petrol)

#         if current_petrol < 0:
#             start = i
#             current_petrol = 0

#         current_petrol += petrol - distance

#     return start if total_petrol >= 0 else -1

# print(truckTour([[1, 5], [10, 3], [3, 4]]))


# from collections import deque
# def equalStacks(h1, h2, h3):
#     h1_queue = deque(h1)
#     h2_queue = deque(h2)
#     h3_queue = deque(h3)

#     h1_sum, h2_sum, h3_sum = sum(h1_queue), sum(h2_queue), sum(h3_queue)

#     while h1_queue and h2_queue and h3_queue:
#         min_sum = min(h1_sum, h2_sum, h3_sum)
#         print('min_sum', min_sum)

#         while h1_sum > min_sum:
#             h1_sum -= h1_queue.popleft()

#         while h2_sum > min_sum:
#             h2_sum -= h2_queue.popleft()

#         while h3_sum > min_sum:
#             h3_sum -= h3_queue.popleft()

#         if h1_sum == h2_sum == h3_sum:
#             return h1_sum

#     return 0


# h1 = [3, 2, 1, 1, 1]
# h2 = [4, 3, 2]
# h3 = [1, 1, 4, 1]
# print(equalStacks(h1, h2, h3))


# import math

# def maxSubarray(arr):
#     n = len(arr)
#     current_sum = 0
#     max_sum = -math.inf
#     max_positive_sum = 0

#     for i in range(n):
#         print('this is arr[i]', arr[i])
#         current_sum = max(arr[i], current_sum + arr[i])
#         print('this is current sum', current_sum)
#         max_sum = max(max_sum, current_sum)
#         print('this is max sum', max_sum)


#         if arr[i] > 0:
#             max_positive_sum += arr[i]
#             print('this is max positive sum', max_positive_sum)
#         print('-------------')

#     if max(arr) < 0:
#         max_positive_sum = max(arr)

#     return max_sum, max_positive_sum

# # arr1 = [1, 2, 3, 4]
# arr2 = [2, -3, 2, 3, 4, -5, 10]
# # arr3 = [-2, -3, -1, -4, -6]

# # print(maxSubarray(arr1))
# print(maxSubarray(arr2))
# # print(maxSubarray(arr3))


# import heapq

# def cookies(k, A):
#     heapq.heapify(A)
#     i = 0


#     while len(A) > 1 and A[0] < k:
#         first_num = heapq.heappop(A)
#         second_num = heapq.heappop(A)
#         new_num = first_num + 2 * second_num
#         heapq.heappush(A, new_num)
#         i += 1

#     if all(num >= k for num in A):
#         return i
#     else:
#         return -1



# k1 =  7
# A1 = [1, 2, 3, 9, 10, 12]

# print(cookies(k1, A1))
# def hackerlandRadioTransmitters(x, k):
#     transms=1
#     x.sort()
#     i=0
#     centerCandidatePos = x[i]+k
#     antennaPos = i
#     while i < len(x):
#         # print('x', x)
#         print('antennaPos', antennaPos)
#         print('centerCandidatePos', centerCandidatePos)
#         current = x[i]
#         print('current', x[i])
#         if current <= centerCandidatePos:
#             antennaPos = current
#         elif current > antennaPos+k:
#             centerCandidatePos = current+k
#             transms+=1
#         print('transms', transms)
#         print('--------')

#         i+=1

#     return transms


# x1 = [1, 2, 3, 4, 5]
# k1 = 1

# x2 = [7, 2, 4, 6, 5, 9, 12, 11]
# k2 = 2

# print(hackerlandRadioTransmitters(x1, k1))
# print(hackerlandRadioTransmitters(x2, k2))

#
# from collections import deque
# def solve(arr, queries):
#     result = []

#     for q in queries:
#         print('q', q)
#         min_among_max = max_val = max(arr[:q])
#         queue = deque(arr[:q])

#         i = q
#         while i < len(arr):
#             print('queue', queue)
#             num = arr[i]
#             print('num', num)
#             queue.append(num)
#             popped = queue.popleft()
#             print('popped', popped)

#             max_val = max(max_val, num) if popped < max_val else max(queue)
#             print('max val', max_val)
#             min_among_max = min(min_among_max, max_val)
#             print('min among max', min_among_max)
#             i += 1
#             print('-----------')
#         print('q stop -------')
#         result.append(min_among_max)
#     return result


# arr1 = [33, 11, 44, 11, 55]
# queries1 = [1, 2, 3, 4, 5]

# print(solve(arr1, queries1))


# def arrayManipulation(n, queries):
#     n_array = [0] * n
#     for query in queries:
#         first_index = query[0] - 1
#         second_index = query[1]
#         value = query[2]
#         for i in range(first_index, second_index):
#             n_array[i] += value

#     return max(n_array)




# def arrayManipulation(n, queries):
#     n_array = [0] * (n + 1)

#     for query in queries:
#         first_index = query[0] - 1
#         second_index = query[1]
#         value = query[2]

#         n_array[first_index] += value
#         n_array[second_index] -= value
#     max_value = 0
#     prefix_sum = 0

#     for i in range(n + 1):
#         prefix_sum += n_array[i]
#         max_value = max(max_value, prefix_sum)


#     return max_value



# from itertools import accumulate
# def arrayManipulation(n, queries):
#     deltas = [0] * (n+1)
#     for a, b, k in queries:
#         deltas[a-1] += k
#         deltas[b] -= k
#     return max(accumulate(deltas))


# queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# print(arrayManipulation(5, queries))


def highestValuePalindrome(s, n, k):
    if k > len(s):
        return '9' * len(s)

    min_changes_to_make_palindrome = 0
    arr = [int(c) for c in s]
    mid = len(arr) // 2

    marked = [False] * mid
    print('marked', marked)

    for i in range(mid):
        l = arr[i]
        r = arr[-(i+1)]
        max_val = max(l, r)
        if l != r:
            min_changes_to_make_palindrome += 1
            arr[i] = arr[-(i+1)] = max_val
            marked[i] = True

    if min_changes_to_make_palindrome > k:
        return '-1'

    changes_left = k - min_changes_to_make_palindrome
    for i in range(mid):
        if arr[i] == 9:
            continue

        change_required = 1 if marked[i] else 2
        if change_required <= changes_left:
            arr[i] = arr[-(i+1)] = 9
            changes_left -= change_required
        if changes_left == 0:
            break

    if changes_left == 1 and len(arr) % 2 != 0:
        arr[mid] = 9

    return "".join(str(i) for i in arr)


s1 = '3943'
n1 = 4
k1 = 1

s2 = '092282'
n2 = 6
k2 = 3

s3 = '0011'
n3 = 4
k3 = 1

print(highestValuePalindrome(s1, n1, k1))
print(highestValuePalindrome(s2, n2, k2))
print(highestValuePalindrome(s3, n3, k3))


