import math
import sys
import traceback

# global variable
INT_MAX = 2147483647
INT_MIN = -2147483648
# PLATFORM = 'LOCAL'
PLATFORM = 'ONLINE_JUDGE'

# Function to solve the problem


def solve(arr, n):
  # your code goes here.
  prefix = [0] * n
  for i in range(n-1, -1, -1):
    prefix[i] = (prefix[i+2] if i+2 < n else 0) + arr[i]

  odd, even, ans = 0, 0, 0
  for i in range(0, n):
    if i % 2 == 0:
      totalOdd = odd + (prefix[i+2] if i+2 < n else 0)
      totalEven = even + (prefix[i+1] if i+1 < n else 0)
      even += arr[i]

      if totalEven == totalOdd:
        ans += 1
    else:
      totalOdd = odd + (prefix[i+1] if i+1 < n else 0)
      totalEven = even + (prefix[i+2] if i+2 < n else 0)
      odd += arr[i]

      if totalEven == totalOdd:
        ans += 1
  
  print(ans)

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
  if PLATFORM == "LOCAL":
    sys.stdin = open("../input.txt", "r")
    sys.stdout = open("../output.txt", "w")

  # Reading the number of test cases
  # t = int(input().strip())
  t = 1

  # pre computations go here

  # Running each test case
  for _ in range(t):
    # Reading inputs for each test case
    n = int(input())
    arr = getInputs(n, int)

    # Calling the solve function
    solve(arr, n)


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
