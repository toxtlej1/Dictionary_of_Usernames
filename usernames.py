"""
	Author: Jesus Toxtle
	Date: 01/27/2022
	Time: 23:40 PM
	Purpose: Python program will check whether an existing (key, value) pair in a dictonary from a text file already exists.
	Version: V1
"""
import json

def username_taken(username):
	print("\nThat username " + username + " is already taken.\nThe program will now terminate." + "\n")
	exit(1)

while True:
	print("Please enter a username: ")
	user_name_input = input()

	# Base case: preset list of usernames in list_usernames.txt
	with open("list_usernames.txt", "r") as read_usernames:
		for line in read_usernames:
			if user_name_input in line:
				username_taken(user_name_input)

	# Read list of usernames from newly created .txt file; verify if (key, value) pair already exists.
	with open("list_usernames_new.txt", "r") as read_new_usernames:
		for new_uname in read_new_usernames:
			if user_name_input in new_uname:
				username_taken(user_name_input)

		print(read_new_usernames.read())

	# If the inputted username doesn't exist already, then append a new (key, value) pair to the new .txt file
	with open("list_usernames_new.txt", "a+") as write_new_username:
		print('I don\'t have ' + user_name_input + ' username, what is it?')
		add_new_username = input()
		write_new_username.write(json.dumps('{ %s : %s },' % (user_name_input, add_new_username)))
		write_new_username.write("\n")
		write_new_username.close()
