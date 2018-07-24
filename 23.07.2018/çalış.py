
"""
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)


"""



########ornekk2######
"""
    input: two integer values
           lower limit 'start' and maximum 'end'
           the arguments aren't inclusive.
    output: if reading successful then returns the read integer. 
    purpose: reads from command-line a integer in the given bounds. 
             while input invalid asks user again
"""

loop=True

while(loop):

    try:
        # reads and convert the input from the console

        userInput= int(input("enter your choise:"))

        # check whether input is in the given bounds.


        if userInput > end or userInput < start:

            # error case

            print("the arguments aren't inclusive")


        else:

            # valid case
        loop=False  # aborts while-loop

    except ValueError:

        # error case

    print("please try again.only numbers")

    return userInput

x= get_user_input(1,6)

print(x)





















