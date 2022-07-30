from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
import datetime

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # from app.blueprints.auth import bp as auth_bp
    # app.register_blueprint(auth_bp)

    # from app.blueprints.api import bp as api_bp
    # app.register_blueprint(api_bp)

    @app.context_processor
    def inject_today_date():
        return {'today_date': datetime.date.today()}

    return app
