from email.policy import default
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask_login import UserMixin

user_project = db.Table('user_project',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    password = db.Column(db.String(250))
    date_registered = db.Column(db.DateTime, default=datetime.utcnow())
    actions_completed = db.relationship('Project', secondary=user_project, backref='users_completed')

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)

    def check_my_password(self, password):
        return check_password_hash(self.password, password)

    def get_user(self):
        return User.query.get(self.user_id)

    def __repr__(self):
        return f'<User: {self.username}>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_date = db.Column(db.Date, unique=True)
    problem = db.Column(db.String(250))
    action = db.Column(db.String(250))
    goal = db.Column(db.String(100))
    resource = db.Column(db.String(250))
    image_link = db.Column(db.String(250))
    

    def __repr__(self):
        return f'<Project: {self.problem}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

