name = input("Hello, please enter your name: ")
print(f"Hello, {name}! Welcome to the program.")
age = int(input("How old are you? "))
phonenumber = int(input("Please enter your phone number: "))
list = [name,age, phonenumber]
print(list)
print(f"Good, your name is {list[0]}, your age is {list[1]}, and your phone number is {list[2]}.")
#Now, I'm going to save those information on a text file called 'user_info.txt'
with open('user_info.txt', 'w') as file:
    file.write(f"Name: {list[0]}\n")
    file.write(f"Age: {list[1]}\n")
    file.write(f"Phone Number: {list[2]}\n");

print("Your information has been saved to 'user_info.txt'.")
if __name__ == "__main__":
    print("This script is being run directly.")
