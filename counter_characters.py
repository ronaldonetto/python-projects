#Code to determine the number of characters in a password
password = input("Enter your password: ") 

counter_characters = 0 #character counter

for i in password: #A loop to iterate through each character and thus sum the total quantity.
    counter_characters +=1 

print(f"Your password '{password}' contains {counter_characters} characters")
