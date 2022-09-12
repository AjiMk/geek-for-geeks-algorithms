"""
   https://en.wikipedia.org/wiki/Palindrome

   test-cases

   I/P: abcd
   O/P: false

   I/P: abba
   O/P: true

   I/P: geeks
   O/P: false
"""

def isPalindrome(string, start, end):
    if start>= end:
        return True

    return string[start]==string[end] and isPalindrome(string, start+1, end-1)


inputs = [
    "abcd",
    "abba",
    "geeks",
    "forgeeksskeegfor"
]

for input in inputs:
    palindrome_status = "`palindrome`" if isPalindrome(input,0, len(input)-1) else "`not palindrome`"
    print(input+" is "+ palindrome_status)
