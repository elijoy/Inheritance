import PersonClass as person

def main():
    pers = person.Person("Elizabeth", "1234 Rochelle Rd", "555-5555")
    pers.print_person()

    print()
    
    cust = person.Customer("Lizzy", "1600 Sth 5th street", "123-1234",1,True)
    cust.print_person()

main()