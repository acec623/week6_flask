from . import bp as auth_bp
# from auth import bp as auth_bp
from flask import render_template, flash, redirect
from .forms import RegisterForm, SignInForm
from app.blueprints.social.models import User
from flask_login import login_user, logout_user, login_required


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        u = User(username=username, email=email, password_hash='',
                 first_name=first_name, last_name=last_name)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists, try again.')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exists, try again')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
            # db.session.add(u)
            # db.session.commit()
            flash(f'Request to register {username} successful')
            return redirect('/')
    return render_template('register.jinja', form=form)


@auth_bp.route('/signin', methods=['GET','POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or Password was incorrect, try again.')
            return redirect('/signin')
        flash(f'{username} succesfully signed in!')
        login_user(user_match, remember=False)
        return redirect('/')
    return render_template('signin.jinja',sign_in_form=form)


@login_required
@auth_bp.route('/signout')
def signout():
    logout_user()
    return redirect('/')