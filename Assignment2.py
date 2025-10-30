# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    list = set(numbers) # Order doesn't matter; need to make list items unique.
    
    max1 = max(list)

    list.remove(max1)

    if len(list) >= 2:
        max2 = max(list)

    else:
        max2 = None

    return (max1, max2)

# print(max_two_in_list([5]))

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    list = sorted(set(numbers))

    return list

# print(remove_duplicates_and_sort([3, 1, 2, 3, 1]))

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    sum = 0

    for i in arr:
        sum += i
        result.append(sum)

    return result

# print(cumulative_sum([1, 2, 3, 4]))

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [[]]

# print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(list, step):
    new_list = list[0: (len(list)): step]

    return new_list

# print(slice_every_nth([10, 20, 30, 40, 50], 3))

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    if len(list1) != len(list2):
        result = "The two lists are not of the same length."

    else:
        result = [a * b for a, b in zip(list1, list2)]
        result = sum(result)

    return result

print(dot_product([2, 3, 4], [5, 6, 7]))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    return [[0, 0], [0, 0]]