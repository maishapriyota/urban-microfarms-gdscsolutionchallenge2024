# Import necessary modules
from flask import Flask, jsonify, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, auth

# Define the House class
class House:
    def __init__(self, id, address, occupants, has_poultry, has_vegetable_garden, has_fish_pond):
        self.id = id
        self.address = address
        self.occupants = occupants
        self.has_poultry = has_poultry
        self.has_vegetable_garden = has_vegetable_garden
        self.has_fish_pond = has_fish_pond

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase app
cred = credentials.Certificate("credentials/serviceAccountKey.json")

firebase_admin.initialize_app(cred)

# List to store house objects
houses = []

# Route to retrieve all houses
@app.route('/houses', methods=['GET'])
def get_houses():
    return jsonify([house.__dict__ for house in houses])

# Route to create a new house
@app.route('/houses', methods=['POST'])
def create_house():
    data = request.json
    new_house = House(len(houses) + 1, data['address'], data['occupants'], data['has_poultry'], data['has_vegetable_garden'], data['has_fish_pond'])
    houses.append(new_house)
    return jsonify(new_house.__dict__), 201

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            # Sign in the user with email and password
            user = auth.sign_in_with_email_and_password(email, password)
            # Redirect to the dashboard
            return redirect(url_for('dashboard'))
        except auth.AuthError as e:
            return render_template('login.html', error=str(e))
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
def logout():
    # Implement logout logic
    # For example: auth.sign_out(user)
    return redirect(url_for('index'))

# Route for dashboard
@app.route('/dashboard')
def dashboard():
    # Implement dashboard logic
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)