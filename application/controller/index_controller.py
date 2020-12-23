from flask import render_template, request
from application import app
from application.model.entity.produto import Produto
from application.model.dao.produto_dao import ProdutoDAO


@app.route("/")
def index():
    lstProduto = ProdutoDAO().get_listar_produtos()
    return render_template('index.html', lstProduto = lstProduto)

