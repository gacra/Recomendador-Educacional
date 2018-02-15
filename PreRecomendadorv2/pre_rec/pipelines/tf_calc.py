import math


class TfCalc(object):
    def open_spider(self, spider):
        self.tam_conj_itens = 0
        self.cont_termos = {}

    def process_item(self, item, spider):
        self.tam_conj_itens +=1

        vet_termos = item.termos
        vet_tf = {}

        if vet_termos:
            for termo in vet_termos:
                if vet_tf.get(termo) is None:
                    vet_tf[termo] = TfCalc.tf(vet_termos, termo)
                    self.add_termo(termo)

        item.termos = vet_tf
        return item

    @staticmethod
    def tf(vet_termos, termo):
        freq = vet_termos.count(termo)
        if freq > 0:
            tf = 1 + math.log2(freq)
        else:
            tf = 0
        return tf

    def add_termo(self, termo):
        if self.cont_termos.get(termo) is None:
            self.cont_termos[termo] = 1
        else:
            self.cont_termos[termo] += 1

    def close_spider(self, spider):
        spider.logger.info('Numero de itens: {}'.format(self.tam_conj_itens))
        # spider.logger.info('Cont_termos: {}'.format(self.cont_termos))
