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