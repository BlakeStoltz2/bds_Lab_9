
# encode function
def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

# decode function
def decode(encoded_password):


# main function
def main():
    while True:
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            password = input("Enter password to encode: ")
            print("Encoded password:", encode(password))

        elif choice == '2':
            encoded_password = input("Enter password to decode: ")
            print("Decoded password:", decode(encoded_password))

        elif choice == '3':
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
