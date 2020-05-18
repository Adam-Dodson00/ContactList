import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table in a given database"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    print('table created')


def create_contact(conn, contacts_list):
    """Add a info to a table"""
    sql = ''' INSERT INTO contacts_list(first_name,last_name,dob,ph_number)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, contacts_list)
    print('Contact added')
    return cur.lastrowid


def show(conn):
    """show all contacts"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts_list")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def search(conn, first_name):
    """find a contact by searching first names"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts_list WHERE first_name=?", (first_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def delete(conn, idnum):
    """remove a contact"""
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts_list WHERE id=?", (idnum,))
    print('contact deleted')


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM contacts_list'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def close_connection(conn):
    conn.close()


def main():
    database = r"Contacts"
    conn = create_connection(database)
    with conn:
    #     """Create table"""
    #     sql_input_fields = """ CREATE TABLE IF NOT EXISTS contacts_list(
    #                             id integer PRIMARY KEY,
    #                             first_name text NOT NULL,
    #                             last_name text NOT NULL,
    #                             dob text NOT NULL,
    #                             ph_number text NOT NULL);"""
    #     create_table(conn,sql_input_fields)

        """Create contacts"""
        # contact = ('Adam', 'Dodson', '04-01-2000', '0438284577')
        # contact = ('Bob', 'Dodson', '05-11-2010', '0473884567')
        #
        # create_contact(conn, contact)

        """show items in the tables"""
        show(conn)

        """search for a first name"""
        # search(conn, "Adam")

        """remove a contact by id number"""
        # delete(conn, 2)

        """close connection"""
        # close_connection()

        # delete_all_tasks(conn)


if __name__ == '__main__':
    main()