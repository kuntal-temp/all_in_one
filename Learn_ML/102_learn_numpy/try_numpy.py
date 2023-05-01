import numpy as np

list_1D = [10, 20, 30, 40, 50, 60, 70, 80, 90]
list_2D = [
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80],
    [90, 100]
]
list_3D = [
    [
        [10, 20],
        [30, 40]
    ],
    [
        [50, 60],
        [70, 80]
    ]
]

# array
array_1D = np.array(list_1D, dtype='float')
print("1D array::\n", array_1D, "shape=", array_1D.shape, "ndim=", array_1D.ndim, "size=", array_1D.size, "dtype=", array_1D.dtype, "itemsize=", array_1D.itemsize)
array_2D= np.array(list_2D, dtype='complex')
print("2D array::\n", array_2D, "shape=", array_2D.shape, "ndim=", array_2D.ndim, "size=", array_2D.size, "dtype=", array_2D.dtype, "itemsize=", array_2D.itemsize)
array_3D= np.array(list_3D, dtype='int')
print("3D array::\n", array_3D, "shape=", array_3D.shape, "ndim=", array_3D.ndim, "size=", array_3D.size, "dtype=", array_3D.dtype, "itemsize=", array_3D.itemsize)

to_list = array_1D.tolist()
print("to_list::\n", to_list)

array_new = np.ndarray((2,), buffer=np.array([10,20,30,40]), offset=8, dtype='int')
print("array_new::", array_new)
array_new = np.ndarray((2,), buffer=np.array([10,20,30,40]), offset=16, dtype='int')
print("array_new::", array_new)

# shape, reshape, resize, ravel, flatten
array_100 = np.shape(array_2D)
print("shape::\n", array_100)

array_100 = array_1D.reshape((3, 3), order='c')
print("reshape[row major]::\n", array_100)

array_100 = array_1D.reshape((3, 3), order='f')
print("reshape[col major]::\n", array_100)

array_100 = array_2D.reshape(-1)
print("flattened array::\n", array_100)

array_100 = array_2D.ravel()
print("ravel::\n", array_100)

array_100 = array_2D.flatten(order='f')
print("flatten::\n", array_100)

array_new = np.zeros((3, 4, 5))
array_new_shape = np.moveaxis(array_new, 0, -1).shape
print("array_new_shape::", array_new_shape)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
output_0 = np.concatenate((a, b), axis=0)
print("output_0::", output_0)
output_0 = np.concatenate((a, b), axis=1)
print("output_0::", output_0)
output_0 = np.concatenate((a, b), axis=None)
print("output_0::", output_0)

# asarray
array_100 = np.asarray(array_1D, dtype='int').reshape((3,3), order='c')
print("asarray[order=[row major]]::\n", array_100)
array_100 = np.asarray(array_1D, dtype='int').reshape((3, 3), order='F')
print("asarray[order=[col major]::\n", array_100)

# arrange
''' do not touch upper limit '''
array_100 = np.arange(10)
print("arrange::\n", array_100)
array_100 = np.arange(10, 20, 2)
print("arrange[+ve]::\n", array_100)
array_100 = np.arange(20, 10, -2)
print("arrange[-ne]::\n", array_100)

# linspace
array_100 = np.linspace(10, 20, 2)
print("linspace::\n", array_100)
array_100 = np.linspace(10, 20, 5)
print("linspace::\n", array_100)
array_100 = np.linspace(10, 20, 10, dtype='int')
print("linspace::\n", array_100)
array_100 = np.linspace(10, 20, 20, dtype='float')
print("linspace::\n", array_100)

# logspace
array_100 = np.logspace(2.0, 3.0, num=4)
print("logspace::\n", array_100)

# zeros & zeros_like
array_100 = np.zeros(shape=(2, 4), dtype='int')
print("zeros::\n", array_100)
array_200 = np.zeros_like(array_100)
print("zeros_like::\n", array_200)
array_200 = np.zeros_like(array_100, shape=(4, 2), dtype='complex')
print("zeros_like::\n", array_200)

# ones & ones_like
array_100 = np.ones(shape=(2, 4), dtype='int')
print("ones::\n", array_100)
array_200 = np.ones_like(array_100)
print("ones_like::\n", array_200)

# empty & empty_like
array_100 = np.empty(shape=(2, 2), dtype='int')
print("empty::\n", array_100)
array_200 = np.empty_like(array_100)
print("empty_like::\n", array_200)

# eye
array_100 = np.eye(2, dtype='complex')
print("eye::\n", array_100)

# identity
array_100 = np.identity(2, dtype='complex')
print("identity::\n", array_100)

# transpose
array_100 = array_2D.T
print("transpose::\n", array_100)

# array_split
array_100 = np.arange(10, 20, 2)
array_100 = np.array_split(array_100, 3)
print("array_split::\n", array_100)

