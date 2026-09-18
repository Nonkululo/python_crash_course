#A list is a collection of items in a particular order. 
bicycles =['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing Elemnts in a List
print(bicycles[0]) #prints the first item in the list
print(bicycles[0].title()) #prints the first item in the list with the first letter capitalized

#Indx Positions Start at 0 not 1 
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) #prints the last item in the list

#Using Individual Values from a List
message = "My First bicycle was a " + bicycles[0].title() + ". "
print(message)

# Activity 3.1 on pg 73 
names = ['Salina' , 'Lubabalo' , 'Asanda' , 'Kwanele' , 'Sindiswa']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#Activity 3.2 on pg 73
greetings =  "Hello, " + names[0] + "! How are you?" 
print(greetings)

greetings2 = "Hello, " + names[1] + "! How are you?"
print(greetings2)

greetings3 = "Hello, " + names[2] + "! How are you?"
print(greetings3)

greetings4 = "Hello, " + names[3] + "! How are you?"
print(greetings4)

greetings5 = "Hello, " + names[4] + "! How are you?"
print(greetings5)

#Activity 3.3 on pg 73
transportation = ['Car', 'Airplane' , 'Train' , 'Bus' , 'Bicycle' , 'Skateboard' ]
message = "I would absolutely love to learn and buy a " + transportation[-1] + "."
print(message)

#Modifying Elements in a List 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements to a List
motorcycles.append('ducati') #.append() - adds an item to the end of th list 
print(motorcycles)

# Append on an empty list
motorcycles = [] #creates an empty list
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting Elements into a List
motorcycles.insert(0, 'Toyota') #.insert() - adds an item at a specific position in the list
print(motorcycles)

#Removing Elements from a List using the del Statement
motorcycles = ['bmw' , 'mercedes' , 'audi' , 'suzuki']
print(motorcycles)
del motorcycles[0] #removes the first item in the list
print(motorcycles)

del motorcycles[-1]
print(motorcycles)

#Removing an Item Using the pop() Method     
# The pop() method removes the last item in a list, but it lets you work with that item after removing it.
motorcycles =['nyathi' , 'quantunm' , 'ntambai' , 'iveco']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles =['nyathi' , 'quantunm' , 'ntambai' , 'iveco']
last_owned = motorcycles.pop()
print("The last motorcycle was a " +last_owned.title() + ".")

