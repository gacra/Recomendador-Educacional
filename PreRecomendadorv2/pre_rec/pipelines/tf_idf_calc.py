# import math
#
#
# class TfIdfCalc(object):
#     def open_spider(self, spider):
#         self.tam_conj_itens = 0
#         self.cont_termos = {}
#
#     def process_item(self, item, spider):
#         vet_termos = item.termos
#         vet_tf = {}
#
#         for termo in vet_termos:
#             if vet_tf.get(termo) is None:
#                 vet_tf[termo] = TfIdfCalc.tf(vet_termos, termo)
#                 self.add_termo(termo)
#         item
#
#     @staticmethod
#     def tf(vet_termos, termo):
#         freq = vet_termos.count(termo)
#         if freq > 0:
#             tf = 1 + math.log2(freq)
#         else:
#             tf = 0
#         return tf
#
#     def add_termo(self, termos_cont, termo):
#         if termos_cont.get(termo) is None:
#             self.cont_termos[termo] = 1
#         else:
#             termos_cont[termo] = termos_cont[termo] + 1
