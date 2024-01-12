class PhoneBook:
    def __init__(self):
        self.entries = {}

    def look_up_entry(self, name):
        if name in self.entries:
            print(f"Found entry for {name}: {self.entries[name]}")
        else:
            print(f"No entry found for {name}")


    def set_entry(self, name, phone_number):
        self.entries[name] = phone_number
        print(f"Entry stored for {name}.")


    def delete_entry(self, name):
        if name in self.entries:
            del self.entries[name]
            print(f"Deleted entry for {name}")
        else:
            print(f"No entry found for {name}")


    def list_all_entries(self):
        for name, phone_number in self.entries.items():
            print(f"Found entry for {name}: {phone_number}")

def main():
    phonebook = PhoneBook()

    while True:
            print("\nElectronic Phone Book\n=====================")
            print("1. Look up an entry")
            print("2. Set an entry")
            print("3. Delete an entry")
            print("4. List all entries")
            print("5. Quit")


            choice = input("What do you want to do (1-5)? ")


            if choice == "1":
                name = input("\nName: ")
                phonebook.look_up_entry(name)
            elif choice == "2":
                name = input("\nName: ")
                Phone_number = input("Phone Number: ")
                phonebook.set_entry(name, Phone_number)
            elif choice == "3":
                name = input("\nName: ")
                phonebook.delete_entry(name)
            elif choice == "4":
                phonebook.list_all_entries()
            elif choice == "5":
                print("\nBye.")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
    