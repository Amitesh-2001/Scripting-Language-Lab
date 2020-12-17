a=["physics","mathematics","chemistry","biology"]

#Retreiving values in list
print("Set of values in the list:",a[2:3])

#Negative index
print("Negative index",a[-2])

#change list item
a[2]="english"
print("values in the list:",a)


#delete list item
del a[2]
print("values in the list:",a)

#insert value at particular index
a.insert(1,"social studies")
print("values in the list:",a)

#reverse values
a.reverse() #returns no values
print("reversed values in the list:",a)

#sorted values
a.sort() #returns no values
print("sorted values in the list:",a)
