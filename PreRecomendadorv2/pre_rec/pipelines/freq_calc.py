import math


class FreqCalc(object):

    def open_spider(self, spider):
        self.tam_conj_itens = 0

    def process_item(self, item, spider):
        self.tam_conj_itens +=1

        vet_termos = item.termos
        vet_freq = {}

        if vet_termos:
            for termo in vet_termos:
                if vet_freq.get(termo) is None:
                    vet_freq[termo] = FreqCalc.obter_freq(vet_termos, termo)

        # item.termos = vet_freq
        item.termos = {k:v for k,v in vet_freq.items() if v>1}
        return item

    @staticmethod
    def obter_freq(vet_termos, termo):
        freq = vet_termos.count(termo)
        return freq

    def close_spider(self, spider):
        spider.logger.info('Numero de itens: {}'.format(self.tam_conj_itens))
