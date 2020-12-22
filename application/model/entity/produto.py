class Produto:

    def _init_(self, id, nome, descricao, precoBase, precoEntrada, parcelamento):
        self._id = id 
        self._nome = nome
        self._descricao = descricao
        self._precoBase = precoBase
        self._precoEntrada = precoEntrada 
        self._parcelamento = parcelamento 

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def get_precoBase(self):
        return self._precoBase

    def get_precoEntrada(self):
        return self._precoEntrada

    def get_parcelamento(self):
        return self._parcelamento