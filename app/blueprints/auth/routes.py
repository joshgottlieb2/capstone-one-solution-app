from flask import render_template, request, redirect, url_for, flash
from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask_login import login_user, logout_user
from . forms import RegistrationForm 

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Handle login form requests
        user = User.query.filter_by(email=request.form['inputEmail']).first()
 
        if user is None:
            flash(f'User with email {request.form["inputEmail"]} does not exist.', 'danger')
        elif not user.check_my_password(request.form['inputPassword']):
            flash('Password is incorrect', 'danger')
        else:
            login_user(user)
            flash("User logged in", 'success')
            return redirect(url_for('main.home'))
        
        return render_template('login.html')
 
    else:  
        return render_template('login.html')
 
@app.route("/register", methods=["GET", "POST"])
def register():

    wtform = RegistrationForm()
    try:
        if request.method=="POST" and wtform.validate_on_submit():
            email = wtform.email.data
            # Query the database for a user with the passed in email
            check_user = User.query.filter_by(email=email).first()
            # If they already exist, show error. Otherwise, create user.
            if check_user is not None:
                flash('Error, user already exists', 'danger')
            else:
                email = wtform.email.data
                first_name = wtform.first_name.data
                last_name = wtform.last_name.data
                username = wtform.username.data
                password = wtform.password.data
                city = wtform.city.data
                state = wtform.state.data

                if request.form['inputPassword']:    
                    new_user = User(
                        email=request.form['inputEmail'],
                        password='',
                        username=request.form['inputUsername'],
                        first_name=request.form['inputFirstName'],
                        last_name=request.form['inputLastName'],
                        city=request.form['inputCity'],
                        state=request.form['inputState'],
                        )

                    new_user.hash_my_password(request.form['inputPassword'])
                    db.session.add(new_user)
                    db.session.commit()
    
                    flash('User created successfully, please login', 'success')
                    return redirect(url_for('auth.login'))
                else:
                    flash('Error, please try again', 'danger')

        elif request.method == 'POST':
            flash('Form data not valid', 'danger')
        else:
            return render_template('register.html', form=wtform)
    except:
        flash('Invalid Form Data: Please check your form')
        # raise Exception('Invalid Form Data: Please check your form')
    return render_template('register.html', form=wtform)

        
