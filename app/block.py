from flask import render_template
from app import app

item = 'block'

@app.route('/'+item)
def block():
  posts = [
    {
      'title' : 'first post',
      'body' : 'This is a test msg'
    }
  ]
  
  project = {'name' : 'Blockchain Tutorial'}
  return render_template(item+'.html',
                          title='vendetta.ch',
                          subtitle=item,
                          project=project,
                          posts=posts)
