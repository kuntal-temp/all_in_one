# There are several important differences between NumPy arrays and the standard Python sequences
 - NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.
 - The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.

The main difference is that the array_split() allows sections to be an integer which does not result in equal array division.