# trim_zeros
array_400 = np.array([0, 0, 1, 0, 5, 2, 0, 0, 4, 0, 0, 0])
array_400 = np.trim_zeros(array_400)
print("trim_zeros::\n", array_400)

# unique
array_400 = np.array([2, 1, 5, 4, 2, 5, 1, 4, 8])
array_400 = np.unique(array_400)
print("unique::\n", array_400)
array_400 = np.array(['a', 'b', 'b', 'c', 'a'])
array_400, indices = np.unique(array_400, return_index=True)
print("array_400, indices", array_400, indices)

# insert/delete
array_500 = np.arange(6).reshape((2, 3))
array_after_delete = np.delete(array_500, 5)
print("deleted_array::\n", array_after_delete)
array_after_insert = np.insert(array_500, obj=2, values=50, axis=0)
print("array_after_insert::[axis=0]\n", array_after_insert)
array_after_insert = np.insert(array_500, obj=2, values=50, axis=1)
print("array_after_insert::[axis=1]\n", array_after_insert)

# Binary operations
bwt_and= np.bitwise_and(13, 17)
binary_format = np.binary_repr(12)
left_sft = np.left_shift(5, 2)

# String operations
array_100 = np.array(["pythOn", "numPy", 55])
array_200 = np.array(["1", "2", "7"])
capitalize = np.char.capitalize(array_100)
print("capitalize:: ", capitalize)
lower = np.char.lower(array_100)
print("lower:: ", lower)
str_add = np.char.add(array_100, array_200)
print("str_add:: ", str_add)
str_multi = np.array(["a", "b", "c"])
str_multi = np.char.multiply(str_multi, 5)
print("str_multi:: ", str_multi)
str_multi = np.array(['a', 'b', 'c', 'd', 'e', 'f']).reshape((2, 3))
str_multi = np.char.multiply(str_multi, 5)
print("str_multi:: ", str_multi)
str_replace = np.array(["That is a mango", "Monkeys eat mangos"])
str_replace = np.char.replace(str_replace, 'mango', 'banana')
print("str_replace:: ", str_replace)

# Arithmetic Operations
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
add_ans = a+b   # np.add(a, b)
print(add_ans)
sub_ans = a-b   # np.subtract(a, b)
print(sub_ans)
sub_ans = a-b-1 # np.subtract(a, b, 1)
print(sub_ans)
mul_ans = a*b   # np.multiply(a, b)
print(mul_ans)
div_ans = a/b   # np.divide(a, b)
print(div_ans)
mod_ans = np.mod(a, b)
print(mod_ans)
rem_ans = np.remainder(a, b)
print(rem_ans)
pow_ans = np.power(a, b)
print(pow_ans)
mean_a = np.mean(a)
print(mean_a)
mean_b = np.average(b)
print(mean_b)
sum_a = np.sum(a)
print(sum_a)

# sort & filtering
array_700 = np.array([[1,4],[3,1]])
sorted_array = np.sort(array_700)
print("sorted_array::", sorted_array)
sorted_array = np.sort(array_700, axis=None)
print("sorted_array::", sorted_array)
sorted_array = np.sort(array_700, axis=0)
print("sorted_array::", sorted_array)
sorted_array = np.argsort(array_700, axis=None)
print("argsort_array::", sorted_array)
sorted_array = np.argmax(array_700, axis=None)
print("argmax_array::", sorted_array)

array_where = np.arange(10, 20, 2)
array_where = np.where(array_where > 15)
print("array_where::", array_where)
array_where = np.where(array_where == 15)
print("array_where::", array_where)

# stacking
np_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_0 = np.vstack([np_arr, np_arr])
print("output_0::\n", output_0)
output_0 = np.hstack([np_arr, np_arr])
print("output_0::\n", output_0)

# Loop & Iter
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("shape=", arr.shape)
for i in np.nditer(arr):
  print(i, end=", ")
for idx, i in np.ndenumerate(arr):
  print(idx, i)

# Random Useful
''' Datetime Support Functions '''
array_datetime = ['2002-10-27T04:30', '2002-10-27T05:30', '2002-10-27T06:30', '2002-10-27T07:30']
array_datetime = np.array(array_datetime, dtype='M8[m]')
array_datetime = np.datetime_as_string(array_datetime)
print("array_datetime::", array_datetime)

can_cast = np.can_cast(np.array(1000.0), np.float32)
print("can_cast::", can_cast)

non_zero_array = np.array([3, 0, 2, 19])
non_zero_array = np.nonzero(non_zero_array)
print("non_zero_array::", non_zero_array)

# Vectorization
def add(arr1, arr2):
    return (arr1 + arr2)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
vectorized_add = np.vectorize(add)
result = vectorized_add(arr1, arr2)
print(result)
