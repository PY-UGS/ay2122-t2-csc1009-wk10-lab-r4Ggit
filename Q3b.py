def selection(case):
    switcher = {
        "CSC1006": 'Mathematics 2',
        "CSC1007": 'Operating Systems',
        "CSC1008": 'Data structures and Algorithms',
        "CSC1009": 'Object-Oriented Programming',
        "CSC1010": 'Computer Networking',
    }
    return switcher.get(case, "Unknown Module Code")
def forLoop():
    for x in range(102, 66, -1):  # For loop from 102 to 66 with decrement -1
        if x % 2 != 0:            # If I divide by 2 and remainder is not 0, print i
            print('Value of x is: ' + str(x))
            print()

if __name__ == "__main__":
	module = input('Enter module code: ')  # user input
	print(selection(module))  # prints out option
	forLoop() # call function for loop

