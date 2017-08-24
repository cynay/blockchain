from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  posts = [
    {
      'title' : 'Blockchain technologies tutorial',
      'body' : """This Project is mostly for self education about Blockchain
                technologies. """
    },
    {
      'title' : 'Help',
      'body' : """If anyone would like to work together on a project please 
                contact me."""
    },
  ]
  
  project = {'name' : 'Blockchain Tutorial'}
  return render_template('index.html',
                          title='vendetta.ch',
                          project=project,
                          posts=posts)
