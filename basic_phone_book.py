import pickle
from os.path import exists

if exists("phonebook.pickle"):
    phonebook_file = open("phonebook.pickle", "r")
    phonebook_dict = pickle.load(phonebook_file)
    phonebook_file.close()
else:
    phonebook_dict = {}
    
# if exists("phonebook.pickle"):
# raw = open("phonebook.pickle", "r")
# phonebook = pickle.load(raw)


# def savedata():
#     raw = open("phonebook.pickle", "w")
#     pickle.dump(phonebook, raw)
#     raw.close()

# phonebook = {
#         "emma": "388-229-1111",
#         "dwayne": "348-019-7783",
#         "jonas": "531-904-3975"
#     }

# print phonebook

# for key, value in phonebook.items():
#     if key == "Dwayne":
#         print phonebook["Dwayne"]

while True:
    print "\nElectronic Phone Book"
    print "====================="

    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Save"
    print "6. Quit"

    choice = raw_input("What do you want to do (1 - 6)? ")

    if choice == "1":
        name = raw_input("Name? ").lower()
        # look up person's number and print it out
        if name in phonebook_dict:
            phone_number = phonebook_dict[name]
            print "Found entry for %s: %s" % (name, phone_number)
        else:
            print "%s does not exist." % name
        # for key, value in phonebook.items():
        #     if key == name:
        #         print "Name: %s" % key
        #         print "Found entry for %s: %s" % (key, value)
        #     else:
        #         print "%s does not exist." % name
    elif choice == "2":
        name = raw_input("Name? ").lower()
        phone_number = raw_input("Telephone number? ")
        phonebook_dict[name] = phone_number
        print "Name: %s" % name
        print "Phone Number: %s" % phone_number
        print "Entry stored for %s." % name
    elif choice == "3":
        name = raw_input("Name? ").lower()
        # delete person's entry
        if name in phonebook_dict:
            del phonebook_dict[name]
            print "Deleted entry for %s" % name
        else:
            print "%s does not exist." % name
        # for key, value in phonebook.items():
        #     if key == name:
        #         del phonebook[name]
        # print phonebook
        # print "Deleted entry for %s" % name
    elif choice == "4":
        # Print all entries in the dictionary
        for name, phone_number in phonebook_dict.items():
            print "Found entry for %s: %s" % (name, phone_number)
    elif choice == "5":
        phonebook_file = open("phonebook.pickle", "w")
        pickle.dump(phonebook_dict, phonebook_file)
        phonebook_file.close()
        print "Phonebook saved."
    elif choice == "6":
        # end program
        print "Bye"
        break
    else:
        print "Please choose a list from the following or write 6 to quit."
        # print "reprint electronic phone book"
