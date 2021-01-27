# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Hamza Raza
# Section:     415/ 515
# Assignment:  Lab 6b
# Date:        29 September 2020

#Make a blank list so I can store the user inputs within the list
user_list = []
pass_list = []
#Ask how many pairs there are
num_pairs = int(input("How many username/password pairs would you like: "))
#Run the code for as many pairs the user wants with the for loop
for x in range(num_pairs):
    #Have to ask the user for a username and password which adds into the respective blank list
    user = input("Enter a username: ")
    user_list.append(user)
    password = input("Enter a password: ")
    pass_list.append(password)

#Here I zip up the list making it immutable and encrypted
zip_dict = zip(user_list, pass_list)
dict_up = dict(zip_dict)
print(dict_up)
#The official test of trying to log in
user_guess = input("Enter username: ")
pass_guess = input("Enter password: ")
#Have to run the iterator within the dictionary

while user_guess in dict_up and dict_up[user_guess] != pass_guess:
#If the iterator within the dictionary wihch uses the username matches the password then you are logged in
    if user_guess in dict_up and dict_up[user_guess] == pass_guess:
    #Should end code if you are logged in
        break
#If the the iterator which is explained above doesnt equal the password then its an invalid username and same for the else below
    elif user_guess in dict_up and dict_up[user_guess] != pass_guess:
        print("Invalid password")
    else:
        print("Invalid password")
    user_guess = input("Enter username: ")
    pass_guess = input("Enter password: ")
print('Logged in!')
