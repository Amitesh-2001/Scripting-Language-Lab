d={1:'Amazon',2:'Flipkart',3:'Snapdeal',4:'Myntra'}
#Print all values
print(d)
#Retrieving values
print(d[1])
#Deleting a key-value pair
del d[4]
print(d)

#Get the key-value pairs as list
print("List of key value pairs",d.items())


#Get list of keys
print("List of keys",d.keys())

#Get list of values
print("List of values",d.values())


#Shallow copy of dictionary

print("Shallow copy of dictionary d",d.copy())


#Clear all entries of a dictionary
d.clear()
print("Trying to print a dictionary",d)
