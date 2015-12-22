def convert_radix(n, r):
    return get_digit(n) if n < r else convert_radix(n/r, r) + get_digit(n%r)

def get_digit(n):
    return str(chr(55+n)) if n > 9 else str(n)

def is_palindrome(n):
    results = []
    for i in range(2, 37):
        if check_palin(convert_radix(n, i)):
            results.append(i)
    return results

def check_palin(s):
    return False if s[0] != s[-1] else (True if len(s)<3 else check_palin(s[1:len(s) - 1]))