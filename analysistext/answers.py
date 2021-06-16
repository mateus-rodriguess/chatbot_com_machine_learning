
def positive_reply_message(dist_prob_max, dist_prob_positivo):
    """
    answer if the message is positive
    """
    if dist_prob_max == "positivo" and dist_prob_positivo > 0.95:
        positive_response = "Parece que você esta satisfeito com a resposta, se tiver mais duvidas é so pergutar"
    elif dist_prob_max == "positivo" and dist_prob_positivo > 0.80:
        positive_response = "Obrigado, continue perguntando"
    elif dist_prob_max == "positivo" and dist_prob_positivo > 0.70:
        positive_response = "Ótimo, conseguir sanar sua duvida"
    elif dist_prob_max == "positivo" and dist_prob_positivo > 0.40:
        positive_response = "Ótimo, obrigado pelo feedback"
    else:
        positive_response = "Esta bem, vou tentar da uma resposta melhor ainda"
        
    return positive_response


def negative_reply_message(dist_prob_max, dist_prob_negativo):
    """
    responds if the message is negative
    """
    if dist_prob_max == "negativo" and dist_prob_negativo > 0.95:
        negative_response = "Não gostou da resposta? desculpa, não tenho resposta pra todas as suas perguntas :)"
    elif dist_prob_max == "negativo"  and dist_prob_negativo > 0.80:
        negative_response = "Não conseguir te responder corretamente? Talvez eu não entendi oque você pergutou, pergute novamente"
    elif dist_prob_max == "negativo"  and dist_prob_negativo > 0.70:
        negative_response = "Não esta satifeito com a resposta? Vou melhorar"
    elif dist_prob_max == "negativo"  and dist_prob_negativo > 0.40:
        negative_response = "Calma, vou melhorar minhas respostas, continue perguntando"
    else:
        negative_response = "Obrigado pelo feeback"
        
    return negative_response



