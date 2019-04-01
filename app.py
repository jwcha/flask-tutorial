#!/usr/bin/env python3
# vim: ft=python
#                                                 april's fools day - 2019.04.01

from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
   return 'Index Page'

@app.route('/hello')
def hello():
   return 'Hello, World!'

@app.route('/user/<username>')
def profile(username):
   # show the user profile for that user
   #return '{}\'s profile'.format(username)
   return f'{username}\'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
   # show the post with the given id, the id is an integer
   return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
   # show the subpath after /path/
   return 'Subpath %s' % subpath

@app.route('/login', method=['GET', 'POST'])
def login():
   if request.method == 'POST':
      return do_the_login()
   else:
      return show_the_login_form()

with app.test_request_context():
   print(url_for('index'))
   print(url_for('login'))
   print(url_for('login', next='/'))
   print(url_for('profile', username='John Doe'))