import numpy as np
#Numpy Notes
#----->>> 1. Definition of Numpy: 
# Numpy is python library providing support for large multi-dimensional arrays and matrices representations and lets perform various mathematical operations over them. 
# Arrays of np are ndarrays.

#----->>> 2. Advantages of Numpy
# 	a. Allow several mathematical 	operations over numpy arrays
# 	b. fatser execution time

#----->>> 3. import numpy as np is used to import the numpy lib in your programs

#----->>> 4. numpy is used to create numpy arrays which have less execution time and hence are efficient than other datatypes eg: list


#----->>> 5. to check execution time of any program
'''from time import process_time
# used to determine the starting point of execution and ending point of execution depending on the place it is used.
process_time() 
start_time= process_time()
print('Kaise ho sab!!')
end_time = process_time()
print(start_time - end_time)'''
# """this last instruction will return total time taken to execute print funtion printing Kaisi hai duniya"""




#----->>> 6. to create a numpy array, first import numpy
'''
# printing 100 numbers in a numpy array
np_array = np.array([i for i in range(100)])
print(np_array)'''



#----->>> 7. checking datatype of the numpy array
'''
array = np.array([1,2,3,4,5])
list = [1,2,3,4,5]

print(array)
print(type(array))

print(list)
print(type(list))'''



#----->>> 8. creating a multi-dimensional and checking its size using '.shape' attribute which is used to determine the dimensions of an array
a = np.array([1,2,3])
print(a)
print(a.shape)
b = np.array([(1,2,3,4),(4,5,6,7)])
print(b)
print(b.shape)
# here output for a is (3, ) representing 3 colums and for b is (2,4) since the first value represents 4 and second value represnts column
#use 'dtype' attribute to define datatype of the values being stored in the array
'''b = np.array([(1,2,3),(4,5,6)], dtype=bool)
print(b) '''



#----->>> 9. initial placeholders in numpy arrays
# A zero Matrix
'''array= np.zeros((2,3))
print(array)'''

# An ones matrix
'''array =np.ones((5,4))
print(array)'''

# A Full matrix
'''array =np.full((2,2), 5, dtype="bool")
print(array)'''

# An Identity matrix
'''array = np.eye(3, dtype="int")
print(array)'''

# create a numpy array with random values
'''array = np.random.random((2,3))
print(array)''' # this prints an array having values within a range of (0-1)

# creating a numpy array with random values within a specific range
'''array =np.random.randint(10,15,(3,5))
print (array)'''

# cretaing an array with evenly spaced values
'''array = np.linspace(1, 10, 7, dtype="int")
print(array)''' #programmer specifies the number of values you want in an array, specified after the range provided in the argument above
'''array = np.arange(1,10, 3)
print(array)''' #programmer specifies the space it needs to be present in the values being present in the arrays



# ----->>> 10. Convert a list into a numpy array
'''list1= [1,2,3,4,5,6]
print(list1)
print(type(list1))
array=np.asarray(list1)
print(array)
print(type(array))'''



# ----->>> 11. Analyzing a numpy array
'''array = np.random.randint(100,1000, (2,5))
print(array)
print(array.shape)
print(array.ndim)
print(array.size)
print(array.dtype)'''
     


# ----->>> Mathematical Operations

'''list1 =[1,2,3]
list2 =[4,5,6]
print(list1+list2)'''  # prints a list concatenated with both the given lists
# case is different for numpy arrays, as by adding 2 numpy arrays, it results into summation of values
array1= np.random.randint(10,30,(3,2))
#array2 = np.random.randint(10,35,(3,2))
print(array1)
#print(array2,"\n")
'''print(array1+array2)'''
# using arithmetic operators on arrays 
'''print(array1 + array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
'''
#rithmetical functions are again being used for numpy array mathematical operations
'''print(np.add(array1, array2))
print(np.subtract(array1, array2))
print(np.multiply(array1, array2))
print(np.divide(array1, array2))
'''


# ----->>> Array Manipulation
#transpose of a matrix
'''transpose_array = np.transpose(array1)    # using ' .transpose() ' function
print(transpose_array)
print(transpose_array.shape)
transpose_array2 = array1.T                  # using ' .T ' to transpose
print(transpose_array2)
print(transpose_array2.shape)'''
# Reshaping an array. It is different than transposing
'''print(array1.reshape(6,1))''' # can only reshape an array based on its size...eg: 3x2 can be reshaped into 2x3, 1x6, 6x1 only