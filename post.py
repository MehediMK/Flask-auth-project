from flask import Blueprint,render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

post = Blueprint('post',__name__)

auth = HTTPBasicAuth()

users = {
    "mehedi": generate_password_hash("mehedi123"),
    "khan": generate_password_hash("kha123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@auth.login_required
@post.route('/post')
def index():
    return render_template('dashboard/index.html')