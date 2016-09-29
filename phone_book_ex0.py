phonebook = [
    {
        "name": "Emma",
        "phone": "834-542-8922"
    },
    {
        "name": "Louis",
        "phone": "531-904-3975"
    },
    {
        "name": "Dwayne",
        "phone": "348-019-7783"
    }
]

while True:
    print "Electronic Phone Book"
    print "====================="

    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Quit"

    choice = raw_input("What do you want to do? ")

    if choice == "1":
        name = raw_input("Name? ")
        # look up person's number and print it out
        for index in range(0, len(phonebook)):
            if phonebook[index]["name"] == name:
                print name
                print "Found entry for %s : %s" % (phonebook[index]["name"], phonebook[index]["phone"])
        # break
    elif choice == "2":
        name = raw_input("Name? ")
        phone_number = raw_input("Telephone number? ")
        phonebook.append({"name": name, "phone" : phone_number})
        print "Name: %s" % name
        print "Phone Number: %s" % phone_number
        print "Entry stored for Jazz."
        # break
    elif choice == "3":
        name = raw_input("Name? ")
        # delete person's entry
        for index in range(0, len(phonebook)):
            # print index
            if phonebook[index]["name"] == name:
                del phonebook[index]
                break
        print name
        print "Deleted entry for %s" % name
        # break
    elif choice == "4":
        # Print all entries in the dictionary
        for index in range(0, len(phonebook)):
            # if phonebook[index]["name"] == name:
            print "Found entry for %s: %s" %(phonebook[index]["name"], phonebook[index]["phone"])
        # break
        # for contact in phonebook:
        #     print "Found entry for %s: %s" % (contact[0], contact)
    elif choice == "5":
        print "Bye"
        break
        # end program
    else:
        pass
        # print "reprint electronic phone book"
