user_input = input("Please fill in the blanks below: ")
print(user_input)
print("____(name)____'s favorite subject in school is ____(subject)____.")
user_name = input("What is name? ")
user_subject = input("What is subject? ")

result_statement = "{}'s favorite subject in school is {}.".format(user_name, user_subject)

print(result_statement)
