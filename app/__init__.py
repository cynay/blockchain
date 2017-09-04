from flask import Flask

app = Flask(__name__)
from app import views
from app import hash
from app import block
from app import blockchain
from app import distributed
from app import tokens
