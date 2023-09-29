from flask import render_template, redirect
from flask_login import login_user, logout_user

from app import app
from resources.users.models import UserModel
from .forms import LoginForm

@app.route('/')
def main():
  matrix = {
    'instructors': ['sean','dylan'],
    'students': ['raul','toby','josh','tom','mabel','milad','heather','seanait']
  }
  return render_template('index.jinja', instructors=matrix['instructors'], students=matrix['students'])

@app.route('/user/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    usernameEmail = form.usernameOrEmail.data
    user = UserModel.query.filter_by(username = usernameEmail).first()
    if not user:
      user = UserModel.query.filter_by(email = usernameEmail).first()
    if user and user.check_password(form.password.data):
      login_user(user)
      return redirect('/')
  return render_template('sign_in.j2', form=form)


@app.route('/user/logout')
def logout():
  logout_user()
  return redirect('/')