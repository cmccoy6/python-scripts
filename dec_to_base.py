#!/usr/bin/python3

'''
Converts a user inputed decimal number to a number in a different base system. Prompts the user to choose the base system to convert to. 
'''

#Initialize number as empty string.
number = ""

'''
Run the program while number is still an empty string. Essentially this is a way of ending the program. Since there is a nested while loop
within this loop, it will check this condition only after the tempnumb is 0 and the output is complete.  
'''
while(not(number.isnumeric())):
    
    #Get the number from the user
    number = input("What is the decimal to convert? ")
    
    #Get the base from the user
    base = input("What base would you like to convert to? ")
    
    #Convert this number to an integer and save in variable tempnumb
    tempnumb = int(number)
    
    #Create a string of values which will be used to reference the apporpirate digit, even in number systems which extend beyond 10.
    values = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Initialize output variable to empty string
    output = ""
    
    '''
    Keep executing this while block as long as tempnumb is not greater than 0.
    This condition will be false once tempnumb is 1 / base (because any float will be rounded down), which will mean we have reached the leftmost digit. 
    '''
    while(tempnumb > 0):
        
        #create a variable for keeping track of the index. This will be used for referencing the values string. 
        index = tempnumb % int(base)
        
        #Show the division calculation for each iteration of the while loop. If the remainder is more than 9, show the corresponding letter value in parentheses. 
        if (index > 9):  
            print(tempnumb, "/", base,  "=", int(tempnumb / int(base)), "R", index, "(" + values[index] + ")")
        else:
            print(tempnumb, "/", base,  "=", int(tempnumb / int(base)), "R", index)
        
        #update output by prepending the remainder of tempnumb / base to the beginning of the string
        output = values[index] + output
        
        #update the tempnumb by dividing by base, thus moving one place to the left, or one exponential slot. 
        tempnumb = int(tempnumb / int(base))
    
    #print the base number equivilent of the user input number
    print(number, "in base", base, "is:", output)
    
