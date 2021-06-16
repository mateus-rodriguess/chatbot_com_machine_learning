from analysistext.pln.natural_language_processing import PLN_CSV
from analysistext.answers import positive_reply_message, negative_reply_message


def reply_message(dist_prob_max, dist_prob_positivo, dist_prob_negativo):
    """
    function for text analysis with machine learning
    """
    if dist_prob_max == "positivo":
        resply = positive_reply_message(dist_prob_max, dist_prob_positivo)
    # dist_prob_max == "negativo"
    else:
        resply = negative_reply_message(dist_prob_max, dist_prob_negativo)
    return resply

def message_decision(message):
    """
    function that decides which to choose between machine learning
    """
    feelings = []
    feelings_list = PLN_CSV(message)

    max = feelings_list[0]["dist_prob_max"]
    positivo = feelings_list[0]["dist_prob_positivo"]
    negativo = feelings_list[0]["dist_prob_negativo"]

    feelings.append({"max": max, "positiva": positivo, "negativa": negativo})
   
    # vai retonar uma string para a função message_user
    print(message)
    print(feelings_list[0])
    print("-"*50)
    return reply_message(max, positivo, negativo)


def message_user(message):
    """
    function that receives the user's message and passes it on to the leanrg machine to analyze
    """
    result_text = message_decision(message)
    return result_text
