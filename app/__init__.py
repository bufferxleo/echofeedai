from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models import db, User

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.routes.manager import manager_bp
    from app.routes.user import user_bp
    from app.routes.agent import agent_bp

    app.register_blueprint(manager_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(agent_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app