# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Elizabeth Tenorio
print "Ex. 2.1: Display the values of 01, 010, 0100 and 01000."
print 01
print 010
print 0100
print 01000
# 1
# 8
# 64
# 512
# The unusual results show up that way because a number that starts with zero is interpreted as octal, or base 8 number system. 
# Interpreting an invalid octal number such as 9 results in an error."

print "Exercise 2.2. Type the following statements in the Python interpreter to see what they do:"
print "5   #=> returns 5" 
print "x=5 #=> assigns 5 to variable x then returns nothing"
print "x+1 #=> returns 6"
 
print "Now put the same statements into a script and run it. What is the output?" 
# Putting the statements above into a script and running it performs the specified calculations but outputs nothing on the screen since a command to print it was not in the script.

print "Modify the script by transforming each expression into a print statement and then run it again."
# Transforming each expression into a print statement outputs  
# 5
# 6

print "Ex. 2.3 Assume that we execute the following assignment statements:"
print "width = 17"
print "height = 12.0" 
print "delimiter = '.'"
print "For each of the following expressions, write the value of the expression and the type of the expression."
print "1. width/2       #=> value is '8' and type is 'int'"
print "2. width/2.0     #=> value is '8.5' and type is 'float'"
print "3. height/3      #=> value is '4.0' and type is 'float'"
print "4. 1 + 2 * 5     #=> value is '11' and type is 'int'"
print "5. delimiter * 5 #=> value is '.....' and type is 'str'"

print "Ex.2.4. Practice using the Python interpreter as a calculator:"
print "1. The volume of a sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!"
radius = 5
radius_cubed = radius ** 3 
print "(4.0/3.0) * pi * (5**3)) #=> ",
from math import pi
volume_of_sphere = (4.0/3.0 * pi * (radius_cubed))
print volume_of_sphere
# Volume of sphere is 523.598775598

print "2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?"
cover_price = 24.95
discount = 0.4
shipping_first = 3.00
shipping_additional = 0.75
copies = 60
total_wholesale_cost = ((cover_price * (1 - discount)) * copies) + shipping_first + (shipping_additional * (copies - 1))
print "Total wholesale cost is $%.2f" % (total_wholesale_cost)
# Total wholesale cost is $945.45

print "3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?"
departure_hour = 6
departure_minute = 52
easy_pace = 8*60 + 15 #number of seconds
tempo_pace = 7*60 + 12 #number of seconds
leg1 = 1 * easy_pace 
leg2 = 3 * tempo_pace
leg3 = 1 * easy_pace
total_time = leg1 + leg2 + leg3
total_hour = total_time / 3600
total_minute = total_time / 60
total_hour = total_minute / 60
arrival_hour = departure_hour + total_hour
arrival_minute = departure_minute + total_minute
if arrival_minute > 60:
    arrival_hour = arrival_hour + arrival_minute / 60 
    arrival_minute = arrival_minute - 60
print "Arrival time is %d:%d am" % (arrival_hour, arrival_minute)
# Total run time in seconds is 2286 seconds
# Total run time is 0 hour, 38 minutes, 6 seconds
# Breakfast time is 7:30 am
