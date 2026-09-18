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
print("The last motorcycle was a " + last_owned.title() + ".")

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

motorcycles.remove('ducati') #.remove() - removes an item by value
print(motorcycles)

#Use .remove() method to work with a value that's being removed from the list 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#Activity 3.4 on pg 79 
guest_list =['Bionelo' , 'Kamohelo' , 'Zonge' , 'Nosiphiwo' ]
print("Hello,  " + guest_list[0] + "! I would like to invite you to my dinner. ")
print("Hello,  " + guest_list[1] + "! I would like to invite you to my dinner. ")
print("Hello,  " + guest_list[2] + "! I would like to invite you to my dinner.")
print("Hello,  " + guest_list[3] + "! I would like to invite you to my dinner. ")

#Activity 3.5 on pg 79
print("Unfortunately,  " + guest_list[-1] + " won't make it to the dinner.")
del guest_list[3] #use .del to remove 'Nosiphiwo' from the list
print(guest_list)
guest_list.insert(3, 'Liyabona')#use .insert to add a new guest , 'Liyabona' to the list
print(guest_list)

#Or 
guest_list = [] #Create a new empty list 
guest_list.append('Bionelo') #Add guest names to your list
guest_list.append('Kamohelo')
guest_list.append('Zonge')
guest_list.append('Liyabona') #Replace 'Nosiphiwo' with 'Liyabona' on the last position
print(guest_list)

print("Hello, " + guest_list[0] + "! I would like to invite you to my diner.")
print("Hello, " + guest_list[1] + "! I would like to invite you to my diner.")
print("Hello, " + guest_list[2] + "! I would like to invite you to my diner.")
print("Hello, " + guest_list[3] + "! I would like to invite you to my diner.")

#Activity 3.6 on pg 79
guest_list = ['Boinelo' , 'Kamohelo' , 'Zonge' , 'Liyabona']
print("Hi, again, " + guest_list[0] + ". I have found a bigger table.")
print("Hi, again, " + guest_list[1] + ". I have found a bigger table.")
print("Hi, again, " + guest_list[2] + ". I have found a bigger table.")
print("Hi, again, " + guest_list[3] + ". I have found a bigger table.")

guest_list.insert(0, 'Unathi') #add new gust at the beiginning of the list 
guest_list.insert(2, 'Rele') #add new guest in the middle of the list
guest_list.append('Lisakhanya') #add new guest at the end of the list 

print(guest_list)
print("Hey, " + guest_list[0] + "! You are kindly invisted to my diner at Spur, at 18:00pm.")
print("Hey, " + guest_list[1] + "! You are kindly invisted to my diner at Spur, at 18:00pm.")
print("Hey, " + guest_list[2] + "! You are kindly invisted to my diner at Spur, at 18:00pm.")
print("Hey, " + guest_list[3] + "! You are kindly invisted to my diner at Spur, at 18:00pm.")
print("Hey, " + guest_list[4] + "! You are kindly invisted to my diner at Spur, at 18:00pm.")
print("Hey, " + guest_list[5] + "! You are kindly invisted to my diner at Spur, at 18:00pm.")
print("Hey, " + guest_list[6] + "! You are kindly invisted to my diner at Spur, at 18:00pm.")

#Activity 3.7 on pg 80
guest_list = ['unathi' , 'Boinelo' , 'Rele' , 'Kamohelo' , 'Zonge' , 'Liyabona' , 'Lisakhanya'] #print new guest list will all guests
print("\nI can only invite 2 guests to my dinner, the new dinner table won't arrive in time at 18:00pm.")
new_list = guest_list.pop() #Get a new list and remove guests from old list using pop

print("\nI am sorry, " + new_list + " the chosen dinner table won't arrive at 18:00pm. I can only invite 2 guests. Please do not come anymore")
new_list = guest_list.pop()
print("\nI am sorry, " + new_list + " the chosen dinner table won't arrive at 18:00pm. I can only invite 2 guests. Please do not come anymore")#Print message to removed guests

new_list = guest_list.pop()
print("\nI am sorry, " + new_list + " the chosen dinner table won't arrive at 18:00pm. I can only invite 2 guests. Please do not come anymore")

new_list = guest_list.pop()
print("\nI am sorry, " + new_list + " the chosen dinner table won't arrive at 18:00pm. I can only invite 2 guests. Please do not come anymore")

new_list = guest_list.pop()
print("\nI am sorry, " + new_list + " the chosen dinner table won't arrive at 18:00pm. I can only invite 2 guests. Please do not come anymore")

print("Hey, " + guest_list[0] + "! You are still invited, see you at Spur at 18:00pm.")
print("Hey, " + guest_list[1] + "! You are still invited, see you at Spur at 18:00pm.")

#Print the list to ensure only 2 guests are left from it
print(guest_list)
#You can delete is one by one
del guest_list[0] #delete first guest
print(guest_list)
del guest_list[0]#The last guest'Boinelo' now is the first guest with 'Unathi' out 
print(guest_list)


#Organising a List 
# Sorting a List Permanently with theh sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #Sorts list in an alphabetical order
print(cars)

#Sorting list in reverse alphabetical oder
cars.sort(reverse=True)
print(cars)

#Sorting a List Temporarily with the sorted() Function
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#Printing a List in Reverse Order
print(cars)
cars.reverse() #Reverses the list not alphabetically though
print(cars)

#Finding the Length of a list 
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)


#Activity 3.8 on pg 83
places = ['Dubai' , 'Paris' , 'Cape Town' , 'Victoria Falls' , 'Spain']
print(places)

#Use sorted() to print your list in alphabetical order without modifying the actual list
places.sort()
print(places)

#Use sorted() to print your list in reverse alphabetical order without changing the order oif the original list
places.sort(reverse=True)
print(places)

#Use reverse() to change the order of your list . Print the list to show that its order has changed
places.reverse()
print(places)

#Use reverse() to change the order of your list again . Print the list to show it’s back to its original order
places.reverse()
print(places)

#Use sort() to change your list so it’s stored in alphabetical order . Print the to show that its order has been changed
places.sort()
print(places)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has cxhanged
places.sort(reverse=True)
print(places)

#Activity 3.9 on pg 83
guest_list = ['unathi' , 'Boinelo' , 'Rele' , 'Kamohelo' , 'Zonge' , 'Liyabona' , 'Lisakhanya'] #print new guest list will all guests
print(len(guest_list))

#Activity 3.10 on pg 83
colors =['pink' , 'blue' , 'yellow' , 'green' , 'black'] #creating a list 
print(colors[0]) #printing an item in a list in a specific position
print(colors[-1]) #Index positions
colors[0] = 'white'
print(colors)
colors.append('purple') #appending elements to the end of the list
print(colors)
colors.insert(0, 'grey') #insterting an item from a list in a certain position 
print(colors)
del colors[0] #removing an item from a list at a certain position usimg del method
print(colors)
popped_colors = colors.pop() #removing an item from a list using pop() method 
print(colors)
print(popped_colors) 
bright_color = 'yellow'
colors.remove(bright_color) #removing item by value
print(colors)
colors.sort() #sorting list permanently with sort() method
print(colors)
colors.sort(reverse=True) #reverse list in alphhabetal order
print(colors)
colors.reverse() #printing list in reverse
print(colors)
len(colors) #Finding length of the list


#Avoiding Index Errors When Working with Lists
#If an index error occurs and you can’t figure out how to resolve it, try printing your 
#list or just printing the length of your list. Your list might look much different than 
#you thought it did, especially if it has been managed dynamically by your program. 
#Seeing the actual list, or the exact number of items in your list, can help you sort out 
#such logical errors