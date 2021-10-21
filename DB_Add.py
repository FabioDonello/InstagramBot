import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def insert_data(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO login(first_name, last_name, email, password)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def main(first_name, last_name, email, password):

    database = r"/Users/fabiodonello/Desktop/Esame OOP/InstgramBot_0/DB/IgDB.db"

    # create a database connection
    conn = create_connection(database)

    with conn:
        # Add elements to table
        data = (first_name, last_name, email, password)
        project_id = insert_data(conn, data)








