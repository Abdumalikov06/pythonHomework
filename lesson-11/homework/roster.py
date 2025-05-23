import sqlite3

# Create and connect to the database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Create the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);
""")

# Insert data into the table
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

conn.commit()

# Update Name of Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = "Ezri Dax"
WHERE Name = "Jadzia Dax"
""")

conn.commit()

# Query to retrieve Name and Age of all Bajoran species
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = "Bajoran"
""")
print("Bajoran characters:", cursor.fetchall())

# Delete all characters aged over 100 years
cursor.execute("""
DELETE FROM Roster WHERE Age > 100
""")

conn.commit()

# Add a new column Rank to the Roster table
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")

# Update the Rank values
cursor.executemany("""
UPDATE Roster SET Rank = ? WHERE Name = ?
""", [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])

conn.commit()

# Retrieve all characters sorted by Age in descending order
cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC
""")
print("Sorted characters by age:", cursor.fetchall())

# Close the connection
conn.close()
