from flask import Flask
import os
from application.model.entity.produto import Produto

app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

from application.controller import index_controller
