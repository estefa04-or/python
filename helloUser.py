name = input("Hello, please enter your name: ")

print(f"Hello, {name}! Welcome to the program.")

age = int(input("How old are you? "))

phonenumber = int(input("Please enter your phone number: "))

user_info = {
    "name": name,
    "age": age,
    "phone": phonenumber,
    "additional": ""
}

print(user_info)

print(
    f"Good, your name is {user_info['name']}, "
    f"your age is {user_info['age']}, "
    f"and your phone number is {user_info['phone']}."
)

# Save the information to a text file

with open('user_info.txt', 'w') as file:
    file.write(f"Name: {user_info['name']}\n")
    file.write(f"Age: {user_info['age']}\n")
    file.write(f"Phone Number: {user_info['phone']}\n")
    file.write(f"Additional Information: {user_info['additional']}\n")

print("Your information has been saved to 'user_info.txt'.")

# Read the information from the file

print("Now, let's read the information back from the file.")

with open('user_info.txt', 'r') as file:
    content = file.read()
    print(content)

# Ask for additional information

additional_info = input(
    "Would you like to add any additional information? (yes/no): "
)

if additional_info.lower() == 'yes':

    user_info["additional"] = input(
        "Please enter the additional information: "
    )

    print("Your additional information has been saved.")

# Ask if the user wants to change information

change_info = input(
    "Would you like to change any of the information? (yes/no): "
)

while change_info.lower() == 'yes':

    field_to_change = input(
        "Which field would you like to change? "
        "(name/age/phone/additional): "
    )

    if field_to_change.lower() == 'name':

        new_name = input("Please enter the new name: ")
        user_info["name"] = new_name

    elif field_to_change.lower() == 'age':

        new_age = int(input("Please enter the new age: "))
        user_info["age"] = new_age

    elif field_to_change.lower() == 'phone':

        new_phone = input("Please enter the new phone number: ")
        user_info["phone"] = new_phone

    elif field_to_change.lower() == 'additional':

        new_additional_info = input(
            "Please enter the new additional information: "
        )

        user_info["additional"] = new_additional_info

    else:
        print("Invalid field selection.")

    # Save all four values again

    with open('user_info.txt', 'w') as file:
        file.write(f"Name: {user_info['name']}\n")
        file.write(f"Age: {user_info['age']}\n")
        file.write(f"Phone Number: {user_info['phone']}\n")
        file.write(f"Additional Information: {user_info['additional']}\n")

    change_info = input(
        "Would you like to change any of the information again? (yes/no): "
    )

print("Your information has been updated in 'user_info.txt'.")
