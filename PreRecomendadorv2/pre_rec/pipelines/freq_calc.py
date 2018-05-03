
class FreqCalc(object):

    def process_item(self, item, spider):

        terms_vector = item.terms
        freq_vector = {}

        if terms_vector:
            for term in terms_vector:
                if freq_vector.get(term) is None:
                    freq_vector[term] = FreqCalc.get_freq(terms_vector, term)

        # item.terms = freq_vector
        item.terms = {k:v for k, v in freq_vector.items() if v > 1}
        return item

    @staticmethod
    def get_freq(terms_vector, term):
        freq = terms_vector.count(term)
        return freq
