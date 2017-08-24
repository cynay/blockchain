from flask import render_template
from app import app

@app.route('/hash')
def hash():
  posts = [
    {
      'title' : 'first post',
      'body' : 'This is a test msg'
    }
  ]
  
  project = {'name' : 'Blockchain Tutorial'}
  return render_template('hash.html',
                          title='vendetta.ch',
                          project=project,
                          posts=posts)
