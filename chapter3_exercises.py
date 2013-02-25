# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Elizabeth Tenorio
print "Ex. 3.1. Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get."
'''
repeat_lyrics()
def print_lyrics(): 
    print "I'm a lumberjack, and I'm okay." 
    print "I sleep all night and I work all day."

def repeat_lyrics(): 
    print_lyrics() 
    print_lyrics()
'''
# Having the function call before the definitions results in 'NameError: name 'repeat_lyrics' is not defined'

print "Ex. 3.2. Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?"
'''
def repeat_lyrics(): 
    print_lyrics() 
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()
'''
# Changing the order of the functions does not negatively affect the script at all since they do not generate an output until 'repeat_lyrics' is called. 
# It has the same output as the original program. 

print "Ex. 3.3 Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display."
print ">>> right_justify('allen')"

def right_justify(s):
    padding = ' ' * (70 - len(s))
    print padding + s 

right_justify('allen')

#                                                                 allen

print "Ex. 3.4 A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:"
print "def do_twice(f):"
print "    f()"
print "    f()"

print "def print_spam():" 
print "    print 'spam'"
print
print "do_twice(print_spam)"

print "Here's an example that uses do_twice to call a function named print_spam twice."

print "def print_spam():" 
print "    print 'spam'"

print "do_twice(print_spam)"

print "1. Type this example into a script and test it."
def do_twice(f): 
    f()
    f()

def print_spam(): 
    print 'spam'

do_twice(print_spam)

# spam
# spam

print "2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument."
def do_twice(f, v): 
    f(v)
    f(v)

def print_spam(v): 
    print v   

do_twice(print_spam, 'spam')

# spam
# spam

print "3. Write a more general version of print_spam, called print_twice, that takes a string as a parameter and prints it twice."

def print_twice(s): 
    print s
    print s

print_twice('spam')
# spam
# spam

print "4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument."

def do_twice(f, v): 
    f(v)
    f(v)

def print_twice(v): 
    print v
    print v

do_twice(print_twice, 'spam')
# spam
# spam
# spam
# spam

print "5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four."

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

do_four(print_twice, 'spam') 
# spam
# spam
# spam
# spam
# spam
# spam
# spam
# spam

