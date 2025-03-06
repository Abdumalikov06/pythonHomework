import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# 1. Create the Books table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
""")

# 2. Insert data into Books table
books = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]

cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books)

# 3. Update Data (Change Year_Published of "1984" to 1950)
cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

# 4. Query Data (Retrieve Title and Author where Genre is 'Dystopian')
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
print("Dystopian Books:", cursor.fetchall())

# 5. Delete Data (Remove books published before 1950)
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

# 6. Bonus Task (Add a new column "Rating" and update data)
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
ratings = [
    ("To Kill a Mockingbird", 4.8),
    ("1984", 4.7),
    ("The Great Gatsby", 4.5)
]

for title, rating in ratings:
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))

# 7. Advanced Query (Retrieve all books sorted by Year_Published in ascending order)
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
print("Books sorted by Year_Published:", cursor.fetchall())

# Commit changes and close connection
conn.commit()
conn.close()
