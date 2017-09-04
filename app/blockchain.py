from flask import render_template
from app import app

item = 'blockchain'

@app.route('/'+item)
def blockchain():
  
  project = {'name' : 'Blockchain Tutorial'}
  blocks = [  
      { 
        'idx'   : 1,
        'nonce' : 1075,
        'prev'  : '0000000000000000000000000000000000000000000000000000000000000000',
      },
      { 
        'idx'   : 2,
        'nonce' : 7967,
        'prev'  : '000abdb31b25d34e30d1789e2e979c05874effd197a5ef9c20d3d160d82dd2ad',
      },
      { 
        'idx'   : 3,
        'nonce' : 596,
        'prev'  : '000cd23b18ccdb423fbd23d99fe1c1cbc66cfd6ca5c5bd3897744172b4e7a558',
      },
      { 
        'idx'   : 4,
        'nonce' : 7835,
        'prev'  : '000214d399b2c2c6faa2cbff76f80d9f5ce296c47e889e30f58e6c8174b672c0',
      },
      { 
        'idx'   : 5,
        'nonce' : 8197,
        'prev'  : '000fa968ca76d91a5882f240abe8946eee33e06bb2d7dc76710ef0afc4398288',
      }
    ]
  
  return render_template(item+'.html',
                          title='vendetta.ch',
                          subtitle=item,
                          project=project,
                          blocks=blocks,
                          chainnr=1)
