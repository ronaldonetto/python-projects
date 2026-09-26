#Code written to test whether a password is stromg or weak

#Current Boolean accumulators
counter_characters = 0
uppercase_letters = False
lowercase_letters = False
it_has_numbers = False

#Variables to check password requirements
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

password = input("Your password: ") #Asking the user for the password

#Loop to count the number of characters and check if there are uppercase and lowercase letters and numbers
for character in password:
     counter_characters += 1
     if character in uppercase:
        uppercase_letters = True
     elif character in lowercase:
         lowercase_letters = True
     elif character in numbers:
          it_has_numbers = True
       
print(f"The password contains {counter_characters} characters")  #Displaying the character count  

if uppercase_letters == True:
    print("The password contains uppercase letters.")
else:
   print("The password does not contain uppercase letters.")
if lowercase_letters == True:
    print("The password contains lowercase letters.")
else:
    print("The password does not contain lowercase letters.")
if it_has_numbers == True:
    print("The password contains numbers.")
else:
    print("The password does not contain number")



   
