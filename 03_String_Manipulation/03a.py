def count_characters(sentence) :
    word_count = len(sentence.split())
    digit_count = sum(1 for char in sentence if char.isdigit())
    upper_count = sum(1 for char in sentence if char.isupper())
    lower_count = sum(1 for char in sentence if char.islower())

    return word_count, digit_count, upper_count, lower_count

try:
    sentence = input("Enter a sentence: ")

    word_count, digit_count, upper_count, lower_count = count_characters(sentence)

    print("Number of words:", word_count)
    print("Number of digits:", digit_count)
    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)
except ValueError:
    print("Invalid input. Please enter a valid sentence.")
except Exception as e:
    print(f"An error occurred: {e}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except EOFError:
    print("\nEnd of file reached.")
except MemoryError:
    print("\nMemory error occurred.")
except Exception as e:
    print(f"\nAn unknown error occurred: {e}")