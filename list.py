# list1=["rohan",1,3,"rohan","apple"]
# print(list1)
# # No. of elements in list
# print(len(list1))
# List constructor
list2=list(("seven",6,5,"ABES"))# convert tupple into list
print(list2)
#Accessing the element 
print(list2[1])
print(list2[-1]) # print from back of list (ABES)
print(list2[-3:-1]) # print elements in certain range (6,5)

# To check presence of certain element in list
if"dev" in list2:
  print("yes")
else:
  print(" no ")
  
 # Modification of List 
list2[1]="Dev"
print(list2)
list2[0:2]=[7,"Lamborghini"]
print(list2)

# Inserting element in list (add the element at given position and shift all the element )
list2.insert(0,"Rishab") 
print(list2)

# Appending a element in list (add element at last position )
list2.append("World")
print(list2)

# Deleting a element from list
list2.remove("World")
print(list2)

list2.pop(2) # remove element using index (lamborghini deleted)
print(list2)