import pickle
# from os.path import exists

# if exists("phonebook.pickle"):
raw = open("phonebook.pickle", "r")
phonebook = pickle.load(raw)

# phonebook = {}

def savedata():
    raw = open("phonebook.pickle", "w")
    pickle.dump(phonebook, raw)
    raw.close()

# phonebook = {
#         "Emma": "388-229-1111",
#         "Dwayne": "348-019-7783",
#         "Jonas": "531-904-3975"
#     }

# print phonebook

# for key, value in phonebook.items():
#     if key == "Dwayne":
#         print phonebook["Dwayne"]

while True:
    print "\nElectronic Phone Book"
    print "====================="

    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Save"
    print "6\. Quit"

    choice = raw_input("What do you want to do (1 - 6)? ")

    if choice == "1":
        name = raw_input("Name? ")
        # look up person's number and print it out
        for key, value in phonebook.items():
            if key == name:
                print "Name: %s" % key
                print "Found entry for %s: %s" % (key, value)
    elif choice == "2":
        name = raw_input("Name? ")
        phone_number = raw_input("Telephone number? ")
        phonebook[name] = phone_number
        # phonebook.append({"name": name, "phone" : phone_number})
        print "Name: %s" % name
        print "Phone Number: %s" % phone_number
        print "Entry stored for %s." % name
    elif choice == "3":
        name = raw_input("Name? ")
        # delete person's entry
        for key, value in phonebook.items():
            if key == name:
                del phonebook[name]
        print phonebook
        print "Deleted entry for %s" % name
    elif choice == "4":
        # Print all entries in the dictionary
        for key, value in phonebook.items():
            print "Found entry for %s: %s" % (key, value)
    elif choice == "5":
        savedata()
    elif choice == "6":
        # end program
        print "Bye"
        break
    else:
        print "Please choose a list from the following or write 5 to quit."
        # print "reprint electronic phone book"
