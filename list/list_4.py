#Tuple 
#tuples are immutable
empt_tuple=()
a=(1,2,3,4,5)
print(type(a))
#tuple with one element 
one_el=(1)
print(type(one_el)) #it will print as int
one_el=(1,)
print(type(one_el))#correct way to initialise tuple with single element
#a[0]=50 'tuple' object does not support item assignment
print(a)