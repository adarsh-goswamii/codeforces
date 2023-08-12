import math
import sys
import traceback

# global variable
INT_MAX = 2147483647
INT_MIN = -2147483648
# PLATFORM = 'LOCAL'
PLATFORM = 'ONLINE_JUDGE'

# Function to solve the problem


def solve(arr, n, m):
  # your code goes here.
  map1, map2, curr, ans = {}, {}, 1, []
  for i in arr:
    prevFreq = map1.get(i, 0)
    map1[i] = prevFreq + 1

    map2[prevFreq + 1] = map2.get(prevFreq + 1, 0) + 1

    if map2[curr] == n:
      ans.append('1')
      curr += 1
    else:
      ans.append('0')

  printArrToStr(ans)

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
  print('YES' if bool else 'NO')


def printArrToStr(arr):
  for item in arr:
    sys.stdout.write(item)
  sys.stdout.write('\n')

# Main function to handle input/output


def main():
  # Check if running locally
  if PLATFORM != 'ONLINE_JUDGE':
    sys.stdin = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')

  # Reading the number of test cases
  # t = int(input().strip())
  t = 1

  # pre computations go here

  # Running each test case
  for _ in range(t):
    # Reading inputs for each test case
    [n, m] = getInputs(2, int)
    arr = getInputs(m, int)

    # Calling the solve function
    solve(arr, n, m)


# Calling the main function
if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    with open('../output.txt', 'a') as file:
      # Redirect the standard output to the file
      sys.stdout = file
      traceback.print_exc(file=file)
      print(e)
      # Reset the standard output back to the console
      sys.stdout = sys.__stdout__
