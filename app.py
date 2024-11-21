# Dante Solorzano
# CIS256 Fall 2024
# Programming 5

from flask import Flask, request, render_template_string, render_template
import bcrypt
import re # used to help with validation, since I know regex well

app = Flask(__name__)

def validation_check(str):
  pattern = r"^[a-zA-Z0-9_.-]*$"
  return bool(re.match(pattern, str))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validation_check(password) != True:
            return f'<span style="color: red;">The username can only contain letters A-Z, numbers 0-9, hyphens, and underscores!</span>'
        if validation_check(username) != True:
            return f'<span style="color: red;">The password can only contain letters A-Z, numbers 0-9, hyphens, and underscores!</span>'
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password.encode('utf-8'), salt) # salt helps keep it even more secure, hence why I opted to use regular bcrypt

        return f'Username: {username} Password: {password_hashed}<br><br><i>The password has been hashed here, which would be stored in the database alongside the salt used, not the actual password.</i>'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)