from flask import jsonify, render_template, request, redirect, flash, url_for
from . import bp as app
from flask_login import current_user
from app import db
from app.blueprints.main.models import Suggest
from app.blueprints.main.models import Newsletter, Project

 
@app.route("/suggest", methods=["POST"])
def suggest():
    
    if current_user is None:
        flash(f'User must be logged in to use suggestion form.', 'danger')
        return redirect(url_for('login.html'))
    else:
        print(request.form)
        problem = request.form['inputProblem']
        action = request.form['inputAction']
        resource = request.form['inputResource']
        
        suggest = Suggest(problem=problem, action=action, resource=resource)

        db.session.add(suggest)
        db.session.commit()
        flash('New suggested project added successfully', 'success')
        return redirect(url_for('main.home'))

@app.route("/newsletter", methods=["POST"])
def newsletter():
    
    if current_user is None:
        flash(f'User must be logged in to sign up for Newsletter.', 'danger')
        return redirect(url_for('login.html'))
    else:
        email = request.form['newsletter-email']
        
        newsletter = Newsletter(email=email)

        db.session.add(newsletter)
        db.session.commit()
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('main.home'))


@app.route("/actions_completed", methods=["POST"])
def actions_completed():
    
    if not current_user.is_authenticated:
        flash(f'User must be logged in to submit a completed action.', 'danger')
        return redirect(url_for('auth.login'))
    else:
        id = request.form['inputId']
        target_date = request.form['inputTargetDate']
        problem = request.form['inputProblem']
        action = request.form['inputAction']
        goal = request.form['inputGoal']
        resource = request.form['inputResource']
        image_link = request.form['inputImageLink']
        actions_completed = request.form['inputActionsCompleted']
        
        # suggest = Suggest(problem=problem, action=action, resource=resource)
        project=Project.query.get(id)
        project.actions_completed=int(actions_completed)+1
        db.session.add(project)
        db.session.commit()
        flash('New suggested project added successfully', 'success')
        return redirect(url_for('main.home'))