from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# This function links sqlite
def get_db_connection():
    conn = sqlite3.connect('my_chocolate_house.db')
    conn.row_factory = sqlite3.Row
    return conn

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# To add seasonal flavors
@app.route('/add_flavor', methods=['POST'])
def add_seasonal_flavor():
    name = request.form['flavor_name']
    availability = request.form['availability']
    season = request.form['season']

    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO seasonal_flavors (flavor_name, availability, season) VALUES (?, ?, ?)", 
                     (name, availability, season))
        conn.commit()
        message = f"Added seasonal flavor: '{name}' for {season} season."
        status_code = 201
    except Exception as e:
        message = f"Error adding flavor: {str(e)}"
        status_code = 500
    finally:
        conn.close()

    return jsonify({"message": message}), status_code

# To update the availability status of a seasonal flavor
@app.route('/update_availability', methods=['POST'])
def update_availability():
    flavor_name = request.form['flavor_name']
    new_status = request.form['availability_status']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("UPDATE seasonal_flavors SET availability = ? WHERE flavor_name = ?", 
                       (new_status, flavor_name))
        conn.commit()
        
        if cursor.rowcount > 0:
            message = f"Updated availability status for '{flavor_name}' to '{new_status}'."
            status_code = 200
        else:
            message = f"No seasonal flavor found with the name '{flavor_name}'."
            status_code = 404
    except Exception as e:
        message = f"Error updating flavor: {str(e)}"
        status_code = 500
    finally:
        conn.close()

    return jsonify({"message": message}), status_code

# To display seasonal flavors after updating
@app.route('/flavors', methods=['GET'])
def display_flavors():
    conn = get_db_connection()
    try:
        flavors = conn.execute("SELECT * FROM seasonal_flavors").fetchall()
        message = "Flavors retrieved successfully."
        status_code = 200
    except Exception as e:
        flavors = []
        message = f"Error retrieving flavors: {str(e)}"
        status_code = 500
    finally:
        conn.close()
    
    return render_template('flavors.html', flavors=flavors)

# To delete a seasonal flavor
@app.route('/delete_flavor', methods=['POST'])
def delete_flavor():
    flavor_name = request.form['flavor_name']

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM seasonal_flavors WHERE flavor_name = ?", (flavor_name,))
        conn.commit()

        if cursor.rowcount > 0:
            message = f"Deleted seasonal flavor: '{flavor_name}'."
            status_code = 200
        else:
            message = f"No seasonal flavor found with the name '{flavor_name}'."
            status_code = 404
    except Exception as e:
        message = f"Error deleting flavor: {str(e)}"
        status_code = 500
    finally:
        conn.close()

    return jsonify({"message": message}), status_code


# To add an ingredient
@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    name = request.form['ingredient_name']
    quantity = int(request.form['quantity'])

    conn = get_db_connection()
    cursor = conn.cursor()

    # To check if the ingredient already exists
    cursor.execute("SELECT * FROM ingredient_inventory WHERE ingredient_name = ?", (name,))
    existing_ingredient = cursor.fetchone()

    if existing_ingredient:
        #ingredient for debugging
        print(f"DEBUG: Found existing ingredient: {existing_ingredient['ingredient_name']} with quantity {existing_ingredient['quantity']}")

        message = f"Ingredient '{name}' already exists with quantity {existing_ingredient['quantity']}. You can update it in the inventory."
        status_code = 400  # Use 400 for a "Bad Request" if trying to add a duplicate
    else:
        # Ingredient does not exist, add as new ingredient 
        cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()

        message = f"Added new ingredient: '{name}' with quantity: {quantity}"
        status_code = 201  # Use of 201 for "Created"

    conn.close()
    return jsonify({"message": message}), status_code

