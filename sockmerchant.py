import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    numberPair = 0
    uniquelist = []
    
    for color1 in ar:
        if color1 not in uniquelist:
            uniquelist.append(color1)
        else:
            numberPair+=1
            uniquelist.remove(color1)
        
    return numberPair



n = 9
ar = [10,20,20,10,10,30,50,10,20]
print(sockMerchant(n, ar))