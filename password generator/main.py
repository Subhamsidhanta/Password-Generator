import random
import datetime



def ranascii(n):
    password = ""
    if n>4:
        i = 0
        
        while i < n:
            random_number = random.randint(33, 126)
            password += chr(random_number)
            i = i + 1
        print(password)
        

        save_password(password)
    else:
        print("Password length must be greater than 4. Please try again.")
        n = int(input("Tell me how long you want your password to be: "))
        ranascii(n)

def save_password(password):
    usage_location = input("Where are you going to use this password? (e.g., email, website): ")
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open the file in append mode
    with open("passwords.txt", "a") as file:
        file.write(f"Used for: {usage_location}\nPassword: {password}\nDate/Time: {date_time}\n\n")

    print(f"Password saved with location: {usage_location}")

print("Welcome to the password generator")
n = int(input("Tell me how long you want your password to be: "))
print("Generating password...")
ranascii(n)
