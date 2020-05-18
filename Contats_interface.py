import Contacts_functions
from sqlite3 import Error
import sqlite3


def create_connection(db_file):
    """ create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def main():
    database = r"Contacts"
    conn = create_connection(database)
    usr_input = input('what do you want to do? type help for prompts: ')
    if usr_input == 'help':
        print(
            '1.create contact\n'
            '2.show contacts\n'
            '3.delete contacts\n'
            'quit')
        main()
    if usr_input == '1':
        first = input('first name: ')
        last = input('last name: ')
        dob = input('date of birth dd-mm-yyyy: ')
        ph_num = input('phone number: ')
        with conn:
            contact = (first, last, dob, ph_num)
            print(contact)
            Contacts_functions.create_contact(conn, contact)
        main()
    if usr_input == '2':
        Contacts_functions.show(conn)
        main()
    if usr_input == '3':
        idt = input('What is the id of the name to be deleted? ')
        with conn:
            Contacts_functions.delete(conn, idt)
        print(idt)
        main()
    if usr_input == 'quit':
        print('quitting')
        quit()
    else:
        print('input not recognised')
        main()


if __name__ == '__main__':
    main()