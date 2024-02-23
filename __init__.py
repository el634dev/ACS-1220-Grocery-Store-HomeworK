from flask import Flask, Blueprint
from flask_login import LoginManager
from grocery_app.routes import auth
from flask_bcrypt import Bcrypt
from grocery_app.models import User

app = Flask(__name__)
app.register_blueprint(auth)

# Login Manager Setup
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# -----------------------
# User Loader
@login_manager.user_loader
def load_user(user_id):
    """Load user"""
    return User.query.get(user_id)

bcrypt = Bcrypt(app)
