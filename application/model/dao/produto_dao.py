from application.model.entity.produto import Produto
import json

class ProdutoDAO:

    def __init__(self):
        self._lstProduto = []
    
        with open('C:\\Users\\Jão\\Documents\\provap2linximpulse\\application\\view\static\\json\\products.json') as product_file:
            product_list = json.load(product_file)
    
        for product in product_list:
            self._lstProduto.append(Produto(product['id'],product['name'], product['image'], product['description'], product['oldPrice'], product['price'], product['installments']['value'], product['installments']['count']))

    def get_listar_produtos(self):
        return self._lstProduto