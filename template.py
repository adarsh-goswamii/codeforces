import math
import sys
import traceback
 
# global variable
INT_MAX = 2147483647
INT_MIN = -2147483648
 
# Function to solve the problem
def solve():
    # your code goes here.  
 
# helper functions goes here
def getInputs(num_inputs, type):
    # Reading space-separated inputs
    inputs = input().split()
 
    # Truncate or repeat inputs to match the desired number of inputs
    inputs = inputs[:num_inputs]
 
    # Convert inputs to the desired data type if needed
    inputs = list(map(type, inputs))  # Convert inputs to integers
 
    return inputs
 
 
def printYesOrNo(bool):
    print('YES' if bool else "NO")
 
 
# Main function to handle input/output
def main():
    # Check if running locally
    if sys.platform != 'win32':
        print(sys.platform)
        sys.stdin = open("./input.txt", "r")
        sys.stdout = open("./output.txt", "w")
 
    # Reading the number of test cases
    t = int(input().strip())
 
    # pre computations go here
 
    # Running each test case
    for _ in range(t):
        # Reading inputs for each test case
        
        # Calling the solve function
        solve()
 
 
# Calling the main function
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        with open("../output.txt", "a") as file:
            # Redirect the standard output to the file
            sys.stdout = file
            traceback.print_exc(file=file)
            print(e)
            # Reset the standard output back to the console
            sys.stdout = sys.__stdout__