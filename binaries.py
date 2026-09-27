#Code to convert binary to decimal and decimal to binary

while True:
    #Menu options for the user to chose from
    print("----------- BIT CONVERTER -----------\n")
    print("1 -> Convert binaries to decimal")
    print("2 -> Convert decimal to binaries")
    print("3 -> Exit\n")
 
    choice = int(input("Enter your choice:"))

    if choice == 1:
        binary = input("Enter  a binary number: ")
        number_decimal = int(binary,2)#Converting binary numbers to decimal
        print(f"The binary number {binary} in decimal is {number_decimal}\n")
    elif choice == 2:
        number = int(input("Enter a number: "))
        pury_binary = bin(number)[2:]#Converting decimal number to binary numbers
        print(f"The decimal number {number} in binary is {pury_binary}\n")
    elif choice == 3:
        break   
    else:
        print("Invalid choice, Please enter a valid choice.")
    