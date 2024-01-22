# # s = " ".join(["it", "is", "kind"])

# # print(s)

# # print(type(2.))


# ######### FILTER #################

# # Define a function to check
# # if a number is a multiple of 3
# def is_multiple_of_3(num):
#     return num % 3 == 0


# # Create a list of numbers to filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Use filter and a lambda function to
# # filter the list of numbers and only
# # keep the ones that are multiples of 3
# result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# # Print the result
# print(result)



# ######### MAP #################
# numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
# print(list(result))



# ######### SORTED #################
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"


# people = [
#     Person('John', 25),
#     Person('Alice', 18),
#     Person('Bob', 30)
# ]
# sorted_people = sorted(people, key=lambda x: x.age)
# print(sorted_people)


######### ZIP #################
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")

# x_dict = dict(zip(a, b))
# x_list = list(zip(a, b))
# x_tuple = tuple(zip(a, b))
# x_set = set(zip(a, b))

# print(x_dict)
# print('--------')
# print(x_list)
# print('--------')
# print(x_tuple)
# print('--------')
# print(x_set)


# new_tup = tuple((3, 5, 7))

# print(sum(new_tup))


######### ALL #################
# from collections import Counter
# def countCharacters(words, chars):
#         total = 0
#         count = Counter(chars)
#         print('count---', count)


#         for word in words:
#             word_count = Counter(word)
#             print('word_count---', word_count)

#             ###### ALL ######
#             if all(word_count[char] <= count[char] for char in word):
#                 total += len(word)


#         return total

# ######### ANY #################

arr1= [1,2,3]
arr1.pop()
print(arr1)
