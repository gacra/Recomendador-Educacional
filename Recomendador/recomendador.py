import math

class Similaridade():
    """
    Classe para o cálculo da similaridade de ítens com um perfil do usuário
    """
    def __init__(self, perfilVet: dict):
        """
Classe para o cálculo da similaridade de ítens com um perfil do usuário
        :param perfilVet: Dicionário com os termos (chaves) e seus pesos (valores) do perfil do usuário
        """
        self.perfilVet = perfilVet
        self.perfilMod = 0
        for termoPerfilPeso in perfilVet.values():
            self.perfilMod += termoPerfilPeso*termoPerfilPeso
        self.perfilMod = math.sqrt(self.perfilMod)


    def simCosseno(self, itemVet: dict) -> float:
        """
Calcula a similaridade por cosseno do item com o perfil do usuário inserido na criação da classe
        :param itemVet: Dicionário com os termos (chaves) e seus pesos (valores) o ítem
        :return: Similaridade do item com o perfil
        """
        num = 0
        termoMod = 0
        for termoItemNome, termoItemPeso in itemVet.items():
            termoPerfilPeso = self.perfilVet.get(termoItemNome)
            if termoPerfilPeso is not None:
                num += termoPerfilPeso * termoItemPeso
            termoMod += termoItemPeso*termoItemPeso
        termoMod = math.sqrt(termoMod)
        sim = num / (termoMod*self.perfilMod)

        return sim

if __name__ == '__main__':
    itemVet = {'palavra1': 3, 'palavra2:': 5, 'palavra3': 4, 'palavra4': 1, 'palavra5': 2}
    perfilVet = {'palavra1': 3, 'palavra2:': 4, 'palavra3': 3, 'palavra4': 1}

    sim = Similaridade(perfilVet)

    print(sim.simCosseno(itemVet))
