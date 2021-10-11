def main():
    contacts = open("contacts.txt", "w")
    num = int(input("How many people do you want to add to the address book?   "))
    for address in range(0, num):
        name = input("name:  ")
        phone = input("phone:  ")
        email = input("email:  ")
        contacts.write(name + " " + phone + " " + email + "\n")

        contacts.close()



main()
