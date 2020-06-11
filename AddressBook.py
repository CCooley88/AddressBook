from pip._vendor.distlib.compat import raw_input

# This program is designed to work as an electronic address book taking in various pieces of information about contacts.
# It offers the ability to use a number of multi-level sorting functions, to add and remove contacts,
# and an option to display single contacts based on an e-mail address.

userInput = ""

def printMenu():
    print("1 - Add Entry")
    print("2 - Delete Entry")
    print("3 - Display a single entry")
    print("4 - Sort by first & last name")
    print("5 - Sort by Zip, City, & State")
    print("6 - Sort by e-mail")
    print("7 - Exit")

class Person:
    def __init__(self, first, last, street, city, state, zip, phone, email):
    # def __init__(self, first, last):
        self.first = first
        self.last = last
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def __repr__(self):
        # return self.first + " "  + self.last
        return '{} {} {} {} {}. {}, {}, {}'.format(self.first, self.last, self.street, self.city, self.state,self.zip,self.phone,self.email)


def getNewUserInfo():
    newFirstName = input("First name: ")
    newLastName = input("Last name: ")
    newStreet = input("Street: ")
    newCity = input("City: ")
    newState = input("State: ")
    newZip = input("Zip: ")
    newPhone = input("Phone: ")
    newEmail = input("E-mail: ")
    print("")

    return Person(newFirstName,newLastName, newStreet, newCity, newState, newZip, newPhone, newEmail )

def pSort(person):
    return person.last

def removePerson():
    print("")
    printList()
    toRemove = input("Please enter the rolodex number of this person: ")
    if(int(toRemove) > len(list)-1):
        print("There are only " + str(len(list)) + " entries in the list.")
    elif (int(toRemove) <= 0):
        print("There are no rolodex entries lower than 1.")
    else:
        list.remove(list[int(toRemove)-1])

def showPerson():
    email = input("Enter the e-mail of the person you wish to view: ")
    for person in list:
        if person.email == email:
            print(person.__repr__())
            print("")
            return
    print("Person/e-mail not found in list.")

def printList():
    i=1
    for person in list:
        print(str(i) + " " + person.__repr__())
        # print(x.__repr__())
        i+=1
    print("")

#################
# Adding contacts to the list
list = []
p1 = Person("Al","Albertson", "55 Joy St", "Boston", "Ma", "02110", "144-6987", "AAlbertson@gmail.com")
p2 = Person("Chris", "Boveau", "4 Can St", "Talem", "Ma", "01970", "237-5864", "ChrisBoveau@gmail.com")
p3 = Person("Chris", "Christopherson", "3 Ray Road", "Salem", "Ma", "01970", "368-444", "ChrisChris@gmail.com")
list.append(p3)
list.append(p2)
list.append(p1)


printMenu()
loop = True;
while loop:
    userInput = input("Enter your selection: ")
    if userInput == "1":
         list.append(getNewUserInfo())
    elif userInput == "2":
       removePerson()
    elif userInput == "3":
        showPerson()
    elif userInput == "4":
        list = sorted(list, key=lambda person: (person.first, person.last))
        printList()
    elif userInput == "5":
        list = sorted(list, key=lambda person: (person.zip, person.city, person.state))
        printList()
    elif userInput == "6":
        list = sorted(list, key= lambda person: person.email)
        printList()
    elif userInput == "7":
        loop = False;
    else:
        print("Unknown request entered.")


