from flask import jsonify, request, redirect, flash, url_for
from . import bp as app
from app.blueprints.main.models import Project
from flask_login import current_user
from app import db


 
@app.route("/create_post", methods=["POST"])
def suggest():
    status_input_problem = request.form['statusInputProblem']
    status_input_action = request.form['statusInputAction']
    status_input_resource = request.form['statusInputResource']
    
    user = current_user.id

    new_project = Project(problem=status_input_problem, action=status_input_action, resource=status_input_resource, user_id=user)

    db.session.add(new_project)
    db.session.commit()
    flash('New suggested project added successfully', 'success')
    return redirect(url_for('main.home'))