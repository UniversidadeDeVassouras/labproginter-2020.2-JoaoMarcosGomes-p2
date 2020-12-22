from flask import render_template, request
from application import app
from application.model.entity.Produto import Produto
from application import listaCamisa
from application.model.dao.produto_dao import ProdutoDAO


@app.route ('/')
def home():
    produto_dao = ProdutoDAO()
    for produto in listaCamisa:
        produto_id = produto.get_id()
    produto = produto_dao.buscar_por_id(produto_id)
    return render_template("index.html", listaCamisa = listaCamisa, produto = produto )