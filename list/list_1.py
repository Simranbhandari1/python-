li = [34,67,12,1,78,8]
li.sort()
print(li) #sorts a list in-place (it changes the original list directly).
li.reverse()
print(li)#descending order
li.insert(1,5678) #insert element at 1 index
print(li)
li.append(148)#insert element at the end of the list 
print(li)
print(li.pop(4))#it deletes the element at particular index and return its value 
print(li)
print(li.remove(1))#it does not return any value
print(li)
li.pop()#removes last element from the list
"""
pop() : Removes and returns the element at the given index.

If no index is given, it removes the last element by default.

If the index is out of range → it raises an IndexError

remove(): Removes the first occurrence of the specified value.

If the value does not exist in the list → it raises a ValueError.

It does not return the removed value, only modifies the list.

"""
li.extend([4,5,4,4,6])
print(li)

print(li.count(4))#counts how many time number appears 

new_li = li.copy()#to create shallow copy

print(new_li)

li.clear()
print(li)
print(new_li)
"""
Method	Purpose
append()	Add one item at end
extend()	Add multiple items
insert()	Insert at index
remove()	Remove by value
pop()	Remove by index (returns value)
index()	Find index of a value
count()	Count occurrences
sort()	Sort list
reverse()	Reverse list
copy()	Copy list
clear()	Empty list

"""
