#Looping Trough an Entire List
magicians = ['alice', 'david', 'carolina'] #Define alist
for magician in magicians:#Define the loop to pull a name from the magicians and dtore it in a variable
 #print(magician) #For every magician in the list of magicians, print the magician’s name.
 print(magician.title() + ", that was great trick!") #TIP - when printing the result of a loot add a space before print to avaid error
 print ("I can't wait to see your next trick, " + magician.title() + ".\n" ) #\n inserts a blank line after each pass through the loop, we indent both print statements.
print ("Thank you, everyone. That was a great magic show!") #Only printed once because it is not directed to each magician (not indented) like the first 2 print statements and not printed under the for loop

#Avoiding Indentation Errors

#1. Forgetting to indent 
#-Always indent the line after the for statement in  loop. You forget, phython reminds you by returning an error
second_magicians = ['asanda' , 'ayanda' , 'ayakha']
for second_magician in second_magicians:
 print(second_magicians) #Print statemnt is indented after the for loop to make it part of the loop, if not indented it will return an error


#Forgetting to Indent Additional Lines
#NB  Sometimes your loop will run without any errors but won’t produce the 
#expected result. This can happen when you’re trying to do several tasks in 
#a loop and you forget to indent some of its lines.

clowns = ['bozo', 'pennywise', 'ronald']
for clown in clowns:
 print(clown.title() + ", that was a great tick!") #Indent this print statement, it's after a loop, make it a part of the loop 
print("I can't wait to see your next trick, " + clown.title() + ".\n") #No need to indent this print statement, it's not after a loop 
#This is a logical error, the syntax is correct but the result is not what you expected. The first print statement is indented, so it runs once for each clown in the list. The second print statement is not indented, so it runs only once after the loop has finished running. 
#Because the variable clown is still defined after the loop ends, this line of code runs without error, but it uses only the last value assigned to clown in the loop.
#To print the last message to every clown, you need to indent the second print statement so it runs once for each clown in the list.


#Indenting Unneccessarily 
#when you indent a line that doesn'nt need to be indented, python will correct you, for example:
message = "Hello Python World!"
 #print(message) - returns IndentationError: unexpected indent

#Indenting Unnecessarily After the Loop
#Shoulld you accidentallt indent code that should run fter a loop has finished, the code will be repeated once for each item on th list 
#Python may(sometimes) report the error but often times you'll get a simle logical error, for example:
tricksters = ['alice' , 'david' , 'carolina']
for trickster in tricksters:
 print(trickster.title() + ", that was a great trick! ")
 print("I can't wait to see your next trick, " + trickster.title() + ".\n")
 print("Thank you everyone, that was a great show!")
#Here, the last print statement is indented, so it runs once for each trickster in the list. The result is that the thank-you message is printed three times, once for each trickster in a new line.
#To fix this, you need to unindent the last print statement so it runs only once after the loop has finished. 


#Forgetting the Colon
#NB The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.
#Forgetting the colon at the end of a for statement will cause an error, for example:
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: #Remove this colon here to get the error - indentationerror: expected an indented block
    print(magician)


#Activity 4 on pg 93 (pg 60 on hard copy textbook)
#4-1. Pizzas
pizzas = ['pineapple' , 'chicken' , 'mushroom' , 'bbq' ]
for pizza in pizzas: 
  print("I like " +  pizza.title() + " pizza.")
print("I really love pizza!" + "\n") 

#4-2. Animals
cats = ['tiger' , 'leopard' , 'cheetah' , 'jaguar']
for cat in cats:
  print("A " + cat.title() + " is mejestic animal." )
print("Each of the cats are wild powerful cats." + "\n")


#Making Numerical Lists
#Using the range() Function
#The range() function makes it easy to generate a series of numbers. For example, the
for value in range(1,5): #The range() function starts at 1 and stops before 5, so it returns the values 1, 2, 3, and 4. 
 print(value) #Prints the values in the range. This is an example of the off-by-one behavior of Python’s range() function. The function stops one number before the second number you specify.

#Using range() to Make a List of Numbers
#You can use the list() function to convert the results of range() into a list. For example:
second_numbers = list(range(1,6)) #The range() function starts at 1 and stops before 6, so it returns the values 1, 2, 3, 4, and 5. The list() function takes these values and stores them in a list called numbers.
print(second_numbers) #Prints the list of numbers

#You can use this to skip numbers in a given range by specifying a third argument, called a step size, that determines the increament between each number in the sequence. For example:
even_numbers = list(range(2, 11 , 2)) #The range() function starts at 2 and stops before 11, so it returns the values 2, 4, 6, 8, and 10. The list starts at 2, stops before 11 and increases by 2 hence 2, 11, 2 - start, stop, step
print(even_numbers) #Prints the list of even numbers

#Own example:
factors_of_3 = list(range(3, 22, 3)) #start at 3, stop before 22 and increase by 3 hence 3, 22, 3 - start, stop, step
print(factors_of_3) #Prints the list of factors of 3

#You can make a list of the the first 10 square number, square of each integer from 1-10. Like this:
squares = [ ] #Start with an empty list  
for value in range(1,11): # For loop from value 1 to 10
    square = value**2 #You therefore square each number/value to the power of 2
    squares.append(square) #Each new value of the square is apppend to the list squares 
    #In simple terms: squares.append(value**2) #You can also do this in one line, without the need for the variable square
print(squares) # Print the squared answers


#Simple Statistics with a List of Numbers
#A few Python functions are specific to lists of numbers. For example, you 
#can easily find the minimum, maximum, and sum of a list of numbers:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) #Prints the minimum value in the list
print(max(digits)) #Prints the maximum value in the list
print(sum(digits)) #Prints the sum of all the values in the list


#List Comprehensions
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. 
squares = [value**2 for value in range(1,11)] #This line of code does the same thing as the previous example that used a for loop to generate a list of squares.
#list, value**2, for loop, range(1,11) - all in one line
print(squares) #Prints the list of squares

#Activity 4 on page 97 (pg 64 on hard copy textbook)
#4-3. Counting to Twenty
counting_to_20 = list(range(1,21))
for counting_to_20 in counting_to_20:
  print(counting_to_20)

#4-4. One Million
numbers = list(range(1,10000001))
for number in numbers:
  print(number)

#4-5. Summing a Million
numbers_to_million = list(range(1, 1000001))
print(min(numbers_to_million))
print(max(numbers_to_million))
print(sum(numbers_to_million))

#4-6. Odd Numbers
odd_numbers = list(range(3, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)

#4.7 Threes
threes = list(range(3, 31, 3))
for three in threes:
  print(three)

#Cubes
cubes = []
for value in range(1, 10):
  cube = value**3
  cubes.append(cube)
  print(cube)


#4-9. Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
