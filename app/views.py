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
      'title' : 'Contributing',
      'body' : """As an open source project, mitmproxy welcomes contributions 
                of all forms. If you would like to bring the project forward, 
                please consider contributing in the following areas:
                
                ToDo ...
                """
    },
  ]
  
  project = {'name' : 'Blockchain Tutorial'}
  return render_template('index.html',
                          title='vendetta.ch',
                          project=project,
                          posts=posts)