# To update an ingredient's quantity
@app.route('/update_ingredient', methods=['POST'])
def update_ingredient():
    ingredient_name = request.form['ingredient_name']
    new_quantity = int(request.form['quantity'])

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # this will execute update regardless of whether the ingredient exists
    cursor.execute("UPDATE ingredient_inventory SET quantity = ? WHERE ingredient_name = ?", (new_quantity, ingredient_name))
    conn.commit()

    if cursor.rowcount > 0:
        message = f"Updated ingredient: '{ingredient_name}', New quantity: {new_quantity}"
    else:
        message = f"No ingredient found with the name '{ingredient_name}'."
    
    conn.close()
    return jsonify({"message": message}), 200

# To delete an ingredient
@app.route('/delete_ingredient', methods=['POST'])
def delete_ingredient():
    ingredient_name = request.form['ingredient_name']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Perform the deletion
    cursor.execute("DELETE FROM ingredient_inventory WHERE ingredient_name = ?", (ingredient_name,))
    conn.commit()

    # Check if any row was deleted
    if cursor.rowcount > 0:
        message = f"Deleted ingredient: '{ingredient_name}'"
    else:
        message = f"No ingredient found with the name '{ingredient_name}'."
    
    conn.close()
    return jsonify({"message": message}), 200

# To display ingredients
@app.route('/ingredients', methods=['GET'])
def display_ingredients():
    conn = get_db_connection()
    ingredients = conn.execute("SELECT * FROM ingredient_inventory").fetchall()
    conn.close()
    return render_template('ingredients.html', ingredients=ingredients)

# To add a customer suggestion
@app.route('/add_suggestion', methods=['POST'])
def add_customer_suggestion():
    customer_name = request.form.get('customer_name')
    flavor_suggestion = request.form.get('flavor_suggestion')
    allergy_concerns = request.form.get('allergy_concerns', '')

    if not customer_name or not flavor_suggestion:
        return jsonify({"message": "Customer name and flavor suggestion are required."}), 400

    conn = get_db_connection()
    conn.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)",
                 (customer_name, flavor_suggestion, allergy_concerns))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Added customer suggestion from: '{customer_name}'"}), 201

# To update a customer suggestion
@app.route('/update_suggestion', methods=['POST'])
def update_suggestion():
    suggestion_id = request.form.get('id')
    flavor_suggestion = request.form.get('flavor_suggestion')
    allergy_concerns = request.form.get('allergy_concerns', '')

    if not suggestion_id or not flavor_suggestion:
        return jsonify({"message": "Suggestion ID and new flavor suggestion are required."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE customer_suggestions SET flavor_suggestion = ?, allergy_concerns = ? WHERE id = ?",
                   (flavor_suggestion, allergy_concerns, suggestion_id))
    conn.commit()

    if cursor.rowcount > 0:
        message = f"Updated suggestion with ID {suggestion_id}."
    else:
        message = f"No suggestion found with ID {suggestion_id}."

    conn.close()
    return jsonify({"message": message}), 200

# To delete a customer suggestion
@app.route('/delete_suggestion', methods=['POST'])
def delete_suggestion():
    suggestion_id = request.form.get('suggestion_id')

    if not suggestion_id:
        return jsonify({"message": "Suggestion ID is required."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM customer_suggestions WHERE id = ?", (suggestion_id,))
    conn.commit()

    if cursor.rowcount > 0:
        message = f"Deleted suggestion with ID {suggestion_id}."
    else:
        message = f"No suggestion found with ID {suggestion_id}."

    conn.close()
    return jsonify({"message": message}), 200

# To display customer suggestions
@app.route('/suggestions', methods=['GET'])
def display_suggestions():
    try:
        conn = get_db_connection()
        suggestions = conn.execute("SELECT * FROM customer_suggestions").fetchall()
        conn.close()
        return render_template('suggestions.html', suggestions=suggestions)
    except Exception as e:
        return jsonify({"message": "An error occurred while retrieving suggestions."}), 500

if __name__ == '__main__':
    app.run(debug=True)
