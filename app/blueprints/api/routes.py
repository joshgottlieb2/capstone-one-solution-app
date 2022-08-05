from flask import jsonify, render_template, request, redirect, flash, url_for
from . import bp as app
from flask_login import current_user
from app import db
from app.blueprints.main.models import Suggest
from app.blueprints.main.models import Newsletter

 
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

