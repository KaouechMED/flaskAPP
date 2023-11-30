from MobileAPP import app
from flask import jsonify,request,redirect,url_for
from MobileAPP.models import User
from MobileAPP.forms import RegisterForm, LoginForm
from MobileAPP import db
from flask_login import login_user


# Example route returning a simple message
@app.route('/')
def helloworld():
    return jsonify({'message': 'Hello, world!'})

# Example route for a dashboard, returning a simple JSON response
@app.route('/dashboard')
def dashboard_page():
    return jsonify({'message': 'Welcome to the dashboard!'})

# Example route for the home page, returning a simple JSON response
@app.route('/home')
def home_page():
    return jsonify({'message': 'Welcome to the home page!'})

# Registration API endpoint
@app.route('/api/register', methods=['POST'])
def register_page():
    data = request.get_json()  
    form = RegisterForm(data=data)
    if form.validate():
        user_to_create = User(username=form.username.data,
                              email=form.email_address.data,
                              cin=form.cin.data,
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201  # Created
    if form.errors !={}:
        errors = [error for error in form.errors.items()]
        return jsonify({'errors': errors}), 400  # Return validation errors with status code 400
# Login API endpoint
@app.route('/api/login', methods=['POST'])
def login_page():
    data = request.get_json()
    form = LoginForm(data=data)
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            return redirect(url_for('user_profile', username=attempted_user.username))
        else:
            return jsonify({'error': 'Invalid username or password'}), 401  # Unauthorized
    if form.errors !={}:
        errors = [error for error in form.errors.items()]
        return jsonify({'errors': errors}), 400  # Return validation errors with status code 400

#user profile API endpoint
@app.route('/profile/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': f'Welcome to {user.username}\'s profile page!'})
    else:
        return jsonify({'error': 'User not found'}), 404  # Not Found

