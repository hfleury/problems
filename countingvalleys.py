def countingValleys(n, s):
    
    sealevel = 0
    valleys_number = 0

    for i in s:
        if i == 'U':
            if sealevel == -1:
                valleys_number+=1
            sealevel+=1
        elif i == 'D':
            sealevel-=1
        
    return valleys_number


input_n = 8
input_s = 'UDDDUDDUU'
print(countingValleys(input_n, input_s))
