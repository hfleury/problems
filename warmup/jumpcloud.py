# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    position = 0
    end_position = n - 1
    jumps = 0

    while position < end_position:
        if ((position + 2) <= end_position) and (c[position + 2] == 0):
            position += 2
            jumps += 1
        elif c[position + 1] == 0:
            position += 1
            jumps += 1
    return jumps

input = [0, 0, 0, 0, 1, 0]
print(jumpingOnClouds(input))