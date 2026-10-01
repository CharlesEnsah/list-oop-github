students = ['The Lord','Alimu','Sharon']
print( f"My bestfriend's name is {students[0]}")
print( f"My classmate's name is {students[1]}")
print( f"My classmate's name is {students[2]}")


# Get the index of an item in a list
print(f'The index of The Lord is {students.index('The Lord')}')
print(f'The index of Sharon is {students.index('Sharon')}')

students.insert(3, "Donald")
Fruits = ["Grapes", "Strawberry"]
students.extend(Fruits)
print(students)
Fruits.remove("Grapes")
print(Fruits)
students.pop()
students.pop()
thirdItem = students.pop()
print(students)



