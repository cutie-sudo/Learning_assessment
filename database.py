import sqlite3

def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect("learning_assessment.db")
    return conn


def create_tables():
    """Create necessary tables in the database."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS Students')

    # Create Instructors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Instructors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        specialization TEXT
    )
    ''')

    # Create Courses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        instructor_id INTEGER NOT NULL,
        FOREIGN KEY (instructor_id) REFERENCES Instructors (id)
    )
    ''')

    # Create Students table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        course_id INTEGER,
        FOREIGN KEY (course_id) REFERENCES Courses (id)
    )
    ''')

    # Create Enrollments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Students (id),
        FOREIGN KEY (course_id) REFERENCES Courses (id)
    )
    ''')

    # Create Assessments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (course_id) REFERENCES Courses (id)
    )
    ''')

    # Create Performance table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        assessment_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Students (id),
        FOREIGN KEY (assessment_id) REFERENCES Assessments (id)
    )
    ''')

    conn.commit()
    conn.close()


def get_table_info(table_name):
    """Retrieve information about a table's schema."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    rows = cursor.fetchall()
    conn.close()
    return rows


# Example usage
if __name__ == "__main__":
    create_tables()
    table_info = get_table_info("Instructors")
    print("Table Info for Instructors:")
    for column in table_info:
        print(column)

    table_info = get_table_info("Students")
    print("Table Info for Students:")
    for column in table_info:
        print(column)

    table_info = get_table_info("Enrollments")
    print("Table Info for Enrollments:")
    for column in table_info:
        print(column)
