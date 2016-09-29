import pickle
from os.path import exists

if exists("master_phonebook.pickle"):
    phonebook_file = open("master_phonebook.pickle", "r")
    phonebook_dict = pickle.load(phonebook_file)
    phonebook_file.close()
else:
    phonebook_dict = []

def get_phonenumber():
    for index in range(0, len(phonebook_dict)):
        is_found = False
        if phonebook_dict[index]["name"] == name:
            print "\nFound entry for %s" % phonebook_dict[index]["name"]
            print "Work Number: %s" % phonebook_dict[index]["phone"]["work"]
            print "Home Number: %s" % phonebook_dict[index]["phone"]["home"]
            print "Cell Number: %s" % phonebook_dict[index]["phone"]["cell"]
            is_found = True
            break
    if is_found == False:
        print "%s does not exist." % name
    else:
        pass

def add_new_contact():
    work_number = raw_input("Work number? ")
    home_number = raw_input("Home number? ")
    cell_number = raw_input("Cell number? ")
    phonebook_dict.append({"name": name, "phone" : {"work": work_number, "home": home_number, "cell": cell_number}})
    # print "Name: %s" % name
    # print "Phone Number: %s" % phone_number
    # print "\tWork Number: %s" % work_number
    # print "Home Number: %s" % home_number
    # print "Cell Number: %s" % cell_number
    print "Entry stored for %s." % name

def delete_contact():
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
        print "Work Number: %s" % phonebook_dict[index]["phone"]["work"]
        print "Home Number: %s" % phonebook_dict[index]["phone"]["home"]
        print "Cell Number: %s \n" % phonebook_dict[index]["phone"]["cell"]

def save_session():
    phonebook_file = open("master_phonebook.pickle", "w")
    pickle.dump(phonebook_dict, phonebook_file)
    phonebook_file.close()

while True:
    print "\nElectronic Phone Book"
    print "====================="

    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Save"
    print "6\. Quit"

    choice = int(raw_input("What do you want to do? "))

    if choice > 0 and choice < 7:
        if choice < 4:
            name = raw_input("Name? ").lower()
            if choice == 1:
                # retrieve phonenumber
                get_phonenumber()
            elif choice == 2:
                # store new contact
                add_new_contact()
            elif choice == 3:
                delete_contact()
        else:
            if choice == 4:
                # print all entries in the phonebook
                print_all_entries()
            elif choice == 5:
                save_session()
            else:
                print "Bye"
                break
    else:
        # Prompt user to select from the menu or exit the session
        print "Please choose a list from the following or write 6 to quit."
