import sqlite3
import os
import time
from database import connect_db, create_tables

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Utility Functions
def execute_query(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()


def fetch_query(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

# Instructor Management
def manage_instructors():
    while True:
        print("\n--- Instructor Management ---")
        print("1. Add Instructor")
        print("2. View Instructors")
        print("3. Update Instructor")
        print("4. Delete Instructor")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter instructor name: ")
            email = input("Enter instructor email: ")
            specialization = input("Enter instructor specialization: ")
            execute_query("INSERT INTO Instructors (name, email, specialization) VALUES (?, ?, ?)", (name, email, specialization))
            print("Instructor added successfully.")
        elif choice == "2":
            instructors = fetch_query("SELECT * FROM Instructors")
            for instructor in instructors:
                print(instructor)
        elif choice == "3":
           instructor_id = input("Enter instructor ID to update: ")
           name = input("Enter new name: ")
           email = input("Enter new email: ")
           specialization = input("Enter new specialization: ")  # Include this field if required
           execute_query(
               "UPDATE Instructors SET name = ?, email = ?, specialization = ? WHERE id = ?", 
               (name, email, specialization, instructor_id)
           )
           print("Instructor updated successfully.")
        elif choice == "4":
           instructor_id = input("Enter instructor ID to delete: ")
           execute_query("DELETE FROM Instructors WHERE id = ?", (instructor_id,))
           print("Instructor deleted successfully.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(2)
        clear_screen()

# Course Management
def manage_courses():
    while True:
        print("\n--- Course Management ---")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter course name: ")
            description = input("Enter course description: ")
            instructor_id = input("Enter instructor ID for the course: ")
            execute_query("INSERT INTO Courses (name, description, instructor_id) VALUES (?, ?, ?)", (name, description, instructor_id))
            print("Course added successfully.")
        elif choice == "2":
            courses = fetch_query("SELECT * FROM Courses")
            for course in courses:
                print(course)
        elif choice == "3":
            course_id = input("Enter course ID to update: ")
            name = input("Enter new name: ")
            description = input("Enter new description: ")
            instructor_id = input("Enter new instructor ID: ")
            execute_query(
    "UPDATE Courses SET name = ?, description = ?, instructor_id = ? WHERE id = ?", 
    (name, description, instructor_id, course_id)
)
            print("Course updated successfully.")
        elif choice == "4":
            course_id = input("Enter course ID to delete: ")
            execute_query("DELETE FROM Courses WHERE id = ?", (course_id,))

            print("Course deleted successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

            time.sleep(2)
            clear_screen()

# Student Management
def manage_students():
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            course_id = input("Enter course_id: ")
            execute_query("INSERT INTO Students (name, email, course_id) VALUES (?, ?, ?)", (name, email, course_id))
            print("Student added successfully.")
        elif choice == "2":
            students = fetch_query("SELECT * FROM Students")
            for student in students:
                print(student)
        # In manage_students() function
        elif choice == "3":  # Update Student
           student_id = int(input("Enter student ID to update: "))
           name = input("Enter new name: ")
           email = input("Enter new email: ")
           execute_query(
                "UPDATE Students SET name = ?, email = ? WHERE id = ?",
                (name, email, student_id)
           )
           print("Student updated successfully!")

# In manage_students() function
        elif choice == "4":  # Delete Student
           student_id = int(input("Enter student ID to delete: "))
           execute_query("DELETE FROM Students WHERE id = ?", (student_id,))
           print("Student deleted successfully!")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

            time.sleep(2)
            clear_screen()

# Enrollment Management
def manage_enrollments():
    while True:
        print("\n--- Enrollment Management ---")
        print("1. Add Enrollment")
        print("2. View Enrollments")
        print("3. Update Enrollment")
        print("4. Delete Enrollment")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            execute_query("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
            print("Enrollment added successfully.")
        elif choice == "2":
            enrollments = fetch_query("SELECT * FROM Enrollments")
            for enrollment in enrollments:
                print(enrollment)

        elif choice == "3":
           id = input("Enter enrollment ID to update: ")
           student_id = input("Enter new student ID: ")
           course_id = input("Enter new course ID: ")
           execute_query(
               "UPDATE Enrollments SET student_id = ?, course_id = ? WHERE id = ?", 
               (student_id, course_id, id)
           )
           print("Enrollment updated successfully.")

        elif choice == "4":
            id = input("Enter enrollment ID to delete: ")
            execute_query("DELETE FROM Enrollments WHERE enrollment_id = ?", (id,))
            print("Enrollment deleted successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

            time.sleep(2)
            clear_screen()




# Assessment Management
def manage_assessments():
    while True:
        print("\n--- Assessment Management ---")
        print("1. Add Assessment")
        print("2. View Assessments")
        print("3. Update Assessment")
        print("4. Delete Assessment")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter assessment name: ")
            course_id = input("Enter course ID for the assessment: ")
            execute_query("INSERT INTO Assessments (name, course_id) VALUES (?, ?)", (name, course_id))
            print("Assessment added successfully.")
        elif choice == "2":
            assessments = fetch_query("SELECT * FROM Assessments")
            for assessment in assessments:
                print(assessment)
        elif choice == "3":
            assessment_id = input("Enter assessment ID to update: ")
            name = input("Enter new name: ")
            course_id = input("Enter new course ID: ")
            execute_query("UPDATE Assessments SET name = ?, course_id = ? WHERE assessment_id = ?", (name, course_id, assessment_id))
            print("Assessment updated successfully.")
        elif choice == "4":
            assessment_id = input("Enter assessment ID to delete: ")
            execute_query("DELETE FROM Assessments WHERE assessment_id = ?", (assessment_id,))
            print("Assessment deleted successfully.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

           
            clear_screen()


# Performance Management
def Track_performance():
    while True:
        print("\n--- Performance Management ---")
        print("1. Add Performance")
        print("2. View Performance")
        print("3. Update Performance")
        print("4. Delete Performance")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            student_id = input("Enter student ID: ")
            assessment_id = input("Enter assessment ID: ")
            score = input("Enter score: ")
            execute_query("INSERT INTO Performance (student_id, assessment_id, score) VALUES (?, ?, ?)", (student_id, assessment_id, score))
            print("Performance added successfully.")
            time.sleep(2)
            clear_screen()
        elif choice == "2":
            performance_records = fetch_query("SELECT * FROM Performance")
            for record in performance_records:
                print(record)
            time.sleep(2)
            clear_screen()
        elif choice == "3":
            performance_id = input("Enter performance ID to update: ")
            score = input("Enter new score: ")
            execute_query("UPDATE Performance SET score = ? WHERE performance_id = ?", (score, performance_id))
            print("Performance updated successfully.")
            time.sleep(2)
            clear_screen()
        elif choice == "4":
            performance_id = input("Enter performance ID to delete: ")
            execute_query("DELETE FROM Performance WHERE performance_id = ?", (performance_id,))
            print("Performance deleted successfully.")
            time.sleep(2)
            clear_screen()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
# Main Menu
def main_menu():
    create_tables()
    while True:
        print("\n=== Learning and Assessment Management System ===")
        print("1. Manage Instructors")
        print("2. Manage Courses")
        print("3. Manage Students")
        print("4. Manage Enrollments")
        print("5. Manage Assessments")
        print("6. Track Performance")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            manage_instructors()
        elif choice == "2":
            manage_courses()
        elif choice == "3":
            manage_students()
        elif choice == "4":
            manage_enrollments()
        elif choice == "5":
            manage_assessments()
        elif choice == "6":
            Track_performance()
        elif choice == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def debug_table_info():

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Instructors);")
    rows = cursor.fetchall()
    conn.close()
    print("Table Info for Instructors:")
    for column in rows:
        print(column)

        # Comment this out temporarily if needed


if __name__ == "__main__":
    main_menu()

    create_tables()
    debug_table_info()  # Call this once for debugging
