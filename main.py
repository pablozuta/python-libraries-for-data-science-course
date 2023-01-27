import numpy as np
import random

# creation numpy array from a python list
print("creation numpy array from a python list")
a = np.array([1, 3, 4, 6, 66])
print(a)
print(a[2])
a2 = np.array([23, 7, 64, 87, 432])
print(a2) 
print(a2[2]) 
print("manual assigment of a value with the index")
# assigment
a[0] = 1008
print(a)
a2[0] = 3827
print(a2)
print("")

# setting the data type manually
print("setting data type manually")
b = np.array([2, 65, 432, 4211, 3], dtype='float32')
print(b)
b2 = np.array([24, 65, 78, 54], dtype='i4')
print(b2)
print("")


# create random values on numpy array , the 10 are the range and 6 the size of the array
random_values_array = np.random.randint(10, size=6)
random_values_array_dos = np.random.randint(1000, size=10)
print("this is a random filled values array", random_values_array)
print("this is a random filled values array", random_values_array_dos)
random_values_array_two = np.random.randint(100, size=234)
print("this is a BIG random filled values array", random_values_array_two)
print("")

# accesing a range between this array
print("accesing a range in the BIG array", random_values_array_two[0:29])
print("now a smaller range ", random_values_array_two[0:9])
print("another smaller range ", random_values_array_dos[0:9])
# if the range start is zero you can omit that value and use the :[any other number]
print(random_values_array[:2])
# accesing in steps from inicial value to the last on increments of 3
print("accesing in steps from inicial value to the last on increments of 3")
print(random_values_array_two[0::3])
print("")


# NumPy arrays can be explicitly multidimensional. 

# A list of lists in converted to a 2-dimensional array
print("")
print("A list of lists in converted to a 2-dimensional array")
original_list = [[1,2,3],[3,4,5],[6,7,8]]
two_dimensional_array = np.array(original_list)
print(two_dimensional_array)

# It's often more efficient, especially for large arrays, to create them yourself.

# An array of length 10, filled with 0
array_of_zeros = np.zeros(10, dtype=int)
print(array_of_zeros)

# An array of size 3x5 filled with 1.0 (float)
array_3x5_of_ones = np.ones((3, 5), dtype=float)
print(array_3x5_of_ones)
# An array of size 10x10 filled with 1 int
array_10x10_of_ones = np.ones((10, 10), dtype=int)
print(array_10x10_of_ones)
# An array of size 30x30 filled with 1 int
array_30x30_of_ones = np.ones((30, 30), dtype=int)
print(array_30x30_of_ones)
# changing one value inside this multidimensional array
array_30x30_of_ones[0, 1] = 2
print(array_30x30_of_ones)

# An array of size 3x5 filled with 3.14
array_full_with_3_14 = np.full((3,5), 3.14)
print(array_full_with_3_14)

# An array containing a linear sequence starting at 0 and 
# going up to 20, with steps of 2
linear_array_from_0_to_20_in_steps_of_two = np.arange(0, 20, 2)
print(linear_array_from_0_to_20_in_steps_of_two)

# An array of 5 numbers, linearly spaced between 0 and 1
array_of_five_numbers_linearly_spaced = np.linspace(0, 1, 5)
print(array_of_five_numbers_linearly_spaced)

# The identity matrix of size 3
identity_matrix_of_3 = np.eye(3)
print(identity_matrix_of_3)
# An identity matrix return a 2-D array with ones on the diagonal and zeros elsewhere!

# how many dimensions an array has
print("The number of dimensions are of:" , array_of_zeros.ndim)

# the dimension of a shape
print(array_3x5_of_ones.shape)

# the size of the array
print(array_full_with_3_14.size)

# the data type of the elements
print(array_full_with_3_14.dtype)

# You can concatenate (or join) two or more arrays:
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
array_concatenation = np.concatenate([x, y])
print(array_concatenation)

# Universal functions
print("a = ", a)
print("a + 5 = ", a + 5)
print("a - 5 = ", a - 5)
print("a * 5 = ", a * 5)
print("a / 5 = ", a / 5)

# apply functions on NumPy arrays :
print("Absolute value: ", np.abs(a))
print("Logarithm: ", np.log(np.abs(a)))

# boolean operations
xx = np.random.rand(3, 3)
print(x > 0.5)

# Often, when dealing with large amounts of data, the first thing to do 
# is to calculate statistics on these data
# such as the mean or standard deviation. NumPy has functions for this.
standard_deviation_random_array = np.random.random(100)
print("a random 100 value array", standard_deviation_random_array)

standard_value = np.sum(standard_deviation_random_array)
print(standard_value)

