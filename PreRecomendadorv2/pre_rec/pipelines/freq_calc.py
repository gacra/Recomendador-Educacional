import re
import nltk

from pre_rec import RE_TERMS

class FreqCalc(object):

    def __init__(self):
        nltk.download('stopwords')
        self.stopwords = nltk.corpus.stopwords.words('portuguese')

    def process_item(self, item, spider):

        terms_vector = re.findall(RE_TERMS, item.terms.lower())
        freq_vector = {}

        if terms_vector:
            for term in terms_vector:
                if (freq_vector.get(term) is None) \
                        and (term not in self.stopwords):
                    freq_vector[term] = FreqCalc.get_freq(terms_vector, term)

        item.terms = freq_vector
        # item.terms = {k:v for k, v in freq_vector.items() if v > 1}
        return item

    @staticmethod
    def get_freq(terms_vector, term):
        freq = terms_vector.count(term)
        return freq
