from application.model.entity.Produto import Produto 
from application import listaCamisa

class ProdutoDAO:
    def _init_(self):
        self._listaCamisa = listaCamisa 

    def listar_produtos(self):
        return self._listaCamisa

    def buscar_por_id(self, id):
        for produto in range(0, len(self._listaCamisa)):
            if self._listaCamisa[produto].get_id() == int(id):
                return self._listaCamisa[produto]
        return None