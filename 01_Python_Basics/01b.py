def is_palindrome (number) :
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original_number == reversed_number

def count_digits (number) :
    digit_count = [0] * 10
    while number > 0:
        digit = number % 10
        digit_count[digit] += 1
        number //= 10
    return digit_count

try:
    num = int(input ("Enter a number: ") )
    if num < 0:
        print ("Please enter a non-negative number. ")
    else:
        if is_palindrome (num) :
            print (f"{num} is a palindrome.")
        else:
            print (f"{num} is not a palindrome.")

    digit_count = count_digits (num)

    for digit, count in enumerate(digit_count) :
        if count > 0:
            print (f"Digit {digit} appears {count} times in the number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")