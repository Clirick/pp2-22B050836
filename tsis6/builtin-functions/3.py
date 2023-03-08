def palindrome(s):
    s = s.lower() 
    reversed_s = ''.join(reversed(s))
    
    return s == reversed_s

string = str(input())

if palindrome(string):
    print(f"{string} palindrome")
else:
    print(f"{string} not palindrome")
