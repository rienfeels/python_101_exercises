coin_count = 0
while True:
    print("You have {} coin{}".format(coin_count, 's' if coin_count != 1 else ''))
    user_input = input("Do you want another? (yes/no)").lower()
    if user_input == 'yes':
        coin_count += 1
    elif user_input == 'no':
        print("Bye")
        break
    
              