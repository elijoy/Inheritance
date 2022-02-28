class Person:

    def __init__(self, name,address,phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__phone_number)

class Customer(Person):

    def __init__(self, name, address, phone_number, customer_number, mailing_list):

        Person.__init__(self, name, address, phone_number)

        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def print_person(self):
        Person.print_person(self)
        print(self.__customer_number)
        print(self.__mailing_list)
        
