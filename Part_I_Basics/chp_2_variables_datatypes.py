#Variables
#Activity 2.1 on pg 56
simple_message = "I am doing the first offical activity on the 16th of Sep 2026"
print(simple_message)

#Activity 2.2 on pg 56
simple_message=("I am learning Python programming and I am enjoying it!")
print(simple_message)

#Strings
name = "ada lovelace"
print(name.title()) #title() - capitalizes the first letter of each word in a string
print(name.lower()) #lower() - converts all letters in a string to lowercase
print(name.upper()) #upper() - converts all letters in a string to uppercase

#Combining Strings
first_name = "ada"
last_name ="lovelace"
full_name = first_name + " " +last_name
print(full_name)

#Concanating Strings
print("Hello, " + full_name.title() + "!")
#store message in a variable
message = "Hello, " +full_name.title() +"!"
print(message)

#Adding Whitespace to Strings with Tabs 
print("Languages: \nPython \nC \nJavaScript") #\n - adds new line
print("Languages: \n\tPython \tC \tJavaScript") #\t - adds tab space"
print("Languages: \n\tPython \n\tC \n\tJavaScript") 

#Stripping Withespace
favorite_language = "python    " 
print(favorite_language)
print(favorite_language.rstrip()) #Revomes whitespace to the right
new_language = "   C++"
print(new_language)
print(new_language.lstrip()) #Removes whitespace to the left
new_language = new_language.strip() #Removes whitespace from both sides
print(new_language)
#Or you can assign the variable value back to the variable itself
#favorite_language = favorite_language.rstrip()

#Avoiding Syntax Errors with Strings
message = "One of Python's strengths is its diverse community."
print(message)

message = 'One of Python\'s strengths is its diverse community.' #This will give an error because of the single quote in Python's unless you use \'s
print(message)

#Activity 2.3 on pg 62
person_name = "Eric"
personal_message = "Hello, " + person_name + " would you like to learn python today?"
print(personal_message)

#Activity 2.5 on pg 62
person_name = "Albert Sobukwe"
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

#Activity 2.5 on pg 62
quote = '"A person who never made a mistake never tried anything new."'
print ("Albert Einsten once said, "  + quote )

#Activity 2.6 on pg 62
quote = '"A person who never made a mistake never tried anything new."'
famous_person = 'Albert Einstein'
print(famous_person + ' once said ' + quote)

#Activity 2.7 on pg 62
person_name = "  \n\t albert \t einstein  "
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

#Numbers
# + - Addition e.g 2 + 3 = 5
# - Subtraction e.g 5 - 2 = 3
# * Multiplication e.g 2 * 3 = 6
# / Division e.g 3 / 2 = 1.5
# ** Exponentiation e.g 3 ** 2 = 9
# Combination e.g 2 + 3 * 4 = 14 (Multiplication is done first before addition)
# Combination e.g (2 + 3) * 4 = 20 (Parenthesis is done first before multiplication)

#Floats - Numbers with decimal points e.g 0.1, 0.2, 0.3
# 0.1 + 0.1 = 0.2
# 2 * 0.1 = 0.2
# 2 * 0.2 = 0.4
#But 0.2 + 0.1 = 0.30000000000000004 (This is because of the way computers store floating point numbers)
# And 3 * 0.1 = 0.30000000000000004 (This is because of the way computers store floating point numbers)

#Multiple Assignment
x, y, z = 0, 0, 0
print(x)
print(y)
print(z)
print(x, y, z)

#Constants 
#Constants are variables that should not change throughout the program and should be written in all capital letters. Python does not have built-in constant types, but it is a convention to use all capital letters for constants.
MAX_CONNECTIONS = 5000

#Avoiding Type Errors with the str() Function
age = 23
#message = "Happy " + age + "rd Birthday!"
#print(message) - This will give an error because you cannot concatenate a string and an integer
message = "Happy " + str(age) + "rd Birthday!" #This will convert the integer to a string
print(message)

#Activity 2.8 on pg 66
print(5 +3)
print(12 -4)
print(4 *2)
print(16/2)

#Activity 2.9 on pg 66
favorite_number = 12
message = "My favorite  number is " + str(favorite_number) + "!"
print(message)

#Comments
# A comment is maade by placing a # before the comment. Comments are ignored by the python interpreter and are used to explain code to humans.

#Activity 2.10 on pg 66
# Answer - I have already commented on my code above. I have used comments to explain what each line of code does. 

#The Zen of Python
# Import allows us to import Python modules into our code. The Zen of Python is a collection of 19 guiding principles for writing computer programs in the Python language. It was written by Tim Peters and is included as an Easter egg in the Python interpreter. To access the Zen of Python, you can type "import this" in the Python interpreter.
import this
