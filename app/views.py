from flask import render_template
from flask import Markup
from app import app

@app.route('/')
@app.route('/index')
def index():
  posts = [
    {
      'title' : 'Blockchain technologies tutorial',
      'body'  : """This Project is mostly for self education about Blockchain
                technologies. """
    },
    {
      'title' : 'Contributing',
      'body'  : """As an open source project, we  welcomes contributions 
                of all forms. If you would like to bring the project forward, 
                please consider contributing in the following areas:
                
                ToDo ...
                """
    },
    {
      'title' : 'Donations',
      'body'  : Markup("""created by Yannic Schneider <br>
                XBT = 1PzqS24PHSRAWbe4ewDZeHAaijLyFnxqcq <br>
                ETH = 0x164306dD2F1bf443fCC5e2e427A9617F9F451A30 <br>
                """)
    },
  ]
  
  project = {'name' : 'Blockchain Tutorial'}
  return render_template('index.html',
                          title='vendetta.ch',
                          project=project,
                          posts=posts)
