import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('my_chocolate_house.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE seasonal_flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_name TEXT NOT NULL,
    availability TEXT NOT NULL,
    season TEXT NOT NULL,
    availability_status TEXT DEFAULT 'In Stock'
)
''')

cursor.execute('''
CREATE TABLE ingredient_inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL UNIQUE,
    quantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE customer_suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    flavor_suggestion TEXT,
    allergy_concerns TEXT
)
''')


# Insert sample values into seasonal_flavors
cursor.execute("INSERT INTO seasonal_flavors (flavor_name, availability, season, availability_status) VALUES (?, ?, ?, ?)", 
               ('Pumpkin Spice', 'Available', 'Fall', 'In Stock'))
cursor.execute("INSERT INTO seasonal_flavors (flavor_name, availability, season, availability_status) VALUES (?, ?, ?, ?)", 
               ('Peppermint', 'Available', 'Winter', 'In Stock'))
cursor.execute("INSERT INTO seasonal_flavors (flavor_name, availability, season, availability_status) VALUES (?, ?, ?, ?)", 
               ('Mango', 'Limited', 'Summer', 'Out of Stock'))
cursor.execute("INSERT INTO seasonal_flavors (flavor_name, availability, season, availability_status) VALUES (?, ?, ?, ?)", 
               ('Chocolate Mint', 'Available', 'Spring', 'In Stock'))
cursor.execute("INSERT INTO seasonal_flavors (flavor_name, availability, season, availability_status) VALUES (?, ?, ?, ?)", 
               ('Cinnamon Roll', 'Available', 'Fall', 'In Stock'))

# Insert sample values into ingredient_inventory
cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", ('Cocoa Powder', 50))
cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", ('Sugar', 100))
cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", ('Milk', 30))
cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", ('Butter', 20))
cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", ('Vanilla Extract', 10))
cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", ('Flour', 40))

# Insert sample values into customer_suggestions
cursor.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)", 
               ('Alice', 'Chocolate Chip Cookie Dough', 'Nuts'))
cursor.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)", 
               ('Bob', 'Salted Caramel', 'None'))
cursor.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)", 
               ('Charlie', 'Lemon Sorbet', 'Dairy'))
cursor.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)", 
               ('Diana', 'Mint Chocolate Chip', 'Gluten'))
cursor.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)", 
               ('Ethan', 'Matcha Green Tea', 'None'))

# Commit the changes and close the connection
conn.commit()
conn.close()


print("Database created and populated successfully!")


