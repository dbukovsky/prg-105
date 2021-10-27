class Personal_Data:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


def main():
    person1 = Personal_Data("Dylan Bukovsky", "4270 Gladstone Drive", "21", "2246239650")
    person2 = Personal_Data("Melissa Bukovsky", "7115 Country Club Hills Drive", "46", "8474892849")
    person3 = Personal_Data("Tyler Ahlers", "6 St Lo Court", "22", "2246758970")

    print("\n\nPerson one:  " + person1.get_name() + "\n" + person1.get_address() + "\n" + person1.get_age() + "\n" + person1.get_phone())
    print("\n\nPerson two:  " + person2.get_name() + "\n" + person2.get_address() + "\n" + person2.get_age() + "\n" + person2.get_phone())
    print("\n\nPerson three:  " + person3.get_name() + "\n" + person3.get_address() + "\n" + person3.get_age() + "\n" + person3.get_phone())


main()
