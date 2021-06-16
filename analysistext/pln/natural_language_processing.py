# pip install textblob
# python -m textblob.download_corpora
# pip install pandas

from textblob.classifiers import NaiveBayesClassifier
import pandas as pd

def PLN_CSV(text):
    """
    function that uses supervised machine learning to classify whether the message is positive or negative,
    at the end it returns a list

    (PLN) Natural Language Processing...

    """
    feelings_list = []
    try:
        feelings = pd.read_csv(
            'analysistext/pln/feelings.csv', sep=';', header=None)
        clf = NaiveBayesClassifier(feelings.values, format="csv")
    except:
        print("Não conseguiu abrir o arquivo ou ele não existe")
        # A  acurácia vai ser None
        clf = None
    # separação da probabilidade 
    dist_prob = clf.prob_classify(text)
    dist_prob_max = dist_prob.max()
    dist_prob_positivo = dist_prob.prob('positivo')
    dist_prob_negativo = dist_prob.prob('negativo')

    feelings_list.append({"dist_prob_max": dist_prob_max,
                         "dist_prob_positivo": dist_prob_positivo, "dist_prob_negativo": dist_prob_negativo})
    return feelings_list

