name = input("Hello, please enter your name: ")
print(f"Hello, {name}! Welcome to the program.")
age = int(input("How old are you? "))
phonenumber = int(input("Please enter your phone number: "))
user_info = [name,age, phonenumber]
additional_information = ""
print(user_info)
print(f"Good, your name is {user_info[0]}, your age is {user_info[1]}, and your phone number is {user_info[2]}.")
#Now, I'm going to save those information on a text file called 'user_info.txt'
with open('user_info.txt', 'w') as file:
    file.write(f"Name: {user_info[0]}\n")
    file.write(f"Age: {user_info[1]}\n")
    file.write(f"Phone Number: {user_info[2]}\n");

print("Your information has been saved to 'user_info.txt'.")

print("Now, let's read the information back from the file.")
with open('user_info.txt', 'r') as file:
    content = file.read() #.read() reads the entire content of the file and returns it as a string
    print(content)

additional_info = input("Would you like to add any additional information? (yes/no): ")
if additional_info.lower() == 'yes':
    additional_information = input("Please enter the additional information: ")
    print("Your additional information has been saved to 'user_info.txt'.")

change_info = input("Would you like to change any of the information? (yes/no): ")

while change_info.lower() == 'yes':

    field_to_change = input(
        "Which field would you like to change? (name/age/phone/additional): "
    )

    if field_to_change.lower() == 'name':
        new_name = input("Please enter the new name: ")
        user_info[0] = new_name

    elif field_to_change.lower() == 'age':
        new_age = int(input("Please enter the new age: "))
        user_info[1] = new_age

    elif field_to_change.lower() == 'phone':
        new_phone = int(input("Please enter the new phone number: "))
        user_info[2] = new_phone

    elif field_to_change.lower() == 'additional':
        new_additional_info = input(
            "Please enter the new additional information: "
        )
        additional_information = new_additional_info

    else:
        print("Invalid field selection.")

    with open('user_info.txt', 'w') as file:
        file.write(f"Name: {user_info[0]}\n")
        file.write(f"Age: {user_info[1]}\n")
        file.write(f"Phone Number: {user_info[2]}\n")
        file.write(f"Additional Information: {additional_information}\n")

    change_info = input(
        "Would you like to change any of the information again? (yes/no): "
    )

print("Your information has been updated in 'user_info.txt'.")

if __name__ == "__main__":
    print("This script is being run directly.")
