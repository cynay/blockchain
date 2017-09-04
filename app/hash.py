from flask import render_template
from app import app

@app.route('/hash')
def hash():
  
  project = {'name' : 'Blockchain Tutorial'}
  return render_template('hash.html',
                          title='vendetta.ch',
                          project=project,
                          )
