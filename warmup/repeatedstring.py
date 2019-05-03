from collections import Counter

def repeatedString(s, n):

    count_a = s.count('a')
    len_s = len(s)
    divide = n % len_s
    import ipdb; ipdb.set_trace()
    if s == 'a':
        response = n
    elif divide is 0:
        response = count_a * (n / len_s)
    else:
        string_cutted = s[:divide]
        response = count_a * (n / len_s) + string_cutted.count('a')

    return response

s = 'aba'
n = 10
print(repeatedString(s, n))
