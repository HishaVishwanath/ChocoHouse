README - HISHA VISHWANATH
**************************************************************************************************

OVERVIEW
**************************************************************************************************

This project involves managing the data for a Chocolate house.

Task : Seasonal flavor offerings: Add seasonal flavors, check their availability and also mention the seasons , and also update or delete the flavors.  
	Ingredient inventory: Add all the ingredients , also the quantity will be specified and update or delete option will also be provided .
	Customer flavor suggestions and allergy concerns: Here the customers name along with their flavor suggestions and allergies if any will be specifies and this too shall contain update or delete option.
SQLite is used to create table and also to manage the database. 

FILE MANAGEMENT INSTRUCTIONS
**************************************************************************************************

Note : 
Move the downloaded unzipped file to the VisualStudio code.
**************************************************************************************************
SQL Queries 
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

*************************************************************************************************

Setting Up the Environment
Copy the file path and create a directory in terminal for that path.
**************************************************************************************************

Run the file :py app.py (in terminal)
then copy the running path and paste it in google tab ( http://localhost:5000 in your web browser).
**************************************************************************************************
Step 1: Enter the seasonal flavors which will be available for that particular season along with their availability status and also should mention the season when it will be available. Any changes in availability status can be updated and also the flavor can be deleted once it is used up in the view section.
Step 2: Enter the ingredients inventory and also mention their quantity. Further changes in quantity can be made in the view section where for addition of quantity of same ingredient can added just by specifying the numbers and reduction can be showed by using a '-' sign to indicate reduction before the number.
Step 3: Enter the customer name ,their suggestions in flavor and also the products they are allergic for in the customer suggestion block. any changes in this data can be made in view section if the allergies add up or they change their flavor suggestion.
Step 4:you can view all the sections to cross check whether the data entered is correct.

**************************************************************************************************
Tests:
The lists will be updated only on confirming with a OK button.
On testing of updation or deletion of ingredients on refreshing the page has ensured its stability.
On testing the code with the addition of same ingredients and also addition of quanity of those ingredients it has been accurate.


**************************************************************************************************
Outputs:

Task  results: All the data from seasonal flavors , ingredients inventory and customer suggestions database will be displayed.
**************************************************************************************************

ADDITIONAL NOTES :
This application helps in easy management of data in a very simple and easy way where any mistakes can be corrected and any changes can be updated easily.