import sqlite3
from sqlite3 import Error

link = r"C:\Users\39377\Desktop\InstaBot\DB\IgDB.db"


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn, username_command):
    """
    Query all rows in the tasks table
    :param username_command: command for username selection
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(username_command)
    rows = cur.fetchall()

    return rows


def db_update(username_initial):
    # create a database connection
    conn = create_connection(link)
    username_command = "SELECT email, password FROM login WHERE email GLOB '" + username_initial + "*'"

    with conn:
        return select_all_tasks(conn, username_command)


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


def db_add(first_name, last_name, email, password):
    # create a database connection
    conn = create_connection(link)

    with conn:
        # Add elements to table
        data = (first_name, last_name, email, password)
        project_id = insert_data(conn, data)


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def db_create():
    sql_create_login_table = """ CREATE TABLE IF NOT EXISTS login (
                                            first_name text NOT NULL,
                                            last_name text NOT NULL,
                                            email text NOT NULL,
                                            password text NOT NULL
                                        ); """

    # create a database connection
    conn = create_connection(link)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_login_table)
    else:
        print("Error! cannot create the database connection.")
