from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# REST API Endpoints

@app.route('/users', methods=['GET'])
def get_users():
    """Fetch all users"""
    users = User.query.all()
    return jsonify([
        {"id": user.id, "name": user.name, "email": user.email, "age": user.age}
        for user in users
    ])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Fetch a specific user"""
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email, "age": user.age})

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.json
    new_user = User(name=data['name'], email=data['email'], age=data.get('age'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully", "user_id": new_user.id}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    user = User.query.get_or_404(user_id)
    data = request.json
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.age = data.get('age', user.age)
    db.session.commit()
    return jsonify({"message": "User updated successfully"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

# Run the server
if __name__ == "__main__":
    app.run(debug=True, port=5000)
