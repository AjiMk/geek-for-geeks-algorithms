"""
    https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/
"""
def palindromeOfANumber(c_number, number):
    if number//10==0:
        return number%10==c_number[0]%10

    if not palindromeOfANumber(c_number, number//10):
        return False
    c_number[0] = c_number[0]//10

    return (number % 10 == c_number[0] % 10)

number = 112211
c_number = [number]
if palindromeOfANumber(c_number, number):
    print("palindrome")
else:
    print("not palindrome")