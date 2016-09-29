import pickle
from os.path import exists

file_name = "elite_phonebook.pickle"

if exists(file_name):
    phonebook_file = open(file_name, "r")
    phonebook_dict = pickle.load(phonebook_file)
    phonebook_file.close()
    print "Loading file..."
else:
    phonebook_dict = []
    print "Creating new file..."

def lookup_entry():
    for index in range(0, len(phonebook_dict)):
        is_found = False
        if phonebook_dict[index]["name"] == name:
            print "\nFound entry for %s" % phonebook_dict[index]["name"]
            print "Email: %s" % phonebook_dict[index]["email"]
            print "Work Number: %s" % phonebook_dict[index]["phone"]["work"]
            print "Home Number: %s" % phonebook_dict[index]["phone"]["home"]
            print "Cell Number: %s" % phonebook_dict[index]["phone"]["cell"]
            is_found = True
            break
    if is_found == False:
        print "%s does not exist." % name
    else:
        pass

def add_new_entry():
    email = raw_input("Email? ")
    work_number = raw_input("Work number? ")
    home_number = raw_input("Home number? ")
    cell_number = raw_input("Cell number? ")
    phonebook_dict.append({"name": name, "email": email, "phone" : {"work": work_number, "home": home_number, "cell": cell_number}})
    # print "Name: %s" % name
    # print "Phone Number: %s" % phone_number
    # print "\tWork Number: %s" % work_number
    # print "Home Number: %s" % home_number
    # print "Cell Number: %s" % cell_number
    print "Entry stored for %s." % name

def delete_entry():
    for index in range(0, len(phonebook_dict)):
        is_found = False
        # print index
        if phonebook_dict[index]["name"] == name:
            del phonebook_dict[index]
            print "Deleted entry for %s" % name
            is_found = True
            break
    # print "Name %s" % name
    # print "Deleted entry for %s" % name
    if is_found == False:
        print "%s does not exist." % name
    else:
        pass

def print_all_entries():
    for index in range(0, len(phonebook_dict)):
        print "\nFound entry for %s: " % phonebook_dict[index]["name"]
        print "Email: %s" % phonebook_dict[index]["email"]
        print "Work Number: %s" % phonebook_dict[index]["phone"]["work"]
        print "Home Number: %s" % phonebook_dict[index]["phone"]["home"]
        print "Cell Number: %s \n" % phonebook_dict[index]["phone"]["cell"]

def save_entry():
    phonebook_file = open(file_name, "w")
    pickle.dump(phonebook_dict, phonebook_file)
    phonebook_file.close()

while True:
    print "\nElectronic Phone Book"
    print "====================="

    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Save"
    print "6. Quit"

    choice = int(raw_input("What do you want to do? "))

    if choice > 0 and choice < 7:
        if choice < 4:
            name = raw_input("Name? ").lower()
            if choice == 1:
                # retrieve phonenumber
                lookup_entry()
            elif choice == 2:
                # store new contact
                add_new_entry()
            elif choice == 3:
                delete_entry()
        else:
            if choice == 4:
                # print all entries in the phonebook
                print_all_entries()
            elif choice == 5:
                save_entry()
            else:
                print "Bye"
                break
    else:
        # Prompt user to select from the menu or exit the session
        print "Please choose a list from the following or write 6 to quit."
