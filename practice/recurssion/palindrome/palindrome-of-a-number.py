def palindromeOfANumber(c_number, number):
    if number//10==0:
        return number%10==c_number[0]%10

    if not palindromeOfANumber(c_number, number//10):
        return False
    c_number[0] = c_number[0]//10

    return (number % 10 == c_number[0] % 10)
