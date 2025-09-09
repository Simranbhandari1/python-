#dictionary methods

marks = {
    "harry" : 100,
    "Subham" : 200,
    "Rohan" : 23,
    "li":[1,2,3,4],
    0:"hey"
    
}
print(marks.items()) #gives the dictory in the form of list and also the key valyue pair are returned in the form of tuple
#we can iterate over this using the for loop 
print(marks.keys()) #we get the list of the keys 
print(marks.values())#we get the list of the keys 
marks.update({"harry" : 99 , "Simran": 100})#iof any key is not prsent it will be inserted as a new key 
print(marks)
print(marks.get("harry2"))#prints none if key is not present
# print(marks["harry2"]) #it gives error if key is not prsent 

