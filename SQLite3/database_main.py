import sqlite3


def main():
    """Main function to demonstrate SQLite database operations."""

    # Create or connect to the database 'PythonProg.db'
    database = sqlite3.connect('PythonProg.db')

    # Create a cursor object to interact with the database
    cursor = database.cursor()

    # Create a table named 'python_programming' with columns id,
    # name, and grade
    create_table(cursor)

    # Set the values to be inserted into the table
    people = [
        (55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99)
    ]

    # Insert the values into the 'python_programming' table
    insert_data(cursor, people)

    # Execute a SELECT query to retrieve rows where the grade
    # is between 60 and 80
    query_and_print(cursor)

    # Update the grade of 'Carl Davis' to 65
    update_grade_of_carl_davis(cursor)

    # Delete the row where the id is 66
    delete_row_with_id_66(cursor)

    # Update the grade to 80 for all rows where the id is greater than 55
    update_grade_to_80(cursor)

    # Commit the changes to the database
    database.commit()

    # Close the cursor and the database connection
    cursor.close()
    database.close()


def create_table(cursor):
    """Create the 'python_programming' table if it does not exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS python_programming (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade INTEGER
        )
    ''')


def insert_data(cursor, data):
    """Insert data into the 'python_programming' table."""
    cursor.executemany('''
        INSERT INTO python_programming (id, name, grade)
        VALUES (?, ?, ?)
    ''', data)


def query_and_print(cursor):
    """Execute a SELECT query and print the results."""
    cursor.execute('''
        SELECT * FROM python_programming
        WHERE grade > 60
        AND grade < 80;
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def update_grade_of_carl_davis(cursor):
    """Update the grade of 'Carl Davis' to 65."""
    cursor.execute('''
        UPDATE python_programming
        SET grade = 65
        WHERE name = 'Carl Davis'
    ''')


def delete_row_with_id_66(cursor):
    """Delete the row where the id is 66."""
    cursor.execute('''
        DELETE FROM python_programming
        WHERE id = 66
    ''')


def update_grade_to_80(cursor):
    """Update the grade to 80 for all rows where the id is greater than 55."""
    cursor.execute('''
        UPDATE python_programming
        SET grade = 80
        WHERE id > 55
    ''')


if __name__ == "__main__":
    main()
