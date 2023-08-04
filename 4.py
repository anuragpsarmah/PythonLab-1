#SET PROBLEM

'''
INSIGTHS
Boolean value is not counted as a part of the set
The pop() randomly removes any element in a set and also returns the same.
Then discard() removes a particular element from the set and doesnt give any error is element not found
The clear() deletes all elements of the set and makes it empty
del deletes the set from memory and can't be accessed any further
'''

myset = {'Anurag', 1, 3.5, True, 5}

print(myset) 

myset.pop()
print(myset) 

myset.discard('Anurag')
print(myset) 

myset.clear()
print(myset) 

del myset
print(myset) 
