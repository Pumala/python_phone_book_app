import pickle
# from os.path import exists

# if exists("phonebook.pickle"):
raw = open("phonebook.pickle", "r")
phonebook = pickle.load(raw)

#phonebook = [{}]

def savedata():
    raw = open("phonebook.pickle", "w")
    pickle.dump(phonebook, raw)
    raw.close()

phonebook = [
    {
        "name": "Emma",
        "phone": {
            "work": "834-542-8922",
            "home": "559-345-324",
            "cell": "221-456-345"
        }
    },
    {
        "name": "Louis",
        "phone": {
            "work": "766-542-7302",
            "home": "888-205-8421",
            "cell": "339-542-109"
        }
    },
    {
        "name": "Dwayne",
        "phone": {
            "work": "147-069-2938",
            "home": "859-655-2001",
            "cell": "839-103-183"
        }
    }
]

while True:
    print "\nElectronic Phone Book"
    print "====================="

    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Save"
    print "6\. Quit"

    choice = raw_input("What do you want to do? \n")

    if choice == "1":
        name = raw_input("Name? ")
        # look up person's number and print it out
        for index in range(0, len(phonebook)):
            if phonebook[index]["name"] == name:
                print name
                print "Found entry for %s : " % (phonebook[index]["name"])
                print "Work Number: %s" % phonebook[index]["phone"]["work"]
                print "Home Number: %s" % phonebook[index]["phone"]["home"]
                print "Cell Number: %s" % phonebook[index]["phone"]["cell"]
                # print "Found entry for %s : %s" % (phonebook[index]["name"], phonebook[index]["phone"])
        # break
    elif choice == "2":
        name = raw_input("Name? ")
        work_number = raw_input("Work number? ")
        home_number = raw_input("Home number? ")
        cell_number = raw_input("Cell number? ")
        phonebook.append({"name": name, "phone" : {"work": work_number, "home": home_number, "cell": cell_number}})
        print "Name: %s" % name
        # print "Phone Number: %s" % phone_number
        print "Work Number: %s" % work_number
        print "Home Number: %s" % home_number
        print "Cell Number: %s" % cell_number
        print "Entry stored for %s." % name
        # break
    elif choice == "3":
        name = raw_input("Name? ")
        # delete person's entry
        for index in range(0, len(phonebook)):
            # print index
            if phonebook[index]["name"] == name:
                del phonebook[index]
                break
        print "Name %s" % name
        print "Deleted entry for %s" % name
        # print phonebook
        # break
    elif choice == "4":
        # Print all entries in the dictionary
        for index in range(0, len(phonebook)):
            # if phonebook[index]["name"] == name:
            print "Found entry for %s: " % phonebook[index]["name"]
            print "Work Number: %s" % phonebook[index]["phone"]["work"]
            print "Home Number: %s" % phonebook[index]["phone"]["home"]
            print "Cell Number: %s \n" % phonebook[index]["phone"]["cell"]
        # break
        # for contact in phonebook:
        #     print "Found entry for %s: %s" % (contact[0], contact)
    elif choice == "5":
        savedata()
    elif choice == "6":
        print "Bye"
        break
        # end program
    else:
        print "Please choose a list from the following or write 5 to quit."
        # print "reprint electronic phone book"
