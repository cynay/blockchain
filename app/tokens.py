from flask import render_template
from app import app

item = 'tokens'

@app.route('/'+item)
def tokens():
  
  project = {'name' : 'Blockchain Tutorial'}
  chains = [ 
      { 'id'  : 1,
        'head': 'Peer A'
      },
      {
        'id'  : 2,
        'head': 'Peer B'
      },
      {
        'id'  : 3,
        'head': 'Peer C' 
      }
    ]
  blocks = [  
      { 
        'idx'   : 1,
        'nonce' : 2996,
        'txs'   : 
          [
            {
              'id'  : 0,
              'val' : '10.00',
              'from': 'Yannic',
              'to'  : 'Otto'
            },
            {
              'id'  : 1,
              'val' : '16.00',
              'from': 'Thess',
              'to'  : 'Annika'
            },
            {
              'id'  : 2,
              'val' : '100.00',
              'from': 'Ralph',
              'to'  : 'Yannic'
            },
            {
              'id'  : 1,
              'val' : '116.00',
              'from': 'Anouk',
              'to'  : 'Linux'
            },
          ],
        'prev'  : '0000000000000000000000000000000000000000000000000000000000000000',
      },
      { 
        'idx'   : 2,
        'nonce' : 2326,
        'txs'   : 
          [
            {
              'id'  : 0,
              'val' : '150.00',
              'from': 'Simone',
              'to'  : 'Nora'
            },
            {
              'id'  : 1,
              'val' : '1.00',
              'from': 'Jari',
              'to'  : 'Pan'
            },
            {
              'id'  : 2,
              'val' : '5.00',
              'from': 'Walo',
              'to'  : 'Mira'
            },
          ],
        'prev'  : '000b261089e79c6bc025fada6bd06d039bb6d5a22f39ea0e9da6d33c0a3fecea',
      },
      { 
        'idx'   : 3,
        'nonce' : 1683,
        'txs'   : 
          [
            {
              'id'  : 0,
              'val' : '1000.00',
              'from': 'Denise',
              'to'  : 'Florian'
            },
            {
              'id'  : 1,
              'val' : '1600.00',
              'from': 'Sara',
              'to'  : 'Moe'
            },
          ],
        'prev'  : '0006f6225bcd7066979b5822dfa53595c374429e5c006115d4f46e4723c44100',
      },
      { 
        'idx'   : 4,
        'nonce' : 2618,
        'txs'   : 
          [
            {
              'id'  : 0,
              'val' : '110.00',
              'from': 'Kevin',
              'to'  : 'Natascha'
            },
          ],
        'prev'  : '000cd3c570fafa181d6867d5cf5d22f870129bfa9d0e2e7e1e3be5a9ef024ec0',
      },
      { 
        'idx'   : 5,
        'nonce' : 4578,
        'txs'   : 
          [
            {
              'id'  : 0,
              'val' : '1000000.00',
              'from': 'Bigshot',
              'to'  : 'Yannic'
            },
            {
              'id'  : 1,
              'val' : '6.00',
              'from': 'Thess',
              'to'  : 'Yannic'
            },
            {
              'id'  : 2,
              'val' : '1110.00',
              'from': 'Simon',
              'to'  : 'Nora'
            },
            {
              'id'  : 3,
              'val' : '666.00',
              'from': 'Thess',
              'to'  : 'Yannic'
            },
          ],
        'prev'  : '000692002f0b0214eb425e889104b67bda7dadff22de7c6fa43e3330b7553351',
      }
    ]
  
  return render_template(item+'.html',
                          title='vendetta.ch',
                          subtitle=item,
                          project=project,
                          chains=chains,
                          blocks=blocks,
                          )
