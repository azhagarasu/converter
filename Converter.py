#OM
#Number System Conversion
#Getting the decimal input from user
print('***Number system converter***\n\n')
a = int(input('Enter the decimal number: ')) #User entered value is stored in a

print('\n')

#input from user on the type of operation
i = str(input('What would you like to do? \n\n Enter Binary for converting the entered value to Binary \n\n \
Enter Octal for converting the entered value to Octal \n\n Enter Hex for convering the entered value to Hexadecimal \n\n Enter \
Unicode for convering the entered value to its equivalent Unicode value \n\n Enter the desired conversion operation : '))

#Converting the inputed text to lower case so that it can be compared in if else loop
i = i.lower()

print('\n')
print('You have entered', i)
print('\n')

#Created a loop to select the type of operation which the user would want
if i == 'binary':
    #Converting the input number to binary
    binary = "{0:b}".format(a)
    print('\n\nThe binary value of', a, 'is:', binary)
elif i == 'octal':
    #Converting the input number to octal
    octal = "{0:o}".format(a)
    print('The octal value of', a, 'is:', octal)
elif i == 'hex':
    #Converting the input number to hexadecimal
    hexdec = "{0:x}".format(a)
    print('The hexadecimal value of', a, 'is:', hexdec)
elif i == 'unicode':
    #Converting the input number to unicode character
    unicode = "{0:c}".format(a)
    print('The unicode value of', a, 'is:', unicode)
else:
    print('Entered value is incorrect. Please type binary or octal or hex or unicode.')

print('\n\n')
