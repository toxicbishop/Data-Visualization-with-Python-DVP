def binary_to_decimal(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value

    def octal_to_hexadecimal(octal_str):
        decimal_value = int(octal_str, 8)
        hexadecimal_value = hex(decimal_value).upper()
        return hexadecimal_value

def main () :
    try:
        choice = input("Choose a conversion (1 for binary to decimal, 2 for octal to hexadecimal): ")

        if choice == '1':
            binary_str = input("Enter a binary number: ")
            decimal_value = binary_to_decimal (binary_str)
            print (f"Decimal equivalent: {decimal_value}")
        elif choice == '2':
              octal_str = input ("Enter an octal number: ")
              hexadecimal_value = octal_to_hexadecimal(octal_str)
              print (f"Hexadecimal equivalent: (hexadecimal_value]")
        else:
            print ("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if name == "__main__":
    main()