#Remove List Items
NewList = ["Anzim","Tasrif","Tutul",420]
NewList.remove(420)
print(NewList)

#The pop() method removes the specified index.

NewList.pop(2)
print(NewList)

#The del keyword also removes the specified index:

del NewList[1]

print(NewList)

#Clear the List
NewList.clear()

print(NewList)