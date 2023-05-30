#code on how to use lists#
student =["jane","john","irene"]
#code on how to use sets#
cars ={"toyota","mazda","ford"}
#code on how to use tuples#
mytuple = ("apple", "banana", "cherry")
print(student)
print(cars)
print(mytuple)
print (type(student))
print (type(cars))
print (type(mytuple))

#code on how to use dictionaries#
thisdict =	{"brand": "Ford" ,
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964}
print(thisdict)

students=list(("one","two","three"))
print(students)

thislist = ["apple", "banana", "cherry","mango","plum","berries"]
if "orange" in thislist:
    print("yes, fruit in the list")
else:
    print("not in the list")
    thislist [4] ="melon"
    print(thislist)
    #adding melon to the list as item 4#
    thislist [1:4] =["kiwi"]
    print(thislist)
    #used to replace items 1 to 4 with kiwi#
    thislist.append("letuce")
    print(thislist)
    #used to add an item at the end of the list#

print(thislist[-1])
#prints item -1 which is the last item on the list#
print(thislist[1])
#prints second item on the list#
print(thislist[0])
#prints first item on the list#
print(thislist[2:5])
#prints items from index 2 to 5 but item index 5 is not displayed#
print(thislist[::])
#prints everything on the list#
print(thislist[:8])
#this line of code prints everything on the list when we use a number that is more than the list items provided#
