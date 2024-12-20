import pytest
from main import execute_query, fetch_query, connect_db
import sqlite3

# Utility test to check if a table exists and fetch records
@pytest.fixture(scope="module")
def setup_database():
    # Setup the database before tests
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Instructors (id INTEGER PRIMARY KEY, name TEXT, email TEXT, specialization TEXT);")
    cursor.execute("DELETE FROM Instructors;")  # Clean up any existing data before tests
    conn.commit()
    conn.close()
    yield
    # Teardown after tests
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Instructors;")  # Drop the table after tests
    conn.commit()
    conn.close()

# Test execute_query - Insert data
def test_execute_query_insert(setup_database):
    execute_query("INSERT INTO Instructors (name, email, specialization) VALUES (?, ?, ?)", ("John Doe", "john@example.com", "Math"))
    
    # Check if the record was inserted
    result = fetch_query("SELECT * FROM Instructors WHERE name = ?", ("John Doe",))
    assert len(result) == 1
    assert result[0][1] == "John Doe"  # Ensure the name matches
    assert result[0][2] == "john@example.com"  # Ensure email matches
    assert result[0][3] == "Math"  # Ensure specialization matches

# Test fetch_query - Check data retrieval
def test_fetch_query(setup_database):
    # Insert test data
    execute_query("INSERT INTO Instructors (name, email, specialization) VALUES (?, ?, ?)", ("Jane Doe", "jane@example.com", "Science"))
    
    # Fetch the record
    result = fetch_query("SELECT * FROM Instructors WHERE name = ?", ("Jane Doe",))
    assert len(result) == 1
    assert result[0][1] == "Jane Doe"

# Test update operation
def test_execute_query_update(setup_database):
    execute_query("INSERT INTO Instructors (name, email, specialization) VALUES (?, ?, ?)", ("Alice", "alice@example.com", "Physics"))
    
    # Update the inserted record
    execute_query("UPDATE Instructors SET email = ? WHERE name = ?", ("alice_new@example.com", "Alice"))
    
    # Fetch the updated record
    result = fetch_query("SELECT * FROM Instructors WHERE name = ?", ("Alice",))
    assert result[0][2] == "alice_new@example.com"  # Verify the email has been updated

# Test delete operation
def test_execute_query_delete(setup_database):
    execute_query("INSERT INTO Instructors (name, email, specialization) VALUES (?, ?, ?)", ("Bob", "bob@example.com", "Chemistry"))
    
    # Delete the inserted record
    execute_query("DELETE FROM Instructors WHERE name = ?", ("Bob",))
    
    # Ensure the record is deleted
    result = fetch_query("SELECT * FROM Instructors WHERE name = ?", ("Bob",))
    assert len(result) == 0  # No results should be returned

# Test the instructor management feature manually (for demonstration, we'll assume it's called from main)
@pytest.mark.parametrize(
    "action, name, email, specialization", [
        ("add", "Charlie", "charlie@example.com", "Biology"),
        ("add", "David", "david@example.com", "Math")
    ]
)
def test_manage_instructors(action, name, email, specialization, setup_database):
    if action == "add":
        execute_query("INSERT INTO Instructors (name, email, specialization) VALUES (?, ?, ?)", (name, email, specialization))
        result = fetch_query("SELECT * FROM Instructors WHERE name = ?", (name,))
        assert len(result) == 1
        assert result[0][1] == name
        assert result[0][2] == email
        assert result[0][3] == specialization

# Test that fetch_query returns an empty list if there are no records
def test_empty_fetch_query(setup_database):
    result = fetch_query("SELECT * FROM Instructors WHERE name = ?", ("Non Existent Name",))
    assert result == []

