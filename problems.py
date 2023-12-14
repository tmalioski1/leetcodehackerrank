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

from collections import deque
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

from collections import deque
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
def rightSideView(root):
     if not root:
            return []

     queue = deque()
     queue.append(root)
     right_list = []

     while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                    right_list.append(node.val)

            if node.left:
                    queue.append(node.left)
            if node.right:
                    queue.append(node.right)

     return right_list


def onesMinusZeros(grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        difference = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        row_ones = [0]*ROWS
        col_ones = [0]*COLS

        print(row_ones, col_ones)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_ones[r] += 1
                    col_ones[c] += 1

        for r in range(ROWS):
            for c in range(COLS):
                difference[r][c] = row_ones[r] + col_ones[c] - (ROWS-row_ones[r]) - (COLS-col_ones[c])

        return difference

print(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))
