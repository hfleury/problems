import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    count_arr = len(arr)
    dimension = 0
    results = []

    while len(arr) > dimension + 2:
        for number in arr[dimension]:
            print(number)
        dimension+=1

    # for lines in arr:

    
    print(arr)

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)

print(result)