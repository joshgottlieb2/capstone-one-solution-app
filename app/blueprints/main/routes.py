from multiprocessing import context
from flask import render_template
from flask_login import current_user
from app.blueprints.main.models import Project
from . import bp as app
from datetime import date, datetime


@app.route("/")
def home():
    projects = Project.query.all()
    context = {
        "projects": projects,
        "user": current_user
    }
    # today = datetime.datetime.utcnow()
    return render_template('index.html', **context)

@app.route('/past_projects')
def past_projects():
    return render_template('past_projects.html')

@app.route('/upcoming_projects')
def upcoming_projects():
    return render_template('upcoming_projects.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/calendar')
def calendar():
    return render_template('home.html')
@app.route('/community')
def community():
    return render_template('home.html')
# @app.route('/contact_us')
# def contact_us():
#     return render_template('contact_us.html')

