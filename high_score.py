def high(words):
    words = words.split()  # Divide a string em uma lista de palavras
    high_score_word = ""  # Variável para armazenar a palavra com maior pontuação
    high_score = 0  # Variável para armazenar o valor da maior pontuação
    
    for word in words:
        score = sum(ord(letter) - ord('a') + 1 for letter in word)  # Calcula a pontuação da palavra
        if score > high_score:  # Se a pontuação da palavra for maior que a pontuação máxima atual
            high_score = score  # Atualiza a maior pontuação
            high_score_word = word  # Atualiza a palavra com maior pontuação
    
    return high_score_word

print(high('man i need a taxi up to ubud'))