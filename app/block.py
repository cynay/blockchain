from flask import render_template
from app import app

@app.route('/block')
def block():
  
  project = {'name' : 'Blockchain Tutorial'}
  return render_template('block.html',
                          title='vendetta.ch',
                          subtitle='block',
                          project=project,
                          )
