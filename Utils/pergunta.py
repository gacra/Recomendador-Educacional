from typing import List

class Pergunta:

    idAtual = 0

    def __init__(self, termosPerg: List[str]):
        """
Classe representativa das perguntas.
        :param id: Identificador númerico das perguntas
        :param termosPerg: Termos das perguntas (inicialmente uma lista de termos, depois um dic com (termo, tf_idf)
        """
        self.id = Pergunta.idAtual
        Pergunta.idAtual += 1
        self.termosPerg = termosPerg

    def __str__(self):
        return "{" + "'id': {}, 'termosPerg': {}".format(self.id, self.termosPerg) +"}"

    def __repr__(self):
        return "{" + "'id': {}, 'termosPerg': {}".format(self.id, self.termosPerg) + "}"

if __name__ == "__main__":
    print([Pergunta(['oi', 'td', 'bem']), Pergunta(['oi', 'vc', 'bem'])])