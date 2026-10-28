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
#An error because print statement should be indented (under for loop)
#print(magians) 
 print(magicians) #Corrected! Print statemnt is indented after the for loop
