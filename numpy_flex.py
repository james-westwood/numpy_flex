import numpy as np
# Q. 11. Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.intersect1d(a,b)
# print(c)
# 12. How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
c = np.setdiff1d(a,b)
# print(c)
# 13. How to get the positions where elements of two arrays match?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
# print(np.where(a==b))
# 14. How to extract all numbers between a given range from a numpy array?
# Q. Get all items between 5 and 10 from a
a = np.array([2, 6, 1, 9, 10, 3, 27])
# method 1
print(a[(a >= 5) & (a <= 10)])
# method 2
mask = np.where((a>=5) & (a<=10))
print(a[mask])
# method 3
truthy_mask = np.logical_and(a>=5, a<=10)
index_mask = np.where(truthy_mask)
print(a[index_mask])
# 15. How to make a python function that handles scalars to work on numpy arrays?
# Q. Convert the function maxx that works on two scalars, to work on two arrays.
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
def pair_max(arr_a, arr_b):
    res = np.empty_like(arr_a)
    for i, (a, b) in enumerate(zip(arr_a, arr_b)):
        if a >= b:
            res[i] = a
        else:
            res[i] = b
    return res
print(pair_max(a, b))
# using the vectorize method
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y
pair_max = np.vectorize(maxx, otypes=[int])
print(pair_max(a, b))
# 16. How to swap two columns in a 2d numpy array?
# Q. Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3,3)
print(arr)
swapped_arr = np.empty_like(arr)
swapped_arr[:,0] = arr[:,0]
swapped_arr[:,1] = arr[:,2]
swapped_arr[:,2] = arr[:,1]
print(swapped_arr)
# better method
swapped_arr = arr[:, [0,2,1]]
print(swapped_arr)
# 17. How to swap two rows in a 2d numpy array?
# Q. Swap rows 1 and 2 in the array arr:
arr = np.arange(9).reshape(3,3)
swapped_arr = arr[[0,2,1],:]
print(swapped_arr)
# 18. How to reverse the rows of a 2D array?
# Q. Reverse the rows of a 2D array arr.
# Input
arr = np.arange(9).reshape(3,3)
print(arr)
reversed_rows_arr = arr[[2,1,0],:]
print(reversed_rows_arr)
# better method, using arr[start:stop:step]
arr = np.arange(9).reshape(3,3)
reversed_rows_arr = arr[::-1]
print(reversed_rows_arr)
# 20. How to create a 2D array containing random floats between 5 and 10?
# Q. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.

arr = np.random.uniform(low=5, high=11, size=(5,3))
print(arr) 
print(arr)


# 21. How to print only 3 decimal places in python numpy array?
# Q. Print or show only 3 decimal places of the numpy array rand_arr.

rand_arr = np.random.random((5,3))

# solution, use: numpy.set_printoptions(precision=None...) 
# #from https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.set_printoptions.html

np.set_printoptions(precision=3)
print(rand_arr)

# 22. How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
# Q. Pretty print rand_arr by suppressing the scientific notation (like 1e10)

# Create the random array
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3

# Desired Output (similar to):
#> array([[ 0.000543,  0.000278,  0.000425],
#>        [ 0.000845,  0.000005,  0.000122],
#>        [ 0.000671,  0.000826,  0.000137]])
Define branch protection rules to disable force pushing, prevent branches from being deleted, and optionally require status checks before merging. New to branch protection rules? Learn more.
np.set_printoptions(suppress=True)
print(rand_arr)

# 23. How to limit the number of items printed in output of numpy array?
# Q. Limit the number of items printed in python numpy array a to a maximum of 6 elements.

a = np.arange(15)
#> array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
# Desired Output:
#> array([ 0,  1,  2, ..., 12, 13, 14])

np.set_printoptions(threshold=6)
print(a)

# 24. How to print the full numpy array without truncating
# Q. Print the full numpy array a without truncating.

# Input:


a = np.arange(15)
np.set_printoptions(threshold=sys.maxsize)
print(a)
#> array([ 0,  1,  2, ..., 12, 13, 14])


# 25. How to import a dataset with numbers and texts keeping the text intact in python numpy?
# Q. Import the iris dataset keeping the text intact.

import requests
import io

link = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

response = requests.get(link, verify=False)
response.raise_for_status()
data = np.load(io.BytesIO(response.content))  # Works!

# data = np.loadtxt(link)

print(data)
# Not sure if this one is working because I can't run it on ONS work machine

# LOOKS LIKE np.genfromtxt() would have been a better solution

# 26. How to extract a particular column from 1D array of tuples?
# Q. Extract the text column species from the 1D iris imported in previous question.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)

text_col = np.array([row[4] for row in iris_1d])

# 27. How to convert a 1d array of tuples to a 2d numpy array?
# Q. Convert the 1D iris to 2D array iris_2d by omitting the species text field.

# running iris_1d.dtype.names gives us the col names
# The names can be used to access items in the np.void (like a tuple)

# HACKY AS HELL solution using nested list comprehension and unpacking the list of voids
iris_2d = np.array([[*void[['f0', 'f1', 'f2', 'f3']]] for void in iris_1d])

# Given solution using .tolist() method on the np.voids

iris_2d = np.array([row.tolist()[:4] for row in iris_1d])